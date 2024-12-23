from sqlalchemy.orm import Session
from app.db.models import Post, Like, Comment, User
from app.schema.post_schemas import PostCreate
from app.schema.comment_schemas import CommentCreate
from fastapi import HTTPException


def create_post(db: Session, post_data: PostCreate, user_id: int):
    db_post = Post(content=post_data.content, user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: Session, current_user: User):
    posts = db.query(Post).filter(Post.user_id == current_user.id).all()
    for post in posts:
        post.likes_count = len(post.likes)
        post.comments_count = len(post.comments)
    return posts


def add_comment(db: Session, post_id: int, comment_data: CommentCreate, user_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    db_comment = Comment(content=comment_data.content, post_id=post_id, user_id=user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def like_post(db: Session, post_id: int, user_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    existing_like = db.query(Like).filter(Like.post_id == post_id, Like.user_id == user_id).first()
    if existing_like:
        raise HTTPException(status_code=400, detail="User already liked this post")

    db_like = Like(post_id=post_id, user_id=user_id)
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like
