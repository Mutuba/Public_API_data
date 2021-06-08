
FROM python:3


ENV PATH="/scripts:${PATH}"

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

RUN pip install -r requirements.txt

# collect static files
RUN python manage.py collectstatic --noinput

CMD gunicorn public_api_data_app.wsgi:application --bind 0.0.0.0:$PORT

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
