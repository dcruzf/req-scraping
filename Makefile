SHELL := /bin/bash
SRC=src
TEST=tests

.PHONY: help
help:
	@echo 'POSSIBLE OPTIONS:'
	@echo '------------------'
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

.PHONY: test
test:
	@coverage run --source=${SRC} --context=${COV_CONTEXT} -m pytest

.PHONY: cov
cov:
	@coverage report -m

.PHONY: format
format:
	@isort ${SRC} ${TEST} . --force-single-line-imports > /dev/null
	@autoflake -r -i --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports --remove-unused-variables --expand-star-imports ${SRC} ${TEST}
	@isort ${SRC} ${TEST} . > /dev/null
	@black ${SRC} ${TEST} .


.PHONY: lint
lint:
	@flake8 ${SRC}/ ${TEST}/
	@isort --check --diff ${SRC} ${TEST}
	@black --check --diff ${SRC} ${TEST}
	@mypy --show-error-codes --pretty ${SRC} ${TEST}

.PHONY: install
install:
	@pip install -r requirements.txt

.PHONY: installdev
installdev:
	@pip install -r requirements-dev.txt

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -f src/*.c src/*.so
	python setup.py clean
	rm -rf coverage.xml

.PHONY: run
run:
	@PYTHONPATH=. python src/main.py urls.txt --attempts 3