.DEFAULT_GOAL := help

.PHONY: dev.clean dev.build dev.run upgrade help requirements
.PHONY: extract_translations compile_translations
.PHONY: detect_changed_source_translations dummy_translations build_dummy_translations
.PHONY: validate_translations pull_translations install_transifex_clients

REPO_NAME := {{cookiecutter.repo_name}}
PACKAGE_NAME := {{cookiecutter.package_name}}
EXTRACT_DIR := $(PACKAGE_NAME)/conf/locale/en/LC_MESSAGES
JS_TARGET := $(PACKAGE_NAME)/public/js/translations

help:
	@perl -nle'print $& if m{^[\.a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

# Common constraints for edx repos. When pinning something here, please provide
# an explanation of why. Ideally, link to other information that will help
# people in the future to remove the pin when possible. Writing an issue
# against the offending project and linking to it here is good.
export UV_CONSTRAINT = https://raw.githubusercontent.com/edx/edx-lint/master/edx_lint/files/common_constraints.txt

upgrade: ## update the uv.lock file with the latest packages satisfying pyproject.toml
	uv lock --upgrade

requirements: ## install development environment requirements
	uv sync --group dev

dev.clean:
	-docker rm $(REPO_NAME)-dev
	-docker rmi $(REPO_NAME)-dev

dev.build:
	docker build -t $(REPO_NAME)-dev $(CURDIR)

dev.run: dev.clean dev.build ## Clean, build and run test image
	docker run -p 8000:8000 -v $(CURDIR):/usr/local/src/$(REPO_NAME) --name $(REPO_NAME)-dev $(REPO_NAME)-dev

dev.stop: ## Stop the running container
	docker stop $(REPO_NAME)-dev

dev.migrate: ## Run migrations in the container
	docker exec -it $(REPO_NAME)-dev python manage.py migrate

dev.logs: ## View logs from the container
	docker logs -f $(REPO_NAME)-dev

dev.exec: ## Execute to the dev container
	docker exec -it $(REPO_NAME)-dev /bin/bash

## Localization targets

extract_translations: ## extract strings to be translated, outputting .po files
	cd $(PACKAGE_NAME) && i18n_tool extract --no-segment --merge-po-files
	mv $(EXTRACT_DIR)/django.po $(EXTRACT_DIR)/text.po

compile_translations: ## compile translation files, outputting .mo files for each supported language
	cd $(PACKAGE_NAME) && i18n_tool generate
	python manage.py compilejsi18n --namespace {{cookiecutter.i18n_namespace}} --output $(JS_TARGET)

detect_changed_source_translations:
	cd $(PACKAGE_NAME) && i18n_tool changed

dummy_translations: ## generate dummy translation (.po) files
	cd $(PACKAGE_NAME) && i18n_tool dummy

build_dummy_translations: dummy_translations compile_translations ## generate and compile dummy translation files

validate_translations: build_dummy_translations detect_changed_source_translations ## validate translations

pull_translations: ## pull translations from transifex
	cd $(PACKAGE_NAME) && i18n_tool transifex pull

install_transifex_client: ## Install the Transifex client
	# Installing client will skip CHANGELOG and LICENSE files from git changes
	# so remind the user to commit the change first before installing client.
	git diff -s --exit-code HEAD || { echo "Please commit changes first."; exit 1; }
	curl -o- https://raw.githubusercontent.com/transifex/cli/master/install.sh | bash
	git checkout -- LICENSE README.md ## overwritten by Transifex installer

selfcheck: ## check that the Makefile is well-formed
	@echo "The Makefile is well-formed."
