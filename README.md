# Bewise_test_task

Для запуска тестового задания прежде всего потребуется его скопировать:
```
git clone https://github.com/yungalexxxey/Bewise_test_task.git
```
После этого необходимо перейти в папку проекта:
```
cd Bewise_test_task
```
Внутри этого проекта будет несколько папок и файлов,а именно:
- Папка db, в которой находятся модули, ответственные за взаимодействие с базой данных
- Папка postgresql_data, которая является хранилещем данных. В папке также присутствует файл, который инициализирует БД.
- Файл docker-compose.yml, с помощью которого и будет собираться и запускаться образ с PostgreSQL и FastAPI веб сервисом.
- Файл main.py
- Файл schemas.py, в котором находятся необходимые схемы для FastAPI

В файле docker-compose.yml находятся необходимые настройки БД, которые можно изменить:
- POSTGRES_DB: "НАЗВАНИЕ_БД"
- POSTGRES_USER: "ИМЯ_ПОЛЬЗОВАТЕЛЯ"
- POSTGRES_PASSWORD: "ПАРОЛЬ"
- ports: "ПОРТ:5432" (ПОРТ используется для подключения извне. По умолчанию 5450)

Однако в случае изменения этого файла, изменить потребуется и `alchemy.py`, а именно:
`
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://ИМЯ_ПОЛЬЗОВАТЕЛЯ:ПАРОЛЬ@172.16.1.4:5432/НАЗВАНИЕ_БД"
`

После проделанных выше действий можно запускать docker-compose:
```
sudo docker-compose up -d
```

Для остановки образа нужно будет использовать следующую команду:
```
docker-compose stop
```

После этой команды будет запущена БД и веб сервис. Для подключения к БД извне нужно использовать следующую команду:
```
psql "host=localhost \                                                                                                                                ✔ 
port=ПОРТ \
dbname=test_db \
user=test_user"
(ПОРТ по умолчанию 5450)
```

Теперь можно в браузере открывать `http://0.0.0.0:8000/docs`.
Пример пользования через swagger:
```
{
  "questions_num": 15 
}
```
Пример POST запроса к API с помощью curl:

```
curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 15 }' http://0.0.0.0:8000/   
```
Если вдруг на вход придёт число, которое меньше нуля (или равно нулю), то ответом будет последний добавленный вопрос.


