from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
import json
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

class Secret(db.Model):
    """
    Secret Model
    Represents a secret object in the database
    """
    __tablename__ = "secrets"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    value = db.Column(db.String(), nullable=False)
    lock = db.Column(db.Boolean(), default=False)

    def __init__(self, value):
        self.value = json.dumps(value)
    
    def set_lock(self, lock_status):
        self.lock = lock_status

    def get_lock(self):
        return self.lock

    def __repr__(self):
        return '<Secret %r>' % self.id
