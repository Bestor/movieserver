FROM python:3.6

ENV http_proxy=http://proxy.houston.hpecorp.net:8080 \
    https_proxy=http://proxy.houston.hpecorp.net:8080 \
    HTTP_PROXY=http://proxy.houston.hpecorp.net:8080 \
    HTTPS_PROXY=http://proxy.houston.hpecorp.net:8080 \
    no_proxy=hpe.com,hpecorp.net,localhost,127.0.0.1/8

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r Dockerfiles/django/requirements.txt
RUN chmod +x Dockerfiles/django/run.sh

WORKDIR /usr/src/app/movieserver/movieserver

CMD [ "./manage.py runserver 0.0.0.0:8000" ]
