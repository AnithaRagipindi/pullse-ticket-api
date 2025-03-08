from typing import Optional
from uuid import UUID
from fastapi import APIRouter, HTTPException
from src.database import supabase
from src.models import Ticket, TicketCreate, TicketUpdate
from src.realtime import publish_event

router = APIRouter(prefix="/api/tickets", tags=["Tickets"])

@router.post("/", response_model=Ticket)
async def create_ticket(ticket: TicketCreate):
    data = ticket.dict()
    response = supabase.table("tickets").insert(data).execute()
    new_ticket = response.data[0]
    await publish_event("tickets", "ticket_created", new_ticket)
    return new_ticket

@router.get("/", response_model=list[Ticket])
async def list_tickets(status: Optional[str] = None, priority: Optional[str] = None):
    query = supabase.table("tickets").select("*")
    if status:
        query = query.eq("status", status)
    if priority:
        query = query.eq("priority", priority)
    response = query.execute()
    return response.data

@router.get("/{id}", response_model=Ticket)
async def get_ticket(id: UUID):
    response = supabase.table("tickets").select("*").eq("id", str(id)).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return response.data[0]

@router.patch("/{id}", response_model=Ticket)
async def update_ticket(id: UUID, ticket: TicketUpdate):
    data = {k: v for k, v in ticket.dict().items() if v is not None}
    data["updated_at"] = "now()"
    response = supabase.table("tickets").update(data).eq("id", str(id)).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Ticket not found")
    updated_ticket = response.data[0]
    await publish_event("tickets", "ticket_updated", updated_ticket)
    return updated_ticket

@router.delete("/{id}")
async def delete_ticket(id: UUID):
    response = supabase.table("tickets").delete().eq("id", str(id)).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"message": "Ticket deleted"}
