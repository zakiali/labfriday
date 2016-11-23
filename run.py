#! /usr/bin/env python
from app import app
import time
from app.scheduler import Scheduler

if __name__ == '__main__':
    #scheduler = Scheduler()
    #scheduler.every(10).seconds.do()
    app.run(debug=True)

