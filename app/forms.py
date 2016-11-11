from flask_wtf import Form
from wtforms import StringField, BooleanField, DateField
from wtforms.validators import DataRequired

class LoginForm(Form):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    date = DateField('date', format='%m/%d/%Y', validators=[DataRequired()]) 
