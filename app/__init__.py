import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
mail = Mail(app)


from app import views, models, jobs
from app import scheduler

scheduler = scheduler.Scheduler()
scheduler.every().day.at("22:18").do(jobs.reminder_email)
scheduler.every().day.at("22:21").do(jobs.followup_email)
scheduler.run_continuously()
