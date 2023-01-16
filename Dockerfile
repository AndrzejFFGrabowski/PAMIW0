FROM python:alpine
FROM ubuntu:trusty
WORKDIR /var/www
ENV FLASK_APP app/app.py
ENV FLASK_DEBUG false
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5050
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN sudo apt-get -y update
RUN sudo apt-get -y upgrade
RUN sudo apt-get install -y sqlite3 libsqlite3-dev
RUN mkdir /db
RUN /usr/bin/sqlite3 /db/pythonDB.db
CMD /bin/bash
COPY app app
CMD ["flask", "run"]
