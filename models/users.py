#!/usr/bin/python3
"""Models module"""

from flask_login import UserMixin
from uuid import uuid4
from werkzeug.security import check_password_hash as cph
from werkzeug.security import generate_password_hash as gph
from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    pic_name = db.Column(db.String(128), nullable=False)

    def __init__(self):
        self.id = str(uuid4())

    def __repr__(self):
        return f'<User {self.email}>'

    def check_password(self, password):
        return cph(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    def update(self, *argv):
        self.name = argv[0]
        self.email = argv[1]
        self.password = gph(argv[2])
        self.pic_name = argv[3]
