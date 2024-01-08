.PHONY: setup lint test

setup:
	pip install -r requirements.txt
	python -m pip install --upgrade pip
	echo "-dependencies installed"

test:
	pytest -s -v --cov=./ --cov-report term-missing

lint:
	black .
	echo "-code is formatted with black"
	ruff . --fix
	echo "-code is formatted with ruff"
