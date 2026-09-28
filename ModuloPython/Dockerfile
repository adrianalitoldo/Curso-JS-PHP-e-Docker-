FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir "Flask>=3,<4" requests

COPY . .
EXPOSE 5000