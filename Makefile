.PHONY: help quality requirements test upgrade validate

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@awk -F ':.*?## ' '/^[a-zA-Z]/ && NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean: ## remove unneeded build artifacts, etc
	rm -rf __pycache__
	rm -rf lib/build

# Define PIP_COMPILE_OPTS=-v to get more information during make upgrade.
PIP_COMPILE = pip-compile --upgrade $(PIP_COMPILE_OPTS)

TEMPLATES=$(wildcard cookiecutter-*)
.PHONY: $(TEMPLATES)
$(TEMPLATES): requirements ## Create a new repo from the template
	test -e var/ || mkdir var
	EDX_COOKIECUTTER_ROOTDIR=$(PWD) cookiecutter $(PWD) --directory $(@) --output-dir var

upgrade: export CUSTOM_COMPILE_COMMAND=make upgrade
upgrade: ## update the requirements/*.txt files with the latest packages satisfying requirements/*.in
	pip install -qr requirements/pip-tools.txt
	$(PIP_COMPILE) --allow-unsafe --rebuild -o requirements/pip.txt requirements/pip.in
	# Make sure to compile files after any other files they include!
	$(PIP_COMPILE) -o requirements/pip-tools.txt requirements/pip-tools.in
	pip install -qr requirements/pip.txt
	pip install -qr requirements/pip-tools.txt
	$(PIP_COMPILE) -o requirements/base.txt requirements/base.in
	$(PIP_COMPILE) -o requirements/test.txt requirements/test.in
	$(PIP_COMPILE) -o requirements/ci.txt requirements/ci.in
	$(PIP_COMPILE) -o requirements/dev.txt requirements/dev.in

	make upgrade_template

REQ_PATH = "python-template/{{cookiecutter.placeholder_repo_name}}/requirements"

upgrade_template: export CUSTOM_COMPILE_COMMAND=make upgrade
upgrade_template: ## update the requirements/pip-tools.txt files within our cookiecutter template code with the latest packages satisfying requirements
	pip install -qr requirements/pip-tools.txt
	$(PIP_COMPILE) --rebuild -o "$(REQ_PATH)/pip-tools.txt" "$(REQ_PATH)/pip-tools.in"
	$(PIP_COMPILE) --allow-unsafe --rebuild -o "$(REQ_PATH)/pip.txt" "$(REQ_PATH)/pip.in"

PY_FILES = tests */hooks/*.py lib/src/*/*.py

quality: ## check coding style with pycodestyle and pylint
	pylint $(PY_FILES)
	pycodestyle $(PY_FILES)
	pydocstyle $(PY_FILES)
	isort --check-only --diff $(PY_FILES)

piptools: ## install pinned version of pip-compile and pip-sync
	pip install -r requirements/pip.txt
	pip install -r requirements/pip-tools.txt

requirements: piptools ## install development environment requirements
	pip-sync requirements/dev.txt
	pip install -e lib

test: ## run tests on every supported Python version
	tox

validate: ## run tests and quality checks
	tox -e quality,py
