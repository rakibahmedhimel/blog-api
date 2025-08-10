from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.blog import BlogCreate, BlogOut, BlogUpdate
from app.models.user import User
from app.crud.blog import create_blog, get_latest_blogs, get_user_blogs, delete_blog, update_blog
from app.deps import get_current_user, get_db

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.post("/create_blog", response_model=BlogOut)
def create_new_blog(
    new_blog: BlogCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    created_blog = create_blog(db=db, blog=new_blog, user_id=current_user.id)
    
    return created_blog


@router.get("/feed", response_model=list[BlogOut])
def get_latest_feed(db: Session = Depends(get_db)):
    blogs = get_latest_blogs(db)
    return [BlogOut(**blog.__dict__) for blog in blogs]


@router.get("/me", response_model=list[BlogOut])
def get_my_blogs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    blogs = get_user_blogs(db, current_user.id)
    return [
        BlogOut(
            id=b.id,
            title=b.title,
            content=b.content,
            created_at=b.created_at,
            updated_at=b.updated_at,
            owner_name=current_user.username,
        )
        for b in blogs
    ]


@router.put("/{blog_id}", response_model=BlogOut)
def update_my_blog(
    blog_id: int,
    blog: BlogUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    updated = update_blog(db, blog_id, blog, current_user.id)
    if not updated:
        raise HTTPException(status_code=403, detail="Not authorized or blog not found")
    return BlogOut(
        id=updated.id,
        title=updated.title,
        content=updated.content,
        created_at=updated.created_at,
        updated_at=updated.updated_at,
        owner_name=updated.owner.username 
    )


@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_my_blog(
    blog_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    deleted = delete_blog(db, blog_id, current_user.id)
    if not deleted:
        raise HTTPException(status_code=403, detail="Not authorized or blog not found")
    return {"message":"Successfully Deleted"}
