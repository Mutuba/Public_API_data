FROM python:3

WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app

RUN pip install -r requirements.txt

ADD . /usr/src/app

# collect static files
RUN python manage.py collectstatic --noinput

CMD gunicorn public_api_data_app.wsgi:application --bind 0.0.0.0:$PORT