
FROM python:3.7-alpine


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV C_FORCE_ROOT true
ENV PYTHONUNBUFFERED 1

# Adding mandatory packages to docker
RUN apk update && apk add --no-cache \
    postgresql \
    zlib \
    jpeg 

# Installing temporary packages required for installing requirements.pip 
RUN apk add --no-cache --virtual build-deps \
    gcc \  
    python3-dev \ 
    musl-dev \
    postgresql-dev\
    zlib-dev \
    jpeg-dev 


WORKDIR /usr/src/app
# copy project
COPY . ./usr/src/app

RUN pip install --no-cache-dir -r ./usr/src/app/requirements.txt


# removing temporary packages from docker and removing cache 
RUN apk del build-deps && \
    find -type d -name __pycache__ -prune -exec rm -rf {} \; && \
    rm -rf ~/.cache/pip

