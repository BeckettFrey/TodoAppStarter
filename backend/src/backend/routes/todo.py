# File: backend/src/backend/routes/todo.py
from fastapi import APIRouter, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from backend.database.mongodb import db
from backend.schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from backend.crud.todo import (
    get_all_todos,
    get_todo_by_id,
    create_todo,
    update_todo,
    delete_todo
)

router = APIRouter()

def get_db() -> AsyncIOMotorDatabase:
    return db

@router.get("/todos", response_model=list[TodoResponse])
async def read_todos(db: AsyncIOMotorDatabase = Depends(get_db)):
    return await get_all_todos(db)

@router.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"} 

@router.get("/todos/{todo_id}", response_model=TodoResponse)
async def read_todo(todo_id: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    todo = await get_todo_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/todos", response_model=TodoResponse)
async def create_new_todo(todo: TodoCreate, db: AsyncIOMotorDatabase = Depends(get_db)):
    return await create_todo(db, todo)

@router.put("/todos/{todo_id}", response_model=TodoResponse)
async def update_existing_todo(todo_id: str, update: TodoUpdate, db: AsyncIOMotorDatabase = Depends(get_db)):
    updated = await update_todo(db, todo_id, update)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found or not modified")
    return updated

@router.delete("/todos/{todo_id}")
async def delete_existing_todo(todo_id: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    success = await delete_todo(db, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}