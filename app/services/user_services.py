from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models import User
from app.utils.security import hash_password
from app.utils.token import create_verification_token
from app.utils.email import send_verification_email

def register_user(db: Session, user_data):
    existing_user = db.query(User).filter((User.name == user_data.name) | (User.email == user_data.email)).first()
    if existing_user:
        raise ValueError("User with this name or email already exists")

    hashed_password = hash_password(user_data.password)
    new_user = User(name=user_data.name, email=user_data.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    verification_token = create_verification_token(new_user.email)

    # Send verification email
    send_verification_email(new_user.email, verification_token)

    return {"message": "User registered successfully", "username": new_user.name}

def verify_email_address(db: Session, email: str):
    db_user = db.query(User).filter(User.email == email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")

    # Mark the user as verified
    db_user.is_verified = True
    db.commit()

    return {"message": "Email verified successfully!"}
