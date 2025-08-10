from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comment import CommentCreate

def create_comment(db: Session, comment: CommentCreate, user_id: int):
    db_comment = Comment(**comment.model_dump(), user_id=user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments_by_blog(db: Session, blog_id: int):
    return db.query(Comment).filter(Comment.blog_id == blog_id).order_by(Comment.created_at.desc()).all()

def get_comment_by_id(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def delete_comment(db: Session, comment: Comment):
    db.delete(comment)
    db.commit()

def update_comment(db: Session, comment: Comment, content: str):
    comment.content = content
    db.commit()
    db.refresh(comment)
    return comment
