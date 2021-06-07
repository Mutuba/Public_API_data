#!/bin/sh
set -e
# sudo docker login --username _ --password=$DOCKER_AUTH_TOKEN
echo  docker login --username _ --password=$DOCKER_AUTH_TOKEN
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi

docker build -f Dockerfile -t $TRAVIS_REPO_SLUG:$TAG .
docker tag $TRAVIS_REPO_SLUG $DOCKER_REPO
docker push $DOCKER_REPO