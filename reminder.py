from studentcompanion import db
from studentcompanion.models import Reminders
from twilio.rest import Client
from datetime import datetime
import threading
import time
from pytz import timezone
from apscheduler.schedulers.background import BlockingScheduler


acc_id = 'ACf9044fa61f64f76cca22bbc4c1ad1149'
acc_auth = '67ef5894683185e6d9d4addfdeb1cc62'
client = Client(acc_id,acc_auth)


def send_reminder(body,to):
    from_num = 'whatsapp:+14155238886'
    to_num = 'whatsapp:+91'+to
    body = '*Your Reminder:* '+body
    client.messages.create(body=body,from_=from_num,to=to_num)


tz = timezone('Asia/Kolkata')

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron',minute='0-59',timezone=tz)
def get_reminders():
        items = Reminders.query.filter_by(date_time=str(datetime.now())[:16])
        if items:
            for item in items:
                threading.Thread(target=send_reminder,args=(item.event,item.number)).start()
                db.session.delete(item)
                db.session.commit()

scheduler.start()
