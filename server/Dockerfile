FROM python:3.11.9-alpine3.19 

RUN mkdir app
WORKDIR /app

COPY . .

RUN apk update && apk add --no-cache bash
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt
