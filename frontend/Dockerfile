FROM node as builder

WORKDIR /app

COPY ./package.json ./package-lock.json .
RUN npm install

ARG REACT_APP_API_URL

COPY . .
RUN npm run build


FROM nginx

COPY --from=builder /app/build /usr/share/nginx/html
