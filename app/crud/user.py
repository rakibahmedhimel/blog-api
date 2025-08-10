from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

def create_user(db : Session, user : UserCreate):
    hashed_pwd = hash_password(user.password)

    new_user = User(username=user.username, email=user.email, hashed_password=hashed_pwd)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

def get_user_by_email(db : Session, email : str):
    return db.query(User).filter(User.email==email).first()


def get_user_by_name(db: Session, name: str = None):
    return db.query(User).filter(User.username==name).first()
    