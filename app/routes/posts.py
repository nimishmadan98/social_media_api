from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schema.post_schemas import PostCreate, PostOut
from app.schema.comment_schemas import CommentCreate, CommentOut
from app.schema.like_schemas import LikeCreate, LikeOut
from app.services.post_services import (
    create_post,
    get_posts,
    add_comment,
    like_post,
)
from app.core.auth import get_current_user
from app.db.database import get_db
from app.db.models import User
from app.utils.security import verify_token

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", response_model=PostOut)
def create_post_route(post: PostCreate, db: Session = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    db_post = create_post(db, post, current_user.id)

    return PostOut.from_orm(db_post)

@router.get("/", response_model=List[PostOut])
def get_posts_route(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_posts(db, current_user)

@router.post("/{post_id}/comments", response_model=CommentOut)
def add_comment_route(post_id: int, comment: CommentCreate, db: Session = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    return add_comment(db, post_id, comment, current_user.id)

@router.post("/{post_id}/likes", response_model=LikeOut)
def like_post_route(post_id: int, db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    return like_post(db, post_id, current_user.id)
