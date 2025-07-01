from fastapi import APIRouter, Depends, HTTPException
from auth import TokenAuth
from models.promptModel import PromptRequest
from services.replicate_api import ask_replicate
from starlette.concurrency import run_in_threadpool
import json
from datetime import datetime
import os

router = APIRouter()
auth = TokenAuth()  # This checks the Bearer token and returns the username

# Authenticates the request and injects the username via Depends(auth).

@router.post("/prompt")
async def submit_prompt(prompt: PromptRequest, username: str = Depends(auth)):
    try:
        
        # Sends the prompt to the model using a background thread (avoiding blocking).

        formatted_text= await run_in_threadpool(ask_replicate, prompt.prompt)
        # formatted_text = response.replace("\n", "")

        # If history.json is missing, creates it with an empty dict.
        
        if not os.path.exists("history.json"):
            with open("history.json", "w") as f:
                json.dump({}, f)

        # Handles possible corruption in history.json gracefully.
        # Ensures the file is reset if it contains invalid JSON.

        try:
            with open("history.json", "r") as f:
                history = json.load(f)
        except json.JSONDecodeError:
            history = {}
            with open("history.json", "w") as f:
                json.dump(history, f, indent=2)


        # If the user has no previous prompts, initialize an empty list
        if username not in history:
            history[username] = []

        # Add the new prompt/response to history
        history[username].append({
            "timestamp": datetime.utcnow().isoformat(),
            "prompt": prompt.prompt,
            "response": formatted_text
        })

        # Save back to the file
        with open("history.json", "w") as f:
            json.dump(history, f, indent=2)

        return {"response": formatted_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing prompt: {str(e)}")
