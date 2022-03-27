from datetime import datetime
import email
from typing import Optional

from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: str


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


# Request Schemas
class Post(PostBase):
    published: Optional[bool] = True
    rating: Optional[int] = 1


class UpdatePost(PostBase):
    title: Optional[str]
    content: Optional[str]
    published: Optional[bool]
    rating: Optional[int]


class User(UserBase):
    password: str
    other_name: Optional[str]


# Response Schemas
class GetPostResponse(BaseModel):

    class Post2(PostBase):
        created_at: datetime

        class Config:
            orm_mode = True
    
    Post: Post2
    vote_count: int

    class Config:
        orm_mode = True

class CreatePostResponse(PostBase):
    created_at: datetime

    class Config:
        orm_mode = True


class CreateUserResponse(UserBase):
    created_at: datetime

    class Config:
        orm_mode = True


class GetUserResponse(UserBase):
    class Config:
        orm_mode = True


# Authentication
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenData(BaseModel):
    id: int


class TokenLoginReponse(BaseModel):
    access_token: str
    bearer: str
