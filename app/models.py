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
    teams = db.Column(mutable_json_type(dbtype=JSONB, nested=True))
    received_requests = db.Column(mutable_json_type(dbtype=JSONB, nested=True))
    confirmedRequests = db.Column(db.Boolean(False))
    team_mates = db.Column(mutable_json_type(dbtype=JSONB, nested=True))
    if (urole == "student"):
        coach = ""
    else:
        coach = email

    def __init__(self, name, password, email, savedEmail, urole, inventory, teams, received_requests, team_mates):
        self.name = name
        self.password = password
        self.email = email
        self.savedEmail = savedEmail
        self.urole = urole
        self.inventory = inventory
        self.teams = teams
        self.received_requests = received_requests
        self.team_mates = team_mates
    def get_id(self):
        return self.id

    def get_username(self):
        return self.name
    
    def get_email(self):
        return self.email

    def get_urole(self):
        return self.urole

    def get_inventory(self):
        return self.inventory
    
    def set_coach(self, val):
        self.coach = val

    def set_inventory(self, inventory):
        if (self.urole == "coach"):
            self.inventory = self.inventory
        else:
            self.inventory = inventory
    # def get_inventory(self):
    #     return self.inventory
