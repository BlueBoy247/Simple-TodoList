FROM node:20.18.0

COPY package*.json ./
RUN npm install
COPY . .
RUN ["cp", ".env.template", ".env"]
EXPOSE 8080
CMD ["npm", "run", "serve"]