from fastapi import APIRouter, HTTPException
from models.userModel import SignupRequest
import json
import uuid
import os

router = APIRouter()

@router.post("/signup")
def signup(user: SignupRequest):
    try:
        # Creates an empty users.json file if it's missing, initializing it with an empty list.

        if not os.path.exists("users.json"):
            with open("users.json", "w") as f:
                json.dump([], f)

        # Loads existing user data into a Python list.

        with open("users.json", "r") as f:
            users = json.load(f)

        for u in users:
            # Prevents duplicate signup using the same username by throwing a 400 error.

            if u["username"] == user.username:
                raise HTTPException(status_code=400, detail="User already exists with this username")
            
            # Prevents duplicate signup using the same email by throwing a 400 error.

            if u["email"] == user.email:
                raise HTTPException(status_code=400, detail="User already exists with this email")

        # create a token
        
        token = str(uuid.uuid4())

        # Creates a new user record with a unique token.

        users.append({
            "username": user.username,
            "email":user.email,
            "password": user.password,
            "token": token
        })

        with open("users.json", "w") as f:
            json.dump(users, f, indent=2)
        
        # Confirms registration and sends the token for future authentication.

       
        return {"message": "Signup successful", "token": token}
    
    # Catches any other errors (like file corruption) and returns a 500 error.
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
