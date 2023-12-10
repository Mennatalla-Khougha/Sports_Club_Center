#!/usr/bin/python3
from flask_security.forms import LoginForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired

class ExtendedLoginForm(LoginForm):
    email = None  # Remove the email field
    username = StringField('Username', [DataRequired()])
    # email = StringField('Username or Email Address', [InputRequired()])