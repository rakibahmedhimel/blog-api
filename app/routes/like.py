from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.like import LikeRequest
from app.crud.like import like_blog, unlike_blog
from app.deps import get_db, get_current_user

router = APIRouter(prefix="/likes", tags=["Likes"])

@router.post("/")
def like_a_blog(payload: LikeRequest, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return like_blog(db, user.id, payload.blog_id)

@router.delete("/")
def unlike_a_blog(payload: LikeRequest, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return unlike_blog(db, user.id, payload.blog_id)
