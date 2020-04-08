FROM python:3.8-slim-buster

RUN apt-get update && apt-get install --yes libmagic-dev

RUN mkdir -p /usr/src/vote21
WORKDIR /usr/src/vote21
ADD requirements/base.txt ./requirements.txt
RUN  python -m pip install -U pip && pip install -r requirements.txt
COPY . /usr/src/vote21

ENTRYPOINT ["sh", "docker-entrypoint.sh"]
