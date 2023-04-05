from . import db
from os import path
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String, unique=True)
    username=db.Column(db.String)
    first_name=db.Column(db.String)
    last_name=db.Column(db.String)
    password=db.Column(db.String)
    confirm_password=db.Column(db.String)
    notes=db.relationship('Notes')
    feedback=db.relationship('Feedback')

class Notes(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

class Feedback(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    feedback_data=db.Column(db.String)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

