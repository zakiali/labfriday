from flask_wtf import Form
from wtforms import StringField, BooleanField, DateField
from wtforms.validators import DataRequired

class SignupForm(Form):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    date = DateField('date', format='%m/%d/%Y', validators=[DataRequired()]) 

class RestaurantForm(Form):
    restaurant = StringField('restaurant', validators=[DataRequired()])

class FoodForm(Form):
    restaurant = StringField('restaurant', validators=[DataRequired()])
    order = StringField('order', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    
    
