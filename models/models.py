#!/usr/bin/python3
"""Models module"""

from flask_login import UserMixin
from uuid import uuid4
from werkzeug.security import check_password_hash as cph
from werkzeug.security import generate_password_hash as gph


users = []


class User(UserMixin):
    def __init__(self):
        self.id = str(uuid4())

    def update(self, *argv):
        self.name = argv[0]
        self.email = argv[1]
        self.password = gph(argv[2])
        self.pic_name = argv[3]

    def set_password(self, password):
        self.password = gph(password)

    def check_password(self, password):
        return cph(self.password, password)

    def set_profile_pic(self, image):
        pass

    def __repr__(self):
        return '<User {}>'.format(self.email)


def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None
