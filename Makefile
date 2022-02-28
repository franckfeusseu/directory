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

