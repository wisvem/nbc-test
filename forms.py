#!/usr/bin/python3
"""Forms module"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms.validators import DataRequired, Email, Length


class CreateAccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    photo = FileField(validators=[FileAllowed(
        photos, 'Image only!'), FileRequired('File was empty!')])
    submit = SubmitField('Create')
