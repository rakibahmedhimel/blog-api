from pydantic import BaseModel

class LikeRequest(BaseModel):
    blog_id: int
