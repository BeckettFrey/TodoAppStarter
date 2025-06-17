# File: backend/tests/integration/test_negative.py
import requests

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000
BASE_URL = f"http://{SERVER_HOST}:{SERVER_PORT}"

def test_get_nonexistent_todo():
    response = requests.get(f"{BASE_URL}/api/todos/nonexistent_id")
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}

def test_create_todo_with_invalid_data():
    todo_data = {
        "completed": False
    }
    response = requests.post(f"{BASE_URL}/api/todos", json=todo_data)
    assert response.status_code == 422  # Unprocessable Entity
    assert "title" in response.json()["detail"][0]["loc"]

    todo_data = {
        "title": "Test Todo",
        "completed": "not_a_boolean"  # Invalid type
    }
    response = requests.post(f"{BASE_URL}/api/todos", json=todo_data)
    assert response.status_code == 422
    assert "completed" in response.json()["detail"][0]["loc"]

def test_update_nonexistent_todo():
    update_data = {
        "title": "Updated Test Todo",
        "completed": True
    }
    response = requests.put(f"{BASE_URL}/api/todos/nonexistent_id", json=update_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found or not modified"}

def test_delete_nonexistent_todo():
    response = requests.delete(f"{BASE_URL}/api/todos/nonexistent_id")
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}
