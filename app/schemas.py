from typing import Optional
from datetime import datetime
from app.database import Base
from pydantic import BaseModel, EmailStr, conint



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True



class PostCreate(PostBase):
    pass



class UserCreate(BaseModel):
    email: EmailStr
    password: str



class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True



class UserLogin(BaseModel):
    email: EmailStr
    password: str



class PostResponse(PostBase):
    id: int
    owner: UserOut
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True




class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True




class Token(BaseModel):
    token_type: str
    access_token: str




class TokenData(BaseModel):
    id: Optional[str] = None



class Vote(BaseModel):
    dir: conint(le=1)
    post_id: int