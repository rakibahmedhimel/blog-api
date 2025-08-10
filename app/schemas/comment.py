from pydantic import BaseModel
from datetime import datetime

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    blog_id: int  # required when creating

class CommentOut(CommentBase):
    id: int
    created_at: datetime
    user_id: int
    blog_id: int

    class Config:
        orm_mode = True
