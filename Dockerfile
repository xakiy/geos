FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8

MAINTAINER Ahamd Ghulam Zakiy <ghulam.zakiy@gmail.com>

RUN apk update; apk add --no-cache sqlite

COPY . /app

WORKDIR /app

RUN pip install -U pip; pip install -r requirements.txt

CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:8080", "--workers", "2", "--log-file", "-"]
