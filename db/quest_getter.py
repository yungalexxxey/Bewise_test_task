import requests
from .models import DbQuestion


def get_question(quest_num: int) -> list[DbQuestion]:
    if quest_num <= 0:
        return []
    api_answer = requests.get(f"https://jservice.io/api/random?count={quest_num}").json()
    list_of_questions = list()
    for i in api_answer:
        obj = DbQuestion(
            id=i['id'],
            question=i['question'],
            answer=i['answer'],
            created_at=i['created_at']
        )
        list_of_questions.append(obj)
    return list_of_questions

