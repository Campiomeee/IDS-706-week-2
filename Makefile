.PHONY: format format-check lint test

format:
	black project tests

format-check:
	black --check project tests

lint:
	flake8 project --ignore=E203,W503 --max-line-length=100

test:
	pytest -q
