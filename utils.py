import time
from celery import Celery

def sleepy():
    time.sleep(4)
    return 'hello'

# Define Celery app
celery = Celery(__name__)

# Define task function
@celery.task(name='app.site_report_task')
def site_report_task():
    report_data = sleepy()
    # Do something with report_data, e.g. save to database