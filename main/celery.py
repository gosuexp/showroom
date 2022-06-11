import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

app = Celery("main")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'showroom_buy_car' : {
        'task': 'showroom.tasks.showroom_buy_car',
        'schedule': crontab(minute='*/3')
    },

    'customer_buy_car': {
        'task': 'showroom.tasks.customers_buy_cars',
        'schedule': crontab(minute='*/3')
    },

}
