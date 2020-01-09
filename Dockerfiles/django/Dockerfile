FROM python:3.6

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r Dockerfiles/django/requirements.txt
RUN chmod +x Dockerfiles/django/run.sh

WORKDIR /usr/src/app/movieserver/movieserver

CMD [ "./run.sh" ]
