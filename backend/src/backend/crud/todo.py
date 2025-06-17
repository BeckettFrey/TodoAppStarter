# File: backend/src/backend/crud/todo.py
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId, errors
from backend.schemas.todo import TodoUpdate, TodoResponse
from typing import List, Optional

COLLECTION_NAME = "todo_db"

def parse_todo(todo: dict) -> TodoResponse:
    """Convert a MongoDB document to a TodoResponse model."""
    return TodoResponse(
        _id=str(todo["_id"]),
        title=todo["title"],
        completed=todo["completed"]
    )

async def get_all_todos(db: AsyncIOMotorDatabase) -> List[TodoResponse]:
    """Retrieve all todos from the database."""
    todos = await db[COLLECTION_NAME].find().to_list(100)
    return [parse_todo(todo) for todo in todos]

async def get_todo_by_id(db: AsyncIOMotorDatabase, todo_id: str) -> Optional[TodoResponse]:
    """Retrieve a todo by its ID."""
    try:
        todo = await db[COLLECTION_NAME].find_one({"_id": ObjectId(todo_id)})
        return parse_todo(todo) if todo else None
    except errors.InvalidId:
        return None

async def create_todo(db: AsyncIOMotorDatabase, todo: dict) -> TodoResponse:
    doc = todo.model_dump() if hasattr(todo, "model_dump") else todo
    insert_result = await db[COLLECTION_NAME].insert_one(doc)
    created = await db[COLLECTION_NAME].find_one({"_id": insert_result.inserted_id})
    return parse_todo(created)


async def update_todo(db: AsyncIOMotorDatabase, todo_id: str, update_data: TodoUpdate) -> Optional[TodoResponse]:
    """Update a todo by its ID."""
    try:
        update = {k: v for k, v in update_data.dict().items() if v is not None}
        result = await db[COLLECTION_NAME].update_one({"_id": ObjectId(todo_id)}, {"$set": update})
        if result.modified_count == 0:
            return None
        updated = await db[COLLECTION_NAME].find_one({"_id": ObjectId(todo_id)})
        return parse_todo(updated)
    except errors.InvalidId:
        return None

async def delete_todo(db: AsyncIOMotorDatabase, todo_id: str) -> bool:
    """Delete a todo by its ID."""
    try:
        result = await db[COLLECTION_NAME].delete_one({"_id": ObjectId(todo_id)})
        return result.deleted_count == 1
    except errors.InvalidId:
        return False