FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && apt-get install -y postgresql-client python3.10 python3-pip
RUN mkdir code
WORKDIR /code
COPY ./requirements /code/requirements/
RUN pip3 install -r requirements/base.txt
COPY . /code/