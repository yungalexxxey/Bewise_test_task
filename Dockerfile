FROM python:3.9

WORKDIR .

COPY ./db ./db
COPY ./req.txt ./req.txt
COPY ./main.py ./main.py

COPY ./schemas.py ./schemas.py

RUN pip install --no-cache-dir --upgrade -r ./req.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]