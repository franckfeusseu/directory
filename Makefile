ifneq (,$(wildcard ./.env))
include .env
ENV_FILE_PARAM = --env-file .env

endif

build:
	docker-compose up --build -d --remove-orphans

up:
	docker-compose up

down:
	docker-compose down

build-staging:
	docker-compose -f docker-compose.staging.yml up --build --remove-orphans

up-staging:
	docker-compose -f docker-compose.staging.yml up

makemigrations:
	docker-compose exec web bash -c "cd directory ; python manage.py makemigrations"

migrate:
	docker-compose exec -w /code/directory web python manage.py migrate

shell-web:
	docker exec -it web01 /bin/bash

collectstatic:
	docker exec -w /code/directory web01 python manage.py collectstatic

superuser:
	docker exec -w /code/directory web01 python manage.py createsuperuser

backup-database:
	@echo "Trying to update database ...."