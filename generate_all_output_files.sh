# invocation: EDX_COOKIECUTTER_ROOTDIR="$(PWD)" bash generate_all_output_files.sh
cookiecutter --no-input -o output/cookiecutter-python-library cookiecutter-python-library
cookiecutter --no-input -o output/cookiecutter-django-app cookiecutter-django-app
cookiecutter --no-input -o output/cookiecutter-django-ida cookiecutter-django-ida
cookiecutter --no-input -o output/cookiecutter-xblock cookiecutter-xblock
