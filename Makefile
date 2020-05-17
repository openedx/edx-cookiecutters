.PHONY: bake help quality replay requirements test upgrade validate watch

BAKE_OPTIONS=--no-input

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@awk -F ':.*?## ' '/^[a-zA-Z]/ && NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

bake.django_app: ## generate project using defaults
	cookiecutter $(BAKE_OPTIONS) cookiecutter-django-app --overwrite-if-exists

bake.django_ida: ## generate project using defaults
	cookiecutter $(BAKE_OPTIONS) cookiecutter-django-ida --overwrite-if-exists

bake.python_library: ## generate project using defaults
	cookiecutter $(BAKE_OPTIONS) cookiecutter-python-library --overwrite-if-exists

# Define PIP_COMPILE_OPTS=-v to get more information during make upgrade.
PIP_COMPILE = pip-compile --rebuild --upgrade $(PIP_COMPILE_OPTS)

upgrade: export CUSTOM_COMPILE_COMMAND=make upgrade
upgrade: ## update the requirements/*.txt files with the latest packages satisfying requirements/*.in
	pip install -qr requirements/pip-tools.txt
	# Make sure to compile files after any other files they include!
	$(PIP_COMPILE) -o requirements/pip-tools.txt requirements/pip-tools.in
	$(PIP_COMPILE) -o requirements/base.txt requirements/base.in
	$(PIP_COMPILE) -o requirements/test.txt requirements/test.in
	$(PIP_COMPILE) -o requirements/travis.txt requirements/travis.in
	$(PIP_COMPILE) -o requirements/dev.txt requirements/dev.in

quality: ## check coding style with pycodestyle and pylint
	tox -e quality

replay: BAKE_OPTIONS=--replay
replay: watch ## replay last cookiecutter run and watch for changes
	;

requirements: ## install development environment requirements
	pip install -qr requirements/pip-tools.txt
	pip install -r requirements/dev.txt

test: ## run tests on every supported Python version
	tox

validate: ## run tests and quality checks
	tox -e quality,py35,py38
	