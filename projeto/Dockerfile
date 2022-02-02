FROM python:3.11.0a4-slim-buster

#ENV DB_URL_FILE=flask-swarn-db_url
#ENV DB_USER_FILE=flask-swarn-db_user
#ENV DB_PASSWORD_FILE=flask-swarn-db_password

RUN apt-get update -y && apt-get install -y python-pip python-dev

# WORKDIR /app

RUN pip install Flask

# RUN mkdir -p /run/secrets

# COPY flask-swarn-db_password /run/secrets/flask-swarn-db_password
# COPY flask-swarn-db_url /run/secrets/flask-swarn-db_url
# COPY flask-swarn-db_user /run/secrets/flask-swarn-db_user

COPY . .

# COPY env_secrets_expand.sh /env_secrets_expand.sh
COPY my.sh /my.sh

EXPOSE 5000

# ENTRYPOINT ["./my.sh" ]

CMD [ "python", "./app.py"]