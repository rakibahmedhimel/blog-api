from sqlalchemy.orm import Session
from app.models.like import Like

def like_blog(db: Session, user_id: int, blog_id: int):
    like = db.query(Like).filter_by(user_id=user_id, blog_id=blog_id).first()
    if not like:
        new_like = Like(user_id=user_id, blog_id=blog_id)
        db.add(new_like)
        db.commit()
        db.refresh(new_like)
    return {"message": "Liked"}

def unlike_blog(db: Session, user_id: int, blog_id: int):
    like = db.query(Like).filter_by(user_id=user_id, blog_id=blog_id).first()
    if like:
        db.delete(like)
        db.commit()
    return {"message": "Unliked"}
