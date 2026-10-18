# Books-Api
# 📚 Books API

A simple REST API for managing books, built with **Python, FastAPI, and SQLite**.
This project will also be useful for beginners who want to learn about databases and APIs.

This project was created as a hands-on learning experience to practice backend development, working with databases, handling HTTP requests, and testing API endpoints.

## 🚀 Features

- Retrieve all books stored in the database.
- Add new books using POST requests.
- Store book data in an SQLite database.
- Validate incoming requests.
- Prevent duplicate book IDs and return an HTTP `409 Conflict` response.
- Test API endpoints using Postman.
- Explore automatically generated API documentation with Swagger UI.

## 🛠️ Tech Stack

- **Python 3**
- **FastAPI** — REST API framework.
- **SQLite** — database for persistent data storage.
- **Uvicorn** — ASGI server.
- **Postman** — API testing tool.

## 📂 Project Structure

```text
Books_API/
├── requirements.txt
├── database.py
└── main.py
```

- `main.py` — API endpoints and application logic.
- `database.py` — database connection and database operations.

*Note: The exact role of `books.py` depends on the final project implementation.*

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone <https://github.com/H1yro/Books-Api.git>
cd Books_API
```

**2. Install dependencies**

```bash
python -m pip install fastapi uvicorn
```

**3. Run the application**

```bash
python -m uvicorn main:app --reload
```

**4. Open the API documentation**

Visit:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Root endpoint |
| GET | `/books` | Retrieve all books |
| POST | `/books` | Add a new book |
| GET | `/hello` | Simple greeting endpoint |

## 🧪 Testing

The API was tested using Postman.

The tests included retrieving books, adding new books, and checking duplicate IDs. Sending the same book ID twice results in a `409 Conflict` response.
