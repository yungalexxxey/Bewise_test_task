from sqlalchemy import Column, Integer, String, TIMESTAMP
from .alchemy import Base


class DbQuestion(Base):
    __tablename__ = 'main_table'
    id = Column(Integer, primary_key=True, unique=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(TIMESTAMP)
