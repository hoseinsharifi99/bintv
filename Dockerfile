# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /blog_project

# Install dependencies
COPY requirements.txt /blog_project/
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /blog_project/