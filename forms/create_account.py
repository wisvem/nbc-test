#!/usr/bin/python3
"""Forms module"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email, Length, EqualTo


class CreateAccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    # TODO validate images
    pic = FileField('Photo', validators=[FileAllowed(
        ['png', 'jpg'], 'Not valid picture')])
    password = PasswordField('Password', validators=[
                             DataRequired(),
                             Length(min=6, message='Too short'),
                             EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm password')
    submit = SubmitField('Create')
