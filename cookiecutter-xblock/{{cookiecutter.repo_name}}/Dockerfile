# Use the official Open edX XBlock SDK image as the base image
FROM openedx/xblock-sdk

# Create the directory for the repository
RUN mkdir -p /usr/local/src/{{cookiecutter.repo_name}}

# Set the created directory as a Docker volume
VOLUME ["/usr/local/src/{{cookiecutter.repo_name}}"]

# Update the package list and install gettext
RUN apt-get update && \
    apt-get install -y gettext

# Prepare the install_and_run_xblock script by appending necessary commands
RUN echo "pip install -r /usr/local/src/{{cookiecutter.repo_name}}/requirements.txt" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh && \
    echo "pip install -e /usr/local/src/{{cookiecutter.repo_name}}" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh && \
    echo "cd /usr/local/src/{{cookiecutter.repo_name}} && make compile_translations && cd /usr/local/src/xblock-sdk" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh && \
    echo "exec python /usr/local/src/xblock-sdk/manage.py \"\$@\"" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh

# Make the install_and_run_xblock script executable
RUN chmod +x /usr/local/src/xblock-sdk/install_and_run_xblock.sh

# Define the entrypoint to use the custom script
ENTRYPOINT ["/bin/bash", "/usr/local/src/xblock-sdk/install_and_run_xblock.sh"]

# Set the default command for the container
CMD ["runserver", "0.0.0.0:8000"]
