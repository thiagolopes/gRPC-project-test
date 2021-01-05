clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

pyformat:
	poetry run black .
	poetry run isort .

test:
	poetry run pytest -x shopping-api

install-deps:
	poetry install

install-deps-without-dev:
	poetry install --no-dev

run:
	poetry run shopping-api/manage.py runserver 8081

migrate:
	poetry run shopping-api/manage.py migrate

makemigrations:
	poetry run shopping-api/manage.py makemigrations

create-user:
	poetry run shopping-api/manage.py createsuperuser
