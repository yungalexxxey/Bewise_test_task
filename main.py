from fastapi import FastAPI, Depends
from schemas import IncomePost
from db.alchemy import get_db
from sqlalchemy.orm import Session
from db.db_questions import add_new_questions
from schemas import QuestionDisplay

app = FastAPI()


@app.post("/", response_model=QuestionDisplay)
async def test_task(post: IncomePost, db: Session = Depends(get_db)) -> dict:
    return add_new_questions(post.questions_num, db)
