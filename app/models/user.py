from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)  # ✅ required
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

