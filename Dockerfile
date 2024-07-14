# Pull official base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /appointment

# Install dependencies
COPY requirements.txt /appointment/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /code/
