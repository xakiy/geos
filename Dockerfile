FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8

RUN apk update; apk add --no-cache sqlite

COPY . /app

WORKDIR /app

RUN pip install -U pip; pip install -r requirements.txt

CMD ["uvicorn", "asgi:app", "--host", "0.0.0.0", "--port", "8000"]
