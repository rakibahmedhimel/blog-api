from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from typing import List
# User Phases:
class UserCreate(BaseModel):
    username : str
    email : EmailStr
    password : str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  # Changed from orm_mode to from_attributes



class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


# Token Phases:
class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    email : str | None = None


#public blog phase:
class PublicBlog(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class PublicUserProfile(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    blogs: List[PublicBlog]

    class Config:
        from_attributes = True



# Blog feed :
class BlogFeed(BaseModel):
    title: str
    content: str
    created_at: datetime
    author_name: str
    likes: int  | None = None# NEW

    class Config:
        orm_mode = True
