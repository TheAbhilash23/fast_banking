FROM python:3.12-slim AS build
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y nano gettext libpq-dev

WORKDIR /application

ADD ./requirements.txt ../application

RUN pip install -r requirements.txt

ADD ./src/core /core

RUN pip install /core
