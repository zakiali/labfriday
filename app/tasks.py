import views #app.views import get_next_volunteer, get_todays_volunteer
import emails
import time
from app import celery

@celery.task
def reminder_email():
    lunch = views.get_next_volunteer()
    if lunch != None:
        emails.reminder_email(lunch) 
        print 'sending reminder email to {0}'.format(lunch.author.nickname)

@celery.task
def followup_email():
    lunch = views.get_todays_volunteer()
    if lunch != None:
        emails.followup_email(lunch)
        print 'sending followup email to {0}'.format(lunch.author.nickname)

@celery.task
def foodishere_email():
    lunch = views.get_todays_volunteer()
    emails.foodishere_email(lunch)
    print 'sending food is here email to lab friday list'
