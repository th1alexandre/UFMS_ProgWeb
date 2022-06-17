FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate

COPY . /app/
