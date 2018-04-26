# labfriday

This project helps keep track of individuals who have ordered food for a group of people (initially used to keep track of our lab lunches).
It can be used for any group where individuals need to order food each week on a rotation. 

The app keeps track of who ordered, when, and what was ordered in different tables. It also sent automatic reminders about when to 
order food and updates about when food will be available.



# Getting Started

## Requirements
A requirements.tex file is included in the installation for a list of packages needed.
You will also need sqlite installed on your machine.

## Installation
For getting the basics running (without automatic emails) you will first need to create a database and then run the app.  
    ```> ./create_db.py```  
    ```> ./run.py```
    
To get the full functionality (which included automated emails), you will need to start the worker and schedulers. Run the following steps.  

Start by running the redis server  
    ```> redis-server # starts the redis database```  

In a different terminal start celery and celery-beat scheduler.  
    ```> celery -A app.celery worker -B --loglevel=info```  

The above command starts the celery worker and the beat scheduler in the same task. This is useful for locally running the web app, but for production applications it is better to run the celery worker and the beat scheduler as separate services. This can be done by first running  
    ```> celery -A app.celery worker --loglevel=info```  

and then in another terminal, starting the scheduler.  
    ```> celery -A app beat```  


Finally, in yet another terminal, run the app.  
    ```> ./run.py```  

## Options 
The app runs as is and you can add users and lunches to the database. However, if you decide that you want to add something else
to the database or add a new table, you will need to migrate the database. ```db_migrate.py``` is script to help you do this. Additionally,
you can go back and forth between database versions using db_upgrade.py and db_downgrade.py

All of the application interface and definitions are in the ```app``` directory. Here you will find the definitions for the views (or 
webpages), the forms (used for inputing information), database schema, email templates, and tasks (for sending automated emails using 
the celery framework). To update when emails get sent, look in the __init__.py script. You can also modify the specific tasks which are schedules in there.
