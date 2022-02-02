# Docker Labs

(https://labs.play-with-docker.com/)[https://labs.play-with-docker.com/]

## Copiar dentro do console do labs

```shell
Ctrl + Ins
```

# Iniciando o swarm

```shell
docker swarm init --advertise-addr <IP_DOCKER_LAB>
```

# Adicionar novo nó

```shell
docker swarm join-token worker
```

Será exibido

```shell
docker swarm join --token SWMTKN-1-43io967kl1889dytd52p3ieflgoym2qgvod5humyy4ctvutjsh-6rsdkpzxj09ui5ni21ww9hw7y <IP_DOCKER_LAB>:2377
```

# Exibir os nós

```shell
docker node ls
```

# Criando serviço

```shell
docker service create --name flask-swarm-python -p 5000 danielso2007/flask-swarm-projeto:1.0.0
```

# Listando serviços

```shell
docker service ls
```

# Com réplicas

```shell
docker service create --name flask-swarm-python --replicas 3 -p 5000 danielso2007/flask-swarm-projeto:1.0.0
```

# Criando compose

```shell
vim docker-compose.yml
```

Os secrets são criados abaixo.


```yaml
version: '3.9'

services:
    flask-swarm-python:
        image: danielso2007/flask-swarm-projeto:3.0.0
        deploy:
            replicas: 3
        ports:
            - 5000
        environment:
            DB_URL: run/secrets/flask-swarn-db_url
            DB_USER: run/secrets/flask-swarn-db_user
            DB_PASSWORD: run/secrets/flask-swarn-db_password
        secrets:
            - flask-swarn-db_url
            - flask-swarn-db_user
            - flask-swarn-db_password
secrets:
    flask-swarn-db_url:
        external: true
    flask-swarn-db_user:
        external: true
    flask-swarn-db_password:
        external: true
```

```shell
docker pull danielso2007/flask-swarm-projeto:3.0.0

docker stack deploy -c docker-compose.yml flask-swarm-python
```

# Scale

Primeiro verificar o nome do serviço.

```shell
docker service ls
docker service scale flask-swarm-python_flask-swarm-python=3
```
# Atualizando imagem

```shell
docker service ls
docker service update --image danielso2007/flask-swarm-projeto:2.0.0 flask-swarm-python_flask-swarm-python
```

# Listando Secret

```shell
docker secret ls
```

```shell
printf "jdbc:mysql://teste:3306" | docker secret create flask-swarn-db_url -
printf "root" | docker secret create flask-swarn-db_user -
printf "root" | docker secret create flask-swarn-db_password -
```

```shell
docker service create --name flask-swarm-python --replicas 3 -p 5000 --secret flask-swarn-db_url --secret flask-swarn-db_user --secret flask-swarn-db_password danielso2007/flask-swarm-projeto:1.0.0
```

```shell
docker ps --filter name=flask-swarm-python -q
docker container exec $(docker ps --filter name=flask-swarm-python -q) ls -l /run/secrets
docker container exec $(docker ps --filter name=flask-swarm-python -q) cat /run/secrets/flask-swarn-db_url
docker container exec $(docker ps --filter name=flask-swarm-python -q) cat /run/secrets/flask-swarn-db_user
docker container exec $(docker ps --filter name=flask-swarm-python -q) cat /run/secrets/flask-swarn-db_password
```

### Analisando o serviço

```shell
docker secret inspect flask-swarn-db_password
```

# Entrando no docker
```shell
docker exec -it $(docker ps --filter name=flask-swarm-python -q) /bin/bash
```
