#!/usr/bin/python3
"""Forms module Create account"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf.file import FileField as ff
from flask_wtf.file import FileRequired as fr
from flask_wtf.file import FileAllowed as fa
from wtforms.validators import DataRequired, Email, Length, EqualTo


formats = ['jpg', 'png', 'jpeg']


class CreateAccountForm(FlaskForm):

    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email(message="Correo invalido")])
    pic = ff('Foto', validators=[fa(formats,
                                    'Formatos válidos '+', '.join(formats)),
                                 fr(message='La foto es obligatoria')],
             )
    password = PasswordField('Contraseña', validators=[
                             DataRequired(),
                             Length(min=3, message='Contraseña muy corta'),
                             EqualTo('confirm',
                                     message='Las contraseñas no coinciden')])
    confirm = PasswordField('Confirmar contraseña')
    submit = SubmitField('Crear cuenta')
