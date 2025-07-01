from pydantic import BaseModel

 
# create a userSchema for signup with username,email,password

class SignupRequest(BaseModel):
    username: str
    email:str
    password: str


# create a schema of the user for login with email and password

class LoginRequest(BaseModel):
    username:str
    password:str
