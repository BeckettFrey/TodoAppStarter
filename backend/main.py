# File: backend/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.mongodb import db

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await db.command("ping")
        print("✅ MongoDB connection successful.")
    except Exception as e:
        print("❌ MongoDB connection failed:", e)
    yield
    # Optionally: await db.client.close()

app = FastAPI(lifespan=lifespan)

# Import routes AFTER app creation
from routes.todo import router as todo_router

app.include_router(todo_router, prefix="/api", tags=["todos"])
