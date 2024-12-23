from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes import users, posts, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def home():
    return {"message": "Welcome to the Social Media API!"}
