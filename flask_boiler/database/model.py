#! /usr/bin/env python

from flask_boiler.database import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    slack_subscription = db.Column(db.String(32))
    slack_id = db.Column(db.String(16))

class Score(db.Model):
    __tablename__ = 'score'

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    given = db.Column(db.Integer)
    bank = db.Column(db.Integer)

    user = db.relationship(User, uselist=False)
    slack_id = db.Column(db.String(16), db.ForeignKey('user.slack_id'))
