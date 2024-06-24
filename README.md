# Offline Debug Environment

This Dockerfile is used to build a Docker image based on Ubuntu 22.04. It installs various tools and dependencies required for a Python application. The image also includes MongoDB database tools and sets the timezone to Europe/Istanbul.


Example usage
```
docker run -it --rm --name debug --privileged \
       -e NAME=debug-container \
       -v /media/py:/media  \
       nexus.local:8090/ubuntu-python-debug:0.0.6
```
