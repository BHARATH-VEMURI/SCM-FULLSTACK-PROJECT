from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)
    # confirm_password: str = Field(..., min_length=8, max_length=128)

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)

class UserOut(BaseModel):
    id: Optional[str]
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr 
    role: str = Field(..., min_length=3, max_length=20)
    created_at: datetime

class UserInDB(UserOut):
    hashed_password: str
    