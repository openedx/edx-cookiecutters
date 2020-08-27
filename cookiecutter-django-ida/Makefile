.DEFAULT_GOAL := test

.PHONY: requirements test clean

requirements:
	pip install -r requirements.txt

test: clean
	# Create a new project with the default values
	cookiecutter . --no-input

	virtualenv -p python3.6 repo_name/.venv

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

docker_build:
	docker build . -f Dockerfile --target app -t openedx/repo_name
	docker build . -f Dockerfile --target newrelic -t openedx/repo_name:latest-newrelic

docker_tag: docker_build
	docker tag openedx/repo_name openedx/repo_name:${GITHUB_SHA}
	docker tag openedx/repo_name:latest-newrelic openedx/repo_name:${GITHUB_SHA}-newrelic

docker_auth:
	echo "$$DOCKERHUB_PASSWORD" | docker login -u "$$DOCKERHUB_USERNAME" --password-stdin

docker_push: docker_tag docker_auth ## push to docker hub
	docker push 'openedx/repo_name:latest'
	docker push "openedx/repo_name:${GITHUB_SHA}"
	docker push 'openedx/repo_name:latest-newrelic'
	docker push "openedx/repo_name:${GITHUB_SHA}-newrelic"
