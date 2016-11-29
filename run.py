#! /usr/bin/env python
from app import app
import time
from app.scheduler import Scheduler
from app import jobs

if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.every().day.at("20:44").do(jobs.reminder_email)
    scheduler.every().day.at("20:44").do(jobs.followup_email)
    scheduler.run_continuously()
    app.run(debug=True, use_reloader=False)

