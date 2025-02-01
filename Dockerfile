FROM python:3.12.0-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY . /app

RUN pip install -U pip setuptools && pip install poetry

RUN poetry install --no-interaction --no-ansi