FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8

RUN apk update; apk add --no-cache git openssl sqlite

WORKDIR /tmp

RUN git clone -b 'FalconVersion1.0' --single-branch https://github.com/xakiy/geos eggs; rm -fr eggs/.git

RUN cp eggs/* /app; rm -fr eggs

WORKDIR /app

RUN pip install -U pip; pip install -r requirements.txt

CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:8000"]
