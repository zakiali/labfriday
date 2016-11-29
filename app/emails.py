from flask import render_template
from flask_mail import Message
from app import app,mail
import datetime

def send_email(subject, sender, recipients, text_body, html_body):
    '''Generic function to send an email'''
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def reminder_email(lunch_model): 
    '''Send a reminder email'''
    subject='[labfriday] You are ordering lab lunch this week! Thanks you!'
    sender = 'zakiali88@gmail.com'
    recipients = [lunch_model.author.email]
    with app.app_context():
        text_body = render_template("reminder.txt", lunch=lunch_model)
        html_body = render_template("reminder.html", lunch=lunch_model)
        send_email(subject, sender, recipients, text_body, html_body)

def followup_email(lunch_model):
    '''Send a follow up email'''
    subject='[labfriday] Thank you for feeding us!'
    sender = 'zakiali88@gmail.com'
    recipients = [lunch_model.author.email]
    with app.app_context():
        text_body = render_template("followup.txt", lunch=lunch_model)
        html_body = render_template("followup.html", lunch=lunch_model)
        send_email(subject, sender, recipients, text_body, html_body)
   
