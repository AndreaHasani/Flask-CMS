from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Email, Length


class loginForm(FlaskForm):
    username = StringField('username', validators=[
        InputRequired(), Length(min=3, max=20)])
    password = StringField('password', validators=[
        InputRequired(), Length(min=8, max=80)])
    # remember = BooleanField('remember me')


class registerForm(FlaskForm):
    username = StringField('username', [
        InputRequired(), Length(min=3, max=20)])
    password = StringField('password', [
        InputRequired(), Length(min=8, max=80)])
    email = StringField('username', [InputRequired(),
                                     Email(), Length(max=50)])
