from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://test_user:pswrd@localhost:5450/test_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base = declarative_base()


metadata = Base.metadata
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
