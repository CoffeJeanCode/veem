from  pydantic import BaseModel, EmailStr 

class Token(BaseModel):
  toke_type: str
  access_token: str