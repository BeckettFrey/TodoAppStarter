# File: backend/src/backend/schemas/todo.py
from pydantic import BaseModel, Field
from typing import Optional

class TodoBase(BaseModel):
    title: str
    completed: bool

class TodoCreate(TodoBase):
     pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None
    
class TodoResponse(TodoBase):
    id: str = Field(..., alias="_id")

    class Config:
        validate_by_name = True
