from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField
from wtforms.validators import DataRequired

class SignupForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    date = DateField('date', format='%m/%d/%Y', validators=[DataRequired()]) 

class RestaurantForm(FlaskForm):
    restaurant = StringField('restaurant', validators=[DataRequired()])

class FoodForm(FlaskForm):
    restaurant = StringField('restaurant', validators=[DataRequired()])
    order = StringField('order')
    price = StringField('price')

