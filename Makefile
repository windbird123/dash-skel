.PHONY: help

help:
	@echo "Usage:"
	@echo "  make run                Run main.py with uv run"
	@echo "  make dev                Run the package with developer settings"
	@echo "  make prod               Run the pacakge with production settings"
	@echo "  make test               CI: Run tests"
	@echo "  make cov                CI: Run test and calculate coverage"
	@echo "  make lint               CI: Lint & Format the code"
	@echo "  make check              CI: Check typing"
	@echo "  make doc                Run local documentation server"
	@echo "  make build              Build the package wheel before publishing to Pypi"
	@echo "  make publish            Publish package to Pypi"
	@echo "  make dbuild             Build the docker image"
	@echo "  make drun               Run the docker image"
	@echo "  make dshell             Enter the docker bash"
	@echo "  make all                Run all CI steps (lint, check, test coverage)"

run:
	uv run main.py

test:
	uv run pytest -vvv -x tests/

cov:
	uv run pytest --cov=./ tests/ --cov-report=term-missing

lint:
	uv run ruff format .
	uv run ruff check --fix .

check:
	uv run ty check .

doc:
	uvx --with mkdocstrings  --with mkdocs-material --with mkdocstrings-python --with mkdocs-include-markdown-plugin mkdocs serve

build:
	uv build

publish:
	uv publish

commit:
	uv run pre-commit

dbuild:
	docker build -t stock-app:latest .

drun:
	docker run --rm stock-app:latest

dshell:
	docker run --rm -it stock-app:latest bash

all:
	$(MAKE) lint
	$(MAKE) check
	$(MAKE) cov
