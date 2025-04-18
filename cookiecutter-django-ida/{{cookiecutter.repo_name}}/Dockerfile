FROM ubuntu:focal AS app

ARG PYTHON_VERSION=3.12
ENV TZ=UTC
ENV TERM=xterm-256color
ENV DEBIAN_FRONTEND=noninteractive

# software-properties-common is needed to setup our Python 3.12 env
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    apt-add-repository -y ppa:deadsnakes/ppa

# Packages installed:
# curl; used to install pip
# gcc; for compiling python extensions distributed with python packages like mysql-client
# language-pack-en & locales; Ubuntu locale support so that system utilities have a consistent language and time zone.
# libmysqlclient-dev; to install header files needed to use native C implementation for MySQL-python for performance gains.
# libssl-dev; mysqlclient wont install without this.
# python{version}; ubuntu doesnt ship with python, so this is the python we will use to run the application
# python{version}-dev; to install header files for python extensions; much wheel-building depends on this
#
# If you add a package here please include a comment above describing what it is used for
RUN apt-get update && apt-get -qy install --no-install-recommends \
        curl \
        gcc \
        language-pack-en \
        libmysqlclient-dev \
        libssl-dev \
        locales \
        pkg-config \
        python${PYTHON_VERSION} \
        python${PYTHON_VERSION}-dev

# delete apt package lists because we do not need them inflating our image
RUN rm -rf /var/lib/apt/lists/*

# Install pip for our version of Python
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python${PYTHON_VERSION}

# create our Python virtual env
ENV VIRTUAL_ENV=/openedx/venvs/{{cookiecutter.project_name}}
RUN pip install virtualenv
RUN virtualenv -p python${PYTHON_VERSION} ${VIRTUAL_ENV}
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Python is Python3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Setup zoneinfo for Python 3.12
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Use UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

EXPOSE {{cookiecutter.port}}
RUN useradd -m --shell /bin/false app

WORKDIR /edx/app/{{cookiecutter.repo_name}}

FROM app AS prod

ENV DJANGO_SETTINGS_MODULE={{cookiecutter.project_name}}.settings.production

# Copy the requirements explicitly even though we copy everything below
# this prevents the image cache from busting unless the dependencies have changed.
COPY requirements/production.txt /edx/app/{{cookiecutter.repo_name}}/requirements/production.txt

# Dependencies are installed as root so they cannot be modified by the application user.
RUN pip install -r requirements/production.txt

RUN mkdir -p /edx/var/log

# Code is owned by root so it cannot be modified by the application user.
# So we copy it before changing users.
USER app

# Gunicorn 19 does not log to stdout or stderr by default. Once we are past gunicorn 19, the logging to STDOUT need not be specified.
CMD gunicorn --workers=2 --name {{cookiecutter.repo_name}} -c /edx/app/{{cookiecutter.repo_name}}/{{cookiecutter.project_name}}/docker_gunicorn_configuration.py --log-file - --max-requests=1000 {{cookiecutter.project_name}}.wsgi:application

# This line is after the requirements so that changes to the code will not bust the image cache
COPY . /edx/app/{{cookiecutter.repo_name}}

FROM app AS dev

ENV DJANGO_SETTINGS_MODULE={{cookiecutter.project_name}}.settings.devstack

# Copy the requirements explicitly even though we copy everything below
# this prevents the image cache from busting unless the dependencies have changed.
COPY requirements/dev.txt /edx/app/{{cookiecutter.repo_name}}/requirements/dev.txt

RUN pip install -r requirements/dev.txt

# After the requirements so changes to the code will not bust the image cache
COPY . /edx/app/{{cookiecutter.repo_name}}

# Devstack related step for backwards compatibility
RUN touch {{cookiecutter.project_name}}/{{cookiecutter.project_name}}_env

CMD while true; do python ./manage.py runserver 0.0.0.0:{{cookiecutter.port}}; sleep 2; done
