WTF_CSRF_ENABLED = False
SECRET_KEY = 'you-will-never-guess'

#SQLAlchemy database setup
import os 
basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('IS_HEROKU'):
    SERVER_NAME='labfriday.herokuapp.com'
else:
    SERVER_NAME='127.0.0.1:5000'

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
#MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = MAIL_USERNAME
#Celery setup
CELERY_BROKER_URL = os.environ.get('REDIS_URL','redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
CELERY_TIMEZONE='US/Pacific'

#timezone config
TIMEZONE='US/Pacific'
