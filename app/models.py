from flask_login import UserMixin
from sqlalchemy_json import mutable_json_type
from sqlalchemy.dialects.postgresql import JSONB
from . import db

class User(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    savedEmail = db.Column(db.String(100))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    urole = db.Column(db.String(100))
    inventory = db.Column(mutable_json_type(dbtype=JSONB, nested=True))
    wishlist_requests = db.Column(mutable_json_type(dbtype=JSONB, nested=True))
    # teams = db.Column(mutable_json_type(dbtype=JSONB, nested=True))
    received_requests = db.Column(mutable_json_type(dbtype=JSONB, nested=True))
    confirmedRequests = db.Column(db.Boolean(False))
    team_mates = db.Column(mutable_json_type(dbtype=JSONB, nested=True))

    def __init__(self, name, password, email, savedEmail, urole, inventory, wishlist_requests, received_requests, team_mates):
        self.name = name
        self.password = password
        self.email = email
        self.savedEmail = savedEmail
        self.urole = urole
        self.inventory = inventory
        self.wishlist_requests = wishlist_requests
        self.received_requests = received_requests
        self.team_mates = team_mates