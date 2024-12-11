FROM_DC := cd docker &&
DC := docker-compose -p ebics-api-client-python
EXEC := $(DC) exec
DOCKER_COMPOSE_FILE := -f docker-compose.yml
BUILD := $(DC) $(DOCKER_COMPOSE_FILE) build
UP := $(DC) $(DOCKER_COMPOSE_FILE) up
DOWN := $(DC) down
PYTHONC := python-ebics-api-client-python
IN_MODULE := --workdir /var/www/ebics-api-client-python

.PHONY: Makefile start stop build

build:
	$(FROM_DC) $(BUILD) --no-cache

start:
	$(FROM_DC) $(UP) -d

stop:
	$(FROM_DC) $(DOWN)

bash:
	$(FROM_DC) $(EXEC) $(IN_MODULE) $(PYTHONC) sh