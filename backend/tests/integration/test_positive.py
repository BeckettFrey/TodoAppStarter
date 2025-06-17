# File: backend/tests/integration/test_positive.py
import requests

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000
BASE_URL = f"http://{SERVER_HOST}:{SERVER_PORT}"

def test_get_all_todos():
    response = requests.get(f"{BASE_URL}/api/todos")
    assert response.status_code == 200
    todos = response.json()
    assert isinstance(todos, list)

def test_create_todo():
    todo_data = {
        "title": "Test Todo",
        "completed": False,
    }
    response = requests.post(f"{BASE_URL}/api/todos", json=todo_data)
    assert response.status_code == 200
    todo = response.json()
    assert todo["title"] == todo_data["title"]
    assert todo["completed"] == todo_data["completed"]
    assert "_id" in todo

def test_get_todo_by_id():
    # First, create a todo item
    todo_data = {
        "title": "Test Todo",
        "completed": False
    }
    response = requests.post(f"{BASE_URL}/api/todos", json=todo_data)
    assert response.status_code == 200
    todo = response.json()
    assert "_id" in todo

    # Now, retrieve the todo item by ID
    todo_id = todo["_id"]
    response = requests.get(f"{BASE_URL}/api/todos/{todo_id}")
    assert response.status_code == 200
    retrieved_todo = response.json()
    assert retrieved_todo["_id"] == todo_id
    assert retrieved_todo["title"] == todo_data["title"]
    assert retrieved_todo["completed"] == todo_data["completed"]

def test_update_todo():
    # First, create a todo item
    todo_data = {
        "title": "Test Todo",
        "completed": False
    }
    response = requests.post(f"{BASE_URL}/api/todos", json=todo_data)
    assert response.status_code == 200
    todo = response.json()
    assert "_id" in todo

    # Now, update the todo item
    todo_id = todo["_id"]
    update_data = {
        "title": "Updated Test Todo",
        "completed": True
    }
    response = requests.put(f"{BASE_URL}/api/todos/{todo_id}", json=update_data)
    assert response.status_code == 200
    updated_todo = response.json()
    assert updated_todo["_id"] == todo_id
    assert updated_todo["title"] == update_data["title"]
    assert updated_todo["completed"] == update_data["completed"]

def test_delete_todo():
    # First, create a todo item
    todo_data = {
        "title": "Test Todo",
        "completed": False
    }
    response = requests.post(f"{BASE_URL}/api/todos", json=todo_data)
    assert response.status_code == 200
    todo = response.json()
    assert "_id" in todo

    # Now, delete the todo item
    todo_id = todo["_id"]
    response = requests.delete(f"{BASE_URL}/api/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted"}

    # Verify that the todo item is no longer retrievable
    response = requests.get(f"{BASE_URL}/api/todos/{todo_id}")
    assert response.status_code == 404