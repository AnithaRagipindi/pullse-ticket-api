from fastapi import APIRouter, HTTPException
from src.database import supabase
from src.models import Agent, AgentCreate

router = APIRouter(prefix="/api/agents", tags=["Agents"])

@router.post("/", response_model=Agent)
async def create_agent(agent: AgentCreate):
    response = supabase.table("agents").insert(agent.dict()).execute()
    return response.data[0]

@router.get("/", response_model=list[Agent])
async def list_agents():
    response = supabase.table("agents").select("*").execute()
    return response.data