.PHONY: setup test lint run db

setup:
	pip install -r requirements.txt
	python -m pip install --upgrade pip
	echo "-dependencies installed"

test:
	pytest -s -v --cov=./ --cov-report term-missing

lint:
	black . && ruff . --fix

run:
	python manage.py runserver

db:
	python manage.py migrate