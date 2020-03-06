from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed
from appmain.user.models import Userdata

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    picture = FileField('Profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = Userdata.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please choose a different username.')

    def validate_email(self, email):
        email = Userdata.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is already taken. Please choose a different email address.')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        user = Userdata.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please choose a different username.')

    def validate_email(self, email):
        email = Userdata.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is already taken. Please choose a different email address.')

class DeleteAccountForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        email = Userdata.query.filter_by(email=email.data).first()
        if email is None:
            raise ValidationError('There is no account with that Email address. Please register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
