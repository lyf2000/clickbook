# Dockerfile
# Pull base image
FROM python:3.8
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV EMAIL_HOST_USER <google email>
ENV EMAIL_HOST_PASSWORD <password>
# Set work directory
WORKDIR /code
# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt
# Copy project
COPY . /code/
