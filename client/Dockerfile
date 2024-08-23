FROM node:20

RUN mkdir app 
WORKDIR /app 

COPY package.json .
COPY . .

RUN npm install 
