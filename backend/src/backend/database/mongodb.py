# File: backend/src/backend/database/mongodb.py
from motor.motor_asyncio import AsyncIOMotorClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = getenv("MONGODB_URL", "mongodb://localhost:27017")
MONGO_DB_NAME = getenv("MONGO_DB_NAME", "todo_db")

client = AsyncIOMotorClient(MONGODB_URL)
db = client[MONGO_DB_NAME]


