import datetime
from api.transactions.models import transaction,UserDealSubscription
from apscheduler.schedulers.background import BackgroundScheduler


def BackgroundRunner():
    deals = UserDealSubscription.objects.all()
    for deal in deals:
        today = datetime.datetime.now()
        diff = deal.created_at - today
        print(diff.days)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(BackgroundRunner, 'interval', minutes=2)
    scheduler.start()