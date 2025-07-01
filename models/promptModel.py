from pydantic import BaseModel

#  create  a promptSchema

class PromptRequest(BaseModel):
    prompt: str
