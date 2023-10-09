FROM ubuntu:focal as app

ENV DEBIAN_FRONTEND noninteractive
# System requirements.
RUN apt update && \
  apt-get install -qy \
  curl \
  gettext \
  # required by bower installer
  git \
  language-pack-en \
  build-essential \
  python3.8-dev \
  python3-virtualenv \
  python3.8-distutils \
  libmysqlclient-dev \
  libssl-dev \
  # mysqlclient >= 2.2.0 requires pkg-config.
  pkg-config \
  libcairo2-dev && \
  rm -rf /var/lib/apt/lists/*

# Use UTF-8.
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ARG COMMON_APP_DIR="/edx/app"
ARG COMMON_CFG_DIR="/edx/etc"
ARG COOKIECUTTER_SERVICE_NAME={{cookiecutter.repo_name}}
ARG COOKIECUTTER_PROJECT_NAME={{cookiecutter.project_name}}
ARG COOKIECUTTER_APP_DIR="${COMMON_APP_DIR}/${COOKIECUTTER_SERVICE_NAME}"
ARG COOKIECUTTER_VENV_DIR="${COMMON_APP_DIR}/${COOKIECUTTER_SERVICE_NAME}/venvs/${COOKIECUTTER_SERVICE_NAME}"
ARG COOKIECUTTER_CODE_DIR="${COOKIECUTTER_APP_DIR}/${COOKIECUTTER_PROJECT_NAME}"
ARG COOKIECUTTER_NODEENV_DIR="${COOKIECUTTER_APP_DIR}/nodeenvs/${COOKIECUTTER_SERVICE_NAME}"

ENV PATH "${COOKIECUTTER_VENV_DIR}/bin:${COOKIECUTTER_NODEENV_DIR}/bin:$PATH"
ENV COOKIECUTTER_CFG "/edx/etc/${COOKIECUTTER_SERVICE_NAME}.yml"
ENV COOKIECUTTER_CODE_DIR "${COOKIECUTTER_CODE_DIR}"
ENV COOKIECUTTER_APP_DIR "${COOKIECUTTER_APP_DIR}"

RUN virtualenv -p python3.8 --always-copy ${COOKIECUTTER_VENV_DIR}

# No need to activate IDA venv as it is already in path
RUN pip install nodeenv

RUN nodeenv ${COOKIECUTTER_NODEENV_DIR} --node=16.14.0 --prebuilt && npm install -g npm@8.5.x

# Working directory will be root of repo.
WORKDIR ${COOKIECUTTER_CODE_DIR}

# Copy over repository
COPY . .

RUN npm install --production && ./node_modules/.bin/bower install --allow-root --production && ./node_modules/.bin/webpack --config webpack.config.js --progress

# Expose canonical Cookie Cutter port
EXPOSE {{cookiecutter.port}}

FROM app as prod

ENV DJANGO_SETTINGS_MODULE "${COOKIECUTTER_SERVICE_NAME}.settings.production"

RUN pip install -r ${COOKIECUTTER_CODE_DIR}/requirements/production.txt

CMD gunicorn --bind=0.0.0.0:{{cookiecutter.port}} --workers 2 --max-requests=1000 -c ${COOKIECUTTER_CODE_DIR}/docker_gunicorn_configuration.py ${COOKIECUTTER_PROJECT_NAME}.wsgi:application

FROM app as dev

ENV DJANGO_SETTINGS_MODULE "${COOKIECUTTER_SERVICE_NAME}.settings.devstack"

RUN pip install -r ${COOKIECUTTER_CODE_DIR}/requirements/django.txt
RUN pip install -r ${COOKIECUTTER_CODE_DIR}/requirements/local.txt

# Devstack related step for backwards compatibility
RUN touch ${COOKIECUTTER_APP_DIR}/${COOKIECUTTER_SERVICE_NAME}_env

CMD while true; do python ./manage.py runserver 0.0.0.0:{{cookiecutter.port}}; sleep 2; done

###########################################################
# Define k8s target
FROM prod as kubernetes
ENV COOKIECUTTER_SETTINGS='kubernetes'
ENV DJANGO_SETTINGS_MODULE="${COOKIECUTTER_SERVICE_NAME}.settings.$COOKIECUTTER_SETTINGS"