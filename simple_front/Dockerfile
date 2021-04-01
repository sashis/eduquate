FROM node:15-alpine

WORKDIR /usr/app
COPY package.json yarn.lock ./
RUN yarn install
EXPOSE 3000
COPY . .
