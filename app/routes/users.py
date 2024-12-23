from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.user_services import register_user, verify_email_address
from app.db.database import get_db
from app.schema.user_schemas import *
from app.utils.security import verify_token

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def register_user_route(user: UserSchema, db: Session = Depends(get_db)):
    return register_user(db, user)

@router.get("/verify/{token}")
def verify_email(token: str, db: Session = Depends(get_db)):
    # Verify the token
    payload = verify_token(token)

    if "error" in payload:
        raise HTTPException(status_code=400, detail=payload["error"])

    email = payload["sub"]

    return verify_email_address(db, email)