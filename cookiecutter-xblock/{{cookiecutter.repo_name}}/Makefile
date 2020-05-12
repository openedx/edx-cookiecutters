.DEFAULT_GOAL := help

.PHONY: dev.clean dev.build dev.run

REPO_NAME := {{cookiecutter.repo_name}}
PACKAGE_NAME := {{cookiecutter.package_name}}
EXTRACT_DIR := $(PACKAGE_NAME)/locale/en/LC_MESSAGES
EXTRACTED_DJANGO := $(EXTRACT_DIR)/django-partial.po
EXTRACTED_DJANGOJS := $(EXTRACT_DIR)/djangojs-partial.po
EXTRACTED_TEXT := $(EXTRACT_DIR)/text.po
JS_TARGET := public/js/translations
TRANSLATIONS_DIR := $(PACKAGE_NAME)/translations

help:
	@perl -nle'print $& if m{^[\.a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

dev.clean:
	-docker rm $(REPO_NAME)-dev
	-docker rmi $(REPO_NAME)-dev

dev.build:
	docker build -t $(REPO_NAME)-dev $(CURDIR)

dev.run: dev.clean dev.build ## Clean, build and run test image
	docker run -p 8000:8000 -v $(CURDIR):/usr/local/src/$(REPO_NAME) --name $(REPO_NAME)-dev $(REPO_NAME)-dev

## Localization targets

extract_translations: symlink_translations ## extract strings to be translated, outputting .po files
	cd $(PACKAGE_NAME) && i18n_tool extract
	mv $(EXTRACTED_DJANGO) $(EXTRACTED_TEXT)
	if [ -f "$(EXTRACTED_DJANGOJS)" ]; then cat $(EXTRACTED_DJANGOJS) >> $(EXTRACTED_TEXT); rm $(EXTRACTED_DJANGOJS); fi

compile_translations: symlink_translations ## compile translation files, outputting .mo files for each supported language
	cd $(PACKAGE_NAME) && i18n_tool generate
	python manage.py compilejsi18n --namespace $(PACKAGE_NAME)i18n --output $(JS_TARGET)

detect_changed_source_translations:
	cd $(PACKAGE_NAME) && i18n_tool changed

dummy_translations: ## generate dummy translation (.po) files
	cd $(PACKAGE_NAME) && i18n_tool dummy

build_dummy_translations: dummy_translations compile_translations ## generate and compile dummy translation files

validate_translations: build_dummy_translations detect_changed_source_translations ## validate translations

pull_translations: ## pull translations from transifex
	cd $(PACKAGE_NAME) && i18n_tool transifex pull

push_translations: extract_translations ## push translations to transifex
	cd $(PACKAGE_NAME) && i18n_tool transifex push

symlink_translations:
	if [ ! -d "$(TRANSLATIONS_DIR)" ]; then ln -s locale/ $(TRANSLATIONS_DIR); fi