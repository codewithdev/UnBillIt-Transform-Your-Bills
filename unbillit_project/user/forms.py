from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from unbillit_project.models import User


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):

    first_name = StringField('First Name', validators=[DataRequired(), Length(
        min=2, max=24, message='First name must be 2 to 24 characters long')])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(
        min=2, max=24, message='Last name must be 2 to 24 characters long')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, max=64, message='Password must be minimum 8 characters long!..'),
    ])
    ########## show validation messages in login.html and register.html ###########
    password_confirm = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')

    def check_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError(
                'Your Email has already been registered. Please use a different one')

    ################# TO DO ##################
    # Add password strength validators later #
    ##########################################


class UpdateUserForm(FlaskForm):

    first_name = StringField('First Name', validators=[DataRequired(), Length(
        min=2, max=24, message='First name must be 2 to 24 characters long')])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(
        min=2, max=24, message='Last name must be 2 to 24 characters long')])
    email = StringField('Email')
    profile_img = FileField('Update profile picture', validators=[
        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')


class ContactForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired(), Length(
        min=2, max=24, message='Name must be 2 to 64 characters long')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(
        min=4, max=2048, message='Last name must be 4 to 2048 characters long')])
    submit = SubmitField('Send')
