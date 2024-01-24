# Secrets Service Broker

## Plan
Below is a plan for the Python container service that interacts with an external secrets manager. The service will be implemented as a Flask-based REST API and will be containerized using Docker for deployment on EKS Fargate.

## Files & Directories:

1. `app/` - Main application directory
   - `__init__.py` - Initializes the Flask application and the API routes
   - `models.py` - Defines the Secret model (data schema)
   - `views.py` - Defines the endpoints for the API
   - `utils.py` - Contains utility functions for locking mechanism and exponential backoff
   - `tests.py` - Contains unit tests for the API

2. `Dockerfile` - Defines the Docker image for the application

3. `requirements.txt` - Lists the Python dependencies for the application

4. `docker-compose.yml` - Allows the application to be run locally for testing

## Code Structure:

### 1. `app/api/views.py`

This file initializes the Flask application and sets up the routes for the API. The API will have the following endpoints:

This file defines the logic for each API endpoint. Each function will interact with the external secrets manager (either AWS Secrets Manager or Hashicorp Vault) to perform the necessary operations. The functions will use the utility functions from `utils.py` to implement the locking mechanism and exponential backoff.

- `POST /secrets` - Create a new secret
- `GET /secrets/<id>` - Get a specific secret
- `PUT /secrets/<id>` - Update a specific secret
- `DELETE /secrets/<id>` - Delete a specific secret
- `GET /secrets` - Get all secrets (with optional regex filtering)

### 2. `app/models.py`

This file defines the Secret model. Each Secret will have the following fields:

- `id` - The unique identifier for the secret
- `value` - The value of the secret (this will be encrypted and never exposed in plaintext)
- `lock` - A boolean indicating whether the secret is currently locked

### 3. `app/utils.py`

This file contains utility functions for the locking mechanism and exponential backoff. The locking mechanism will ensure that operations that update, create, or modify secrets are atomic. The exponential backoff function will be used in case a lock is in place, or an API call fails or takes too long.

### 5. `tests/unit/`

This directory contains unit tests for the API. These tests will ensure that the API functions as expected, and that it handles errors correctly.

## Dockerfile

The Dockerfile will define the Docker image for the application. It will install the necessary Python dependencies and run the Flask application.

## requirements.txt

The requirements.txt file will list the Python dependencies for the application, including Flask and any libraries needed to interact with the external secrets manager (e.g., `boto3` for AWS Secrets Manager or `hvac` for Hashicorp Vault).

## docker-compose.yml

The docker-compose.yml file will allow the application to be run locally for testing. It will define services for the application and any necessary dependencies (such as a database, if needed).