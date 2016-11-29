import schedule
import threading
import time

class Scheduler(schedule.Scheduler):
    def __init__(self): schedule.Scheduler.__init__(self)
    
    def run_continuously(self, interval=1):
        cease_continuous_run = threading.Event()
        
        class ScheduleThread(threading.Thread):
            @classmethod
            def run(cls):
                while not cease_continuous_run.is_set():
                    self.run_pending()
                    time.sleep(interval)
        continuous_thread = ScheduleThread()
        continuous_thread.start()
        return cease_continuous_run
