from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./app.db"

class Base(DeclarativeBase):
    pass



engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

Base.metadata.create_all(
    bind=engine
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()