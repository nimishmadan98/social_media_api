from sqlalchemy.orm import Session
from app.db.models import User

def create_user(db: Session, name: str, email: str, hashed_password: str) -> User:
    """
    Create a new user in the database.
    """
    new_user = User(name=name, email=email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_id(db: Session, user_id: int) -> User:
    """
    Fetch a user by their ID.
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User:
    ""
