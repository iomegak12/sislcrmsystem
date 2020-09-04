FROM python:latest

LABEL Environment Production
LABEL Author "Ramkumar JD"
LABEL Company SISL

COPY . /app

WORKDIR /app

RUN pip install -r requirements

