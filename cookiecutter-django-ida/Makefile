.DEFAULT_GOAL := test

.PHONY: requirements test clean

requirements:
	pip install -r requirements.txt

test: clean
	# Create a new project with the default values
	cookiecutter . --no-input

	virtualenv -p python3.8 repo_name/.venv

	# Generate requirement pins, install them, and execute the project's tests
	. repo_name/.venv/bin/activate && cd repo_name && pip install -U pip==19.3.1 wheel && make upgrade validation_requirements
	. repo_name/.venv/bin/activate && cd repo_name && python manage.py makemigrations
	. repo_name/.venv/bin/activate && cd repo_name && make migrate validate

	# Ensure translations can be compiled
	. repo_name/.venv/bin/activate && cd repo_name && make fake_translations

	# Ensure documentation can be compiled
	. repo_name/.venv/bin/activate && cd repo_name && make doc_requirements
	. repo_name/.venv/bin/activate && cd repo_name/docs && make html

clean:
	rm -rf .venv
	rm -rf repo_name
