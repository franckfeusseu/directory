FROM python:3.8

LABEL maintainer='Franck Fesse <me@fessefranck.com>'

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

COPY --chown=directory ./directory /home/directory/
# copy scripts
COPY --chown=directory ./scripts /home/directory

#exposing our django port : 8000
EXPOSE 8000

# Serve the app
CMD ["bash", "start_server.sh"]