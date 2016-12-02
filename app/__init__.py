import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from celery import Celery

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
mail = Mail(app)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from app import views, models
