from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import UserCreate, UserResponse, Token
from app.models.user import User
from app.crud.user import create_user, get_user_by_email
from app.core.security import verify_password, create_access_token
from app.deps import get_db, get_current_user


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = create_user(db=db, user=user)
    return new_user

@router.post("/login", response_model=Token)
def login(form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    user = get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(data = { "sub" : user.email })
    return {"access_token" : access_token, "token_type" : "bearer"}

@router.get("/me", response_model=UserResponse)
def read_active_user(current_user: User = Depends(get_current_user)):
    # Ensure the profile picture is returned as a URL
    return current_user
