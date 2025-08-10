from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from app.database import Base

class Like(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    blog_id = Column(Integer, ForeignKey("blogs.id", ondelete="CASCADE"))

    __table_args__ = (UniqueConstraint("user_id", "blog_id", name="unique_like"),)
