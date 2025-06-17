# File: backend/src/backend/models/todo.py
from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    completed: bool = False
