FROM node:22-alpine3.19

WORKDIR /frontend

COPY ./frontend /frontend

RUN npm install

EXPOSE 8080

CMD [ "npm", "run", "serve" ]
