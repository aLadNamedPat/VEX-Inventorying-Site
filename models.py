from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000000))
    urole = db.Column(db.String(100))
    inventory = db.Column(db.String(10000))

    def __init__(self, name, password, email, urole, inventory):
        self.name = name
        self.password = password
        self.email = email
        self.urole = urole
        self.inventory = inventory

    def get_id(self):
        return self.id

    def get_username(self):
        return self.name

    def get_urole(self):
        return self.urole
