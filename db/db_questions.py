from sqlalchemy.orm import Session
from .models import DbQuestion
from .quest_getter import get_question


def existence_check(quest: DbQuestion, db: Session) -> bool:
    if db.query(DbQuestion).filter(DbQuestion.id == quest.id).first():
        return True
    return False


def add_to_db(quest: DbQuestion, db: Session) -> None:
    db.add(quest)
    db.commit()


def add_new_questions(question_num: int, db: Session) -> DbQuestion:
    last_quest: DbQuestion = db.query(DbQuestion).all()
    try:
        last_quest = last_quest[-1]
    except IndexError:
        pass
    new_quests = get_question(question_num)
    for i in new_quests:
        if not existence_check(i, db):
            add_to_db(i, db)
            continue
        while True:
            another_quest = get_question(1)[0]
            if not existence_check(another_quest, db):
                add_to_db(another_quest, db)
                break
    return last_quest
