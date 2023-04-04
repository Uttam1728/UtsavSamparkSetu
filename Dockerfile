FROM python:3.7.11-bullseye as utsav_setu_builder

ENV DEPLOYMENT=build
ENV PYTHONUNBUFFERED=1

WORKDIR /lokal/services/utsav_sampark_setu

COPY ./requirements.txt /lokal/services/utsav_sampark_setu/requirements.txt
RUN apt update && apt install -y gettext supervisor \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

COPY . /lokal/services/utsav_sampark_setu
COPY supervisord.conf /etc/supervisord.conf

RUN python manage.py collectstatic --no-input \
    && rm -rf .??*

ENV TZ=IST
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime

EXPOSE 8000

CMD ["supervisord"]

#--env DEPLYOMENT=aws_dev|aws_staging|aws_prod|local_dev
#--env ENV_STARTCMD=
#    "gunicorn --preload --bind 0.0.0.0:8000 --workers 2 --access-logfile - config.wsgi" |
#    "celery worker --app lokalads --concurrency=15 --hostname w1 --loglevel=INFO --queues celery --pool=gevent" |
#    "celery beat --app lokalads --scheduler django_celery_beat.schedulers:DatabaseScheduler' --loglevel=INFO
