#!/bin/sh

# . ./env_secrets_expand.sh

# echo "Here is the secret greeting: for $DB_URL"
# echo "${DB_USER}-->${DB_URL}"

echo $(cat "/run/secrets/flask-swarn-db_password")
echo $(cat "/run/secrets/flask-swarn-db_url")
echo $(cat "/run/secrets/flask-swarn-db_user")
