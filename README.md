# 📝 TodoAppStarter

**TodoAppStarter** is a minimal FastAPI + MongoDB backend — clean, Dockerized, and structured for clarity.

> 🧠 This project is a **personal building block** where I introduced myself to FastAPI, explored the `mongosh` CLI, dockerized a deployable MongoDB + FastAPI backend, enforced PEP and modern Python best practices, and applied clean coding principles

## 🔧 Tech Stack

* [Python 3.11](https://docs.python.org/3.11/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [MongoDB](https://www.mongodb.com/docs/) (via [`motor`](https://motor.readthedocs.io/))
* [Docker](https://docs.docker.com/)
* [Pytest](https://docs.pytest.org/)

## ✅ Features

* REST-style API built with FastAPI
* Async MongoDB access using motor, with basic connection handling
* Docker setup for local dev and deployment experiments
* Organized project structure with pyproject.toml and setuptools
* Simple OOP-style separation between routes, logic, and data access
* Unit and integration test scaffolding using pytest
* Focused more on learning and exploration than polish or completeness

## 🚀 Quickstart

### Local Dev Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install backend as editable package + dev deps
pip install .
pip install -r requirements-dev.txt

# Run tests
pytest
```

### 🐳 Docker (FastAPI in a container)

Make sure Docker is running, then:

```bash
cd backend
docker-compose up --build
```

This will:
* Build the FastAPI app
* Expose it on `localhost:8000`
* Run the app with `uvicorn` inside a container

## 🧪 Tests

Tests are split into:

```
tests/
├── unit/         # Logic-level tests
└── integration/  # Endpoint + DB interaction tests
```

Run all tests with:

```bash
pytest
```

## 🗃 MongoDB Notes

This app expects MongoDB connection info to be passed via a `.env` file, like:

```env
MONGODB_URL=mongodb+srv://...
MONGO_DB_NAME=todo_db
```

To interact with your DB directly, use [`mongosh`](https://www.mongodb.com/docs/mongodb-shell/) CLI (recommended for quick inspection or cleanup):

```bash
mongosh "your-mongodb-connection-string"
```

Then, to drop the database (be careful):

```js
use todo_db
db.dropDatabase()
```

## 📁 Project Structure

```
backend/
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── requirements-dev.txt
├── src/
│   └── backend/
│       ├── main.py
│       └── ... (routers, models, etc.)
└── tests/
    ├── unit/
    └── integration/
```

## 📚 Learning Achievements

This repo documents my hands-on exploration of modern backend development. Through building this project, I:

* **Discovered FastAPI**: Got introduced to FastAPI's intuitive async framework and automatic API documentation
* **Mastered MongoDB CLI**: Explored mongosh for direct database interaction, debugging, and management
* **Dockerized Production Apps**: Created a fully containerized, deployable backend
* **Applied Modern Python Standards**: Enforced PEP compliance, and effective Python best practices
* **Implemented Clean Architecture**: practiced separation of concerns for maintainable code

## License

MIT License