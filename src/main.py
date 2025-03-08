from fastapi import FastAPI
from src.routes import tickets, agents

app = FastAPI(
    title="Pullse Ticket Management API",
    description="A scalable ticket management system with real-time updates.",
    version="1.0.0"
)

app.include_router(tickets.router)
app.include_router(agents.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Pullse Ticket Management API"}