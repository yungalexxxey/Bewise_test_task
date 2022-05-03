import datetime

from pydantic import BaseModel


class IncomePost(BaseModel):
    questions_num: int


class QuestionDisplay(BaseModel):
    id: int = 0
    answer: str = ""
    question: str = ""
    created_at: datetime.datetime = ""

    class Config:
        orm_mode = True
