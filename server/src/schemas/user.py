from typing import Optional
import datetime
from  pydantic import BaseModel, EmailStr 

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserAuth(BaseModel):
    email: EmailStr
    password: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True
