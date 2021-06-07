#!/bin/bash
set -e

sudo docker login --username $HEROKU_USERNAME --password $HEROKU_AUTH_TOKEN registry.heroku.com

# Push Dockerfile to DockerHub
docker-compose build --pull
docker-compose push

sudo docker tag public_data_api_app:latest registry.heroku.com/publicapidataapp/web

if [ $TRAVIS_BRANCH == "master" ] && [ $TRAVIS_PULL_REQUEST == "false" ]; then sudo docker push registry.heroku.com/publicapidataapp/web; fi

chmod +x heroku-container-release.sh
sudo chown $USER:docker ~/.docker
sudo chown $USER:docker ~/.docker/config.json
sudo chmod g+rw ~/.docker/config.json

./heroku-container-release.sh