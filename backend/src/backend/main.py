# File: backend/src/backend/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.database.mongodb import db, client

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await db.command("ping")
        print("✅ MongoDB connection successful.")
    except Exception as e:
        print("❌ MongoDB connection failed:", e)
    yield

app = FastAPI(lifespan=lifespan)
@app.on_event("shutdown")
async def shutdown():
    client.close()

# Import routes AFTER app creation
from backend.routes.todo import router as todo_router

app.include_router(todo_router, prefix="/api", tags=["todos"])

