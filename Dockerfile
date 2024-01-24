# Dockerfile
FROM python:3.8-slim-buster

# Create directory for the app user
RUN mkdir -p /home/app

# Create the app user
RUN addgroup --system app && adduser --system --group app

# Create the home directory
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME

# Set the working directory in the docker container
WORKDIR $APP_HOME

# Install dependencies
RUN apt-get update && apt-get install -y build-essential

# Copy requirements.txt
COPY requirements.txt requirements.txt

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . $APP_HOME

# Chown all the files to the app user
RUN chown -R app:app $APP_HOME

# Change to the app user
USER app

# Expose the port the app runs in
EXPOSE 5000

# Define the command to start the container
CMD gunicorn --bind 0.0.0.0:5000 app:app