FROM python:3.8 AS builder

WORKDIR /app
COPY /code .

CMD ["python","main.py"]