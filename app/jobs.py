from views import get_next_volunteer, get_todays_volunteer
import emails
import time

def reminder_email():
    lunch = get_next_volunteer()
    if lunch != None:
        emails.reminder_email(lunch) 
    
def followup_email()
    lunch = get_todays_volunteer()
    if lunch != None:
        emails.followup_email(lunch)
       

