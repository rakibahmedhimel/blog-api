from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.deps import get_db, get_current_user
from app.schemas.user import PublicUserProfile, UserResponse, UserUpdate
from app.models.user import User
from app.core.security import hash_password
from app.crud.user import get_user_by_name

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/public", response_model=PublicUserProfile)
def search_profile_by_name(name: str = None, db: Session = Depends(get_db)):
    if not name:
        raise HTTPException(status_code=400, detail="Provide valid username.")

    user = get_user_by_name(db, name)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return user


@router.put("/update", response_model=UserResponse)
def update_your_information(
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if user_update.username:
        current_user.username = user_update.username

    if user_update.email:
        # Ensure email isn't taken
        existing = db.query(User).filter(User.email == user_update.email).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already taken")
        current_user.email = user_update.email

    if user_update.password:
        current_user.hashed_password = hash_password(user_update.password)

    db.commit()
    db.refresh(current_user)
    return current_user


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def delete_your_account(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db.delete(current_user)
    db.commit()
    return {"message": "Account deleted successfully"}
