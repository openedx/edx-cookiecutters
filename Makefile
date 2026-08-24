.PHONY: help quality requirements test upgrade upgrade_template validate

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@awk -F ':.*?## ' '/^[a-zA-Z]/ && NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean: ## remove unneeded build artifacts, etc
	rm -rf __pycache__
	rm -rf lib/build

TEMPLATES=$(wildcard cookiecutter-*)
.PHONY: $(TEMPLATES)
$(TEMPLATES): requirements ## Create a new repo from the template
	test -e var/ || mkdir var
	EDX_COOKIECUTTER_ROOTDIR=$(PWD) uv run cookiecutter $(PWD) --directory $(@) --output-dir var

upgrade: ## update uv.lock with the latest packages satisfying pyproject.toml
	uv lock --upgrade

	make upgrade_template

# Define PIP_COMPILE_OPTS=-v to get more information during make upgrade_template.
# NOTE: python-template still uses pip-tools-style requirements/*.in -> *.txt files
# (it's shared by every cookiecutter template and hasn't been migrated to uv yet).
# We compile them with `uv pip compile`, uv's drop-in replacement for pip-compile,
# so this target no longer needs pip-tools installed anywhere.
PIP_COMPILE = uv pip compile --upgrade $(PIP_COMPILE_OPTS)
REQ_PATH = "python-template/{{cookiecutter.placeholder_repo_name}}/requirements"

upgrade_template: export CUSTOM_COMPILE_COMMAND=make upgrade
upgrade_template: ## update the requirements/*.txt files within our cookiecutter template code with the latest packages satisfying requirements
	$(PIP_COMPILE) -o "$(REQ_PATH)/pip-tools.txt" "$(REQ_PATH)/pip-tools.in"
	$(PIP_COMPILE) --allow-unsafe -o "$(REQ_PATH)/pip.txt" "$(REQ_PATH)/pip.in"

PY_FILES = tests */hooks/*.py lib/src/*/*.py

quality: ## check coding style with pycodestyle and pylint
	pylint $(PY_FILES)
	pycodestyle $(PY_FILES)
	pydocstyle $(PY_FILES)
	isort --check-only --diff $(PY_FILES)

requirements: ## install development environment requirements
	uv sync --group dev

test: ## run tests on every supported Python version
	tox

validate: ## run tests and quality checks
	tox -e quality,py
