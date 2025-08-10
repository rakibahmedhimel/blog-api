from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db
from app.schemas import comment as schema
from app.crud import comment as crud
from app.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/comments", tags=["Comments"])

@router.post("/", response_model=schema.CommentOut)
def add_comment(comment: schema.CommentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.create_comment(db, comment, current_user.id)

@router.get("/blog/{blog_id}", response_model=list[schema.CommentOut])
def get_blog_comments(blog_id: int, db: Session = Depends(get_db)):
    return crud.get_comments_by_blog(db, blog_id)

@router.delete("/{comment_id}")
def delete_my_comment(comment_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    comment = crud.get_comment_by_id(db, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    # Comment owner or blog author can delete
    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this comment")

    crud.delete_comment(db, comment)
    return {"detail": "Comment deleted"}


@router.put("/{comment_id}", response_model=schema.CommentOut)
def update_my_comment(comment_id: int, updated: schema.CommentBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    comment = crud.get_comment_by_id(db, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to edit this comment")

    return crud.update_comment(db, comment, updated.content)
