from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import EqualTo, InputRequired


class SignUpForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField("Let's Go!")


class LogInForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField("Let's Go!")


class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    body = StringField('Body', validators=[InputRequired()])
    submit = SubmitField("Submit Your Post")