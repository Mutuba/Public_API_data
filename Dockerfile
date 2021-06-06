
FROM python:3

# RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apk del .tmp
# copy entrypoint.sh
COPY entrypoint.sh /usr/src/app

RUN chmod +x /usr/src/app/entrypoint.sh

ADD . /usr/src/app

# collect static files
RUN python manage.py collectstatic --noinput

CMD gunicorn public_api_data_app.wsgi:application --bind 0.0.0.0:$PORT

# run entrypoint.sh
# ENTRYPOINT ["entrypoint.sh"]