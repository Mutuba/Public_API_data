#!/bin/sh

wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku plugins:install @heroku-cli/plugin-container-registry
docker login --username _ --password=$HEROKU_AUTH_TOKEN registry.heroku.com
heroku container:push web --app $HEROKU_APP_NAME
heroku container:release web --app $HEROKU_APP_NAME