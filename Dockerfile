# Використовуємо офіційний образ Python 3.9 як базу
FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

