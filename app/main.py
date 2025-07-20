from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models import user
from app.schemas.user import UserCreate, UserRead
from app.crud.user import create_user
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import authenticate_user, create_access_token

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

