from fastapi import APIRouter, HTTPException
from models.userModel import LoginRequest
import json

router = APIRouter()

@router.post("/login")
def login(user: LoginRequest):
    try:
        # Parses it into a Python dictionary (history_data).

        with open("users.json", "r") as f:
            users = json.load(f)
        
        # Compares both username and password from the request with stored data.

        for u in users:
            if u["username"] == user.username and u["password"] == user.password:
                return {"token": u["token"]}
        
        # f no match is found, throws a 401 error indicating failed login.

        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Handles other errors (e.g., file not found, malformed JSON) and returns a 500 error. 

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
