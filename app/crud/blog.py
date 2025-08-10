from sqlalchemy.orm import Session
from app.schemas.blog import BlogCreate, BlogUpdate
from app.models.blog import Blog
from app.models.user import User


def create_blog(db: Session, blog: BlogCreate, user_id: int):
    # Get the username from the User table using the user_id
    user_name = db.query(User.username).filter(User.id == user_id).first().username
    
    # Create the new blog with owner_id and owner_name
    db_blog = Blog(**blog.model_dump(), owner_id=user_id, owner_name=user_name)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog



def get_latest_blogs(db: Session, limit: int = 20):
    return (
        db.query(Blog)
        .order_by(Blog.created_at.desc())
        .limit(limit)
        .all()
    )


def get_user_blogs(db: Session, user_id: int):
    return db.query(Blog).filter(Blog.owner_id == user_id).all()


def get_blog_by_id(db: Session, blog_id: int):
    return db.query(Blog).filter(Blog.id == blog_id).first()


def update_blog(db: Session, blog_id: int, blog: BlogUpdate, user_id: int):
    db_blog = get_blog_by_id(db, blog_id)
    if db_blog and db_blog.owner_id == user_id:
        db_blog.title = blog.title
        db_blog.content = blog.content
        db.commit()
        db.refresh(db_blog)
        return db_blog
    return None


def delete_blog(db: Session, blog_id: int, user_id: int):
    db_blog = get_blog_by_id(db, blog_id)
    if db_blog and db_blog.owner_id == user_id:
        db.delete(db_blog)
        db.commit()
        return True
    return False
