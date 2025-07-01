import json
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

class TokenAuth(HTTPBearer):
    def __init__(self, auto_error: bool = True):

        # auto_error to be passed in, which determines whether FastAPI automatically throws on missing credentials.

        super(TokenAuth, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> str:
        try:
            credentials: HTTPAuthorizationCredentials = await super().__call__(request)
            token = credentials.credentials
            with open("users.json", "r") as f:
                users = json.load(f)
                
            # Scans all users to find a token match.

            for user in users:
                if user.get("token") == token:
                    return user["username"]
            raise HTTPException(status_code=401, detail="Invalid token")
        except Exception:
            raise HTTPException(status_code=401, detail="Invalid or missing token")
