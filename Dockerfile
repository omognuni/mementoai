FROM python:3.9

WORKDIR /app

COPY . .

ENV PYTHONPATH="/app"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /
