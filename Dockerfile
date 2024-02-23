FROM python:3.9-alpine

RUN pip install discord

RUN mkdir /app

COPY main.py /app
