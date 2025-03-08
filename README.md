# Pullse Ticket Management API

A scalable backend API for managing support tickets with real-time updates, built for the Pullse Backend Developer Assignment.

## Setup Instructions

### Prerequisites
- **Python 3.10+**: Install from [python.org](https://www.python.org/downloads/).
- **Git**: Install from [git-scm.com](https://git-scm.com/downloads/).
- **Supabase Account**: Sign up at [supabase.com](https://supabase.com) and create a project.
- **Ably Account**: Sign up at [ably.com](https://ably.com) and get an API key.

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/pullse-ticket-api.git
   cd pullse-ticket-api

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Configure Environment Variables**:
   Create a .env file in the root directory with the following:
   SUPABASE_URL=https://your-supabase-project.supabase.co
   SUPABASE_KEY=your-supabase-anon-key
   ABLY_API_KEY=your-ably-api-key
   - Replace the placeholders with your Supabase URL, anon key, and Ably API key.
5. **Initialize the Database**:
   In your Supabase dashboard, go to SQL Editor.
   Copy and run the contents of migrations/init.sql to create the tickets and agents tables.

6. **Run the Application**:
   uvicorn src.main:app --reload
  - The API will be available at http://localhost:8000.
### API Documentation
   The API is fully documented using Swagger/OpenAPI specifications, auto-generated by FastAPI.

     * Interactive Swagger UI: Access at http://localhost:8000/docs after running the app.
     * Raw OpenAPI JSON: Available at http://localhost:8000/openapi.json.
   **Key Endpoints**
   **Ticket Management**
      - POST /api/tickets: Create a new ticket.
         Payload: {"title": "Login Issue", "description": "Cannot log in", "status": "open", "priority": "medium", "assigned_to": "uuid"}
     -  GET /api/tickets: List tickets (optional filters: ?status=open&priority=high).
     -  GET /api/tickets/{id}: Retrieve a specific ticket by UUID.
     -  PATCH /api/tickets/{id}: Update ticket details.
         Payload: {"status": "resolved"}
     -  DELETE /api/tickets/{id}: Delete a ticket.
   **Agent Management**
      - POST /api/agents: Create a new agent.
         Payload: {"name": "John Doe", "email": "john@example.com"}
      - GET /api/agents: List all agents.
   **Real-Time Updates**
      Events (ticket_created, ticket_updated) are broadcasted via Ably on the tickets channel.

### Design Decisions and Challenges Faced
**Design Decisions**
1. **Framework Choice: FastAPI**
   - Why: Selected for its asynchronous capabilities, built-in Swagger generation, and Pydantic integration for type safety (aligning with the TypeScript requirement). It’s lightweight yet powerful for RESTful APIs.
   - Benefit: Simplifies endpoint creation and real-time integration with Ably.
2. **Pydantic for Type Safety**
   - Why: Used Pydantic models (Ticket, Agent) with enums to enforce TypeScript-like validation and structure, ensuring robust payload handling.
   - Benefit: Reduces runtime errors and provides clear API contracts.
3. **Supabase as Database**
   - Why: Chosen for its PostgreSQL backend and simple Python client, avoiding the need for complex ORM setup.
   - Benefit: Quick setup with SQL migrations and seamless CRUD operations.
4. **Ably for Real-Time Updates**
   - Why: Integrated Ably for its reliable pub/sub system to broadcast ticket status changes.
   - Benefit: Enables real-time client updates without managing WebSocket servers manually.
5. **Modular Structure**
   - Why: Organized code into src/routes, src/models, etc., for maintainability and scalability.
   - Benefit: Easy to extend or debug individual components.
**Challenges Faced**
1. **Async Integration with Ably**
- Issue: Initial RuntimeWarning due to unawaited channel.publish coroutine in realtime.py.
- Solution: Converted publish_event to an async function and added await, aligning with FastAPI’s async routes.
- Learning: Highlighted the importance of matching async/sync contexts in Python.
2. **Type Consistency with Supabase**
- Issue: Supabase returns data as dictionaries, which needed mapping to Pydantic models.
- Solution: Configured Pydantic with from_attributes=True and ensured UUIDs were cast correctly.
- Learning: Bridging database responses with typed models requires careful alignment.
3. **Real-Time Testing**
- Issue: Verifying Ably events required a separate client setup.
- Solution: Used a simple JavaScript client to subscribe and log events, confirming broadcasts worked.
- Learning: Real-time systems need end-to-end testing beyond API calls.
4. **Time Constraint**
- Issue: Balancing feature completeness with the tight deadline (March 8th, 2025, 12:00 PM).
- Solution: Focused on core CRUD and real-time functionality, leveraging FastAPI’s rapid development features.
- Learning: Prioritization is key under time pressure.
