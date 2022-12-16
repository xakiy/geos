FROM python:alpine3.9

RUN apk update; apk add --no-cache sqlite

WORKDIR /app

COPY *.py /app

COPY FastAPI/* /app

RUN chmod 755 rebuild-db.py; ./rebuild-db.py

RUN pip install -U pip; pip install -r requirements.txt

CMD ["gunicorn", "asgi:app", "-c", "gunicorn.conf.py"]
