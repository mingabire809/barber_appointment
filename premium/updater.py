from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Premium


def update_checking():
    if date.today() > Premium.expiry_date:
        Premium.isExpired = True
        Premium.isExpired.save()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_checking, 'interval', hours=24)
    scheduler.start()
