# Pullse Ticket Management API

A scalable backend API for managing support tickets with real-time updates.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pullse-ticket-api

2. Set up a virtual environment and install dependencies:
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
3. Configure environment variables in .env.
4. Initialize the Supabase database with migrations/init.sql.
5. Run the application:
    uvicorn src.main:app --reload
API Documentation
Swagger UI: /docs
OpenAPI spec: /openapi.json