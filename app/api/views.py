from flask import request, jsonify, Blueprint
from .models import Secret
from .utils import acquire_lock, release_lock, exponential_backoff
import re

bp = Blueprint('secrets', __name__)

@bp.route('/secrets', methods=['POST'])
def create_secret():
    # Use utility function to acquire lock
    acquire_lock()

    # Get the secret data from the request
    secret_data = request.get_json()

    # Create a new secret
    secret = Secret(secret_data)

    # Save the secret
    secret.save()

    # Use utility function to release lock
    release_lock()

    # Return the secret id
    return jsonify(id=secret.id), 201

@bp.route('/secrets/<id>', methods=['GET'])
def get_secret(id):
    # Fetch the secret
    secret = Secret.get(id)

    # Return the secret data
    return jsonify(secret.data)

@bp.route('/secrets/<id>', methods=['PUT'])
def update_secret(id):
    # Use utility function to acquire lock
    acquire_lock()

    # Get the new secret data from the request
    secret_data = request.get_json()

    # Fetch the secret
    secret = Secret.get(id)

    # Update the secret
    secret.update(secret_data)

    # Use utility function to release lock
    release_lock()

    # Return the updated secret data
    return jsonify(secret.data)

@bp.route('/secrets/<id>', methods=['DELETE'])
def delete_secret(id):
    # Use utility function to acquire lock
    acquire_lock()

    # Fetch the secret
    secret = Secret.get(id)

    # Delete the secret
    secret.delete()

    # Use utility function to release lock
    release_lock()

    # Return success status
    return '', 204

@bp.route('/secrets', methods=['GET'])
def get_secrets():
    # Fetch all secrets
    secrets = Secret.get_all()

    # Filter secrets based on regex pattern from request parameters
    pattern = request.args.get('pattern')
    if pattern:
        secrets = [s for s in secrets if re.match(pattern, s.name)]

    # Return the secrets data
    return jsonify([s.data for s in secrets])
