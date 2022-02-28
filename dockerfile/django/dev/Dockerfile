FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir code
WORKDIR /code
COPY ./requirements /code/requirements/
RUN pip install -r requirements/base.txt
COPY . /code/