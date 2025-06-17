# File: backend/tests/unit/test_crud.py
import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from backend.crud.todo import (
    get_all_todos, get_todo_by_id, create_todo,
    update_todo, delete_todo, COLLECTION_NAME
)
from backend.schemas.todo import TodoUpdate

pytestmark = pytest.mark.asyncio

# -------------------------
# Fixture for test DB
# -------------------------
@pytest_asyncio.fixture
async def db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    test_db = client["test_db"]
    await test_db[COLLECTION_NAME].delete_many({})
    yield test_db
    await test_db[COLLECTION_NAME].delete_many({})

# -------------------------
# Helper
# -------------------------
def make_todo(title="Test Todo", completed=False):
    return {"title": title, "completed": completed}
from backend.schemas.todo import TodoCreate, TodoResponse

# -------------------------
# Actual Test Functions
# -------------------------

async def test_create_and_get_todo(db):
    todo = TodoCreate(**make_todo())
    created = await create_todo(db, todo)
    assert isinstance(created, TodoResponse)
    retrieved = await get_todo_by_id(db, created.id)
    assert retrieved.title == todo.title
    assert retrieved.completed == todo.completed

async def test_get_all_todos(db):
    await create_todo(db, TodoCreate(**make_todo("First")))
    await create_todo(db, TodoCreate(**make_todo("Second")))
    todos = await get_all_todos(db)
    assert len(todos) == 2
    titles = [t.title for t in todos]
    assert "First" in titles and "Second" in titles

async def test_get_todo_by_invalid_id(db):
    todo = await get_todo_by_id(db, "invalid")
    assert todo is None

async def test_update_todo(db):
    created = await create_todo(db, TodoCreate(**make_todo("Original", False)))
    update_data = TodoUpdate(title="Updated", completed=True)
    updated = await update_todo(db, created.id, update_data)
    assert updated.title == "Updated"
    assert updated.completed is True

async def test_update_todo_invalid_id(db):
    update_data = TodoUpdate(title="Nope")
    updated = await update_todo(db, "invalid", update_data)
    assert updated is None

async def test_delete_todo(db):
    created = await create_todo(db, TodoCreate(**make_todo()))
    deleted = await delete_todo(db, created.id)
    assert deleted is True
    assert await get_todo_by_id(db, created.id) is None

async def test_delete_todo_invalid_id(db):
    deleted = await delete_todo(db, "invalid")
    assert deleted is False
