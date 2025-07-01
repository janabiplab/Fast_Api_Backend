from fastapi import APIRouter, Depends, HTTPException
from auth import TokenAuth
import json
import os

router = APIRouter()

# For  token validator class

auth = TokenAuth()  

# router of the history

@router.get("/history")
async def get_history(username: str = Depends(auth)):
    try:

        # if history.json is not present then create it with empty []
        if not os.path.exists("history.json"):
            return {"history": []}  # No history file yet
        
        # Parses it into a Python dictionary (history_data)
        
        with open("history.json", "r") as f:
            history_data = json.load(f)
        
        # Tries to get the history for the specific username.Returns an empty list if the user has no history.

        user_history = history_data.get(username, [])

        return {"username": username, "history": user_history}
    

    # Catches any unexpected error and responds
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading history: {str(e)}")
