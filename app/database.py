from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

# Update this if you're using a different database (e.g., PostgreSQL, MySQL)
DATABASE_URL = "sqlite:///./test.db"

# For SQLite, this connect_args line is required
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

