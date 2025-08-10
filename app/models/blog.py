from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    owner_name = Column(String, nullable=False)  # Keep owner_name as a column

    # Establish the relationship
    owner = relationship("User", back_populates="blogs")
    likes = relationship("Like", backref="blog", cascade="all, delete")
    comments = relationship("Comment", back_populates="blog", cascade="all, delete")
