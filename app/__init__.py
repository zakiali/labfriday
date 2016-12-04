import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from celery import Celery
from celery.schedules import crontab

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
mail = Mail(app)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from app import views, models, emails, tasks

#celery crontab
@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, tasks.followup_email.s(), name='add every 10')

    # Executes every Monday morning at 7:30 a.m.
    #sender.add_periodic_task(
    #    crontab(hour=7, minute=30, day_of_week=1),
    #    test.s('Happy Mondays!'),
    #)

@celery.task
def test():
    print 'Hello'

#@celery.task
#def reminder_email():
##    lunch = get_next_volunteer()
##    if lunch != None:
##        emails.reminder_email(lunch) 
#    print 'sending reminder email'
#
def followup_email():
    print 'sending followup email'
    lunch = views.get_todays_volunteer()
    if lunch != None:
        emails.followup_email(lunch)
 

#setup_periodic_tasks(celery)
