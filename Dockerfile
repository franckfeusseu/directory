FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install dependencies
RUN pip install --upgrade pip setuptools

# create user for the Django project
RUN useradd -ms /bin/bash directory

#set user
USER directory

# set work directory
WORKDIR /home/directory

# create and activate virtual environment
RUN python3 -m venv env

# copy and install pip requirements
COPY --chown=directory ./requirements /home/directory/requirements/
RUN ./env/bin/pip3 install -r /home/directory/requirements/base.txt

COPY --chown=directory directory /home/directory/