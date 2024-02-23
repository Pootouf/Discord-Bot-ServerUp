FROM python:3.10.13

RUN pip install discord

RUN apt-get update -y && mkdir /app

COPY main.py /app
