from pydantic import BaseModel, Field, EmailStr
from typing import Literal, Optional
from uuid import UUID
from datetime import datetime

# Enums
TicketStatus = Literal["open", "in_progress", "resolved", "closed"]
TicketPriority = Literal["low", "medium", "high", "urgent"]

# Ticket Models
class TicketBase(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    status: TicketStatus = "open"
    priority: TicketPriority = "low"
    assigned_to: Optional[str] = None

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TicketStatus] = None
    priority: Optional[TicketPriority] = None
    assigned_to: Optional[str] = None

class Ticket(TicketBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Agent Models
class AgentBase(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr

class AgentCreate(AgentBase):
    pass

class Agent(AgentBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True