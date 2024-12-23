from sqlalchemy.orm import Session
from app.db.models import Post, Comment, Like

def fetch_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def create_new_post(db: Session, content: str, user_id: int):
    new_post = Post(content=content, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def create_new_comment(db: Session, post_id: int, content: str, user_id: int):
    comment = Comment(content=content, post_id=post_id, user_id=user_id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def like_post(db: Session, post_id: int, user_id: int):
    new_like = Like(post_id=post_id, user_id=user_id)
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return new_like
