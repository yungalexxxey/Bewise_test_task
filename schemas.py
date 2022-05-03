import datetime

from pydantic import BaseModel


class IncomePost(BaseModel):
    questions_num: int


class QuestionDisplay(BaseModel):
    id: int = None
    answer: str = None
    question: str = None
    created_at: datetime.datetime = None

    class Config:
        orm_mode = True
