# File: backend/src/backend/database/mongodb.py
from motor.motor_asyncio import AsyncIOMotorClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = getenv("MONGODB_URL")
MONGO_DB_NAME = getenv("MONGO_DB_NAME")

if not MONGODB_URL:
    raise RuntimeError("MONGODB_URL environment variable is not set")
if not MONGO_DB_NAME:
    raise RuntimeError("MONGO_DB_NAME environment variable is not set")

client = AsyncIOMotorClient(MONGODB_URL)
db = client[MONGO_DB_NAME]


