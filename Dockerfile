FROM python:3.10.13

RUN pip install discord

RUN mkdir /app

COPY main.py /app
