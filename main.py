# Imports--------------------------
from fastapi import FastAPI
from pydantic import BaseModel
# ---------------------------------

app = FastAPI(title="Learning App - User Service")
"""
### Initial pipeline, v1:
###     .\.venv\Scripts\Activate.ps1
###     pip install -r requirements.txt
###     uvicorn main:app --reload --port 8000
###     Key stuff on: http://localhost:8000/docs
"""

class User(BaseModel):
    id: int
    name: str
    interests: list[str]
    learning_goals: list[str]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/users/me", response_model=User)
def get_current_user():
    return User(
        id=1,
        name="Test User",
        interests=["Python", "Cloud Computing"],
        learning_goals=["Beer"]
    )
