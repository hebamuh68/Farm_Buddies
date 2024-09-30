FROM python:3.8-slim-buster

# Ensures that Python output is not buffered, meaning that logs and outputs 
# are written directly to the console (stdout and stderr) in real-time.
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /Farm-Buddies

# Install the necessary system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt