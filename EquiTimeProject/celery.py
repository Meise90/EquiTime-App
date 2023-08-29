from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EquiTimeProject.settings')

app = Celery('EquiTimeProject')
app.conf.enable_utc = False

app.conf.update(timezone='Europe/Warsaw')

app.config_from_object(settings, namespace='CELERY')

app.conf.broker_url = 'redis://localhost:6379/0'

app.conf.broker_transport_options = {'visibility_timeout': 3600}

# Celery Beat Settings

app.conf.beat_schedule = {
    'clear-schedule-every-week': {
        'task': 'scheduleapp.tasks.delete_all_func',
        'schedule': crontab(hour=2, minute=0, day_of_week=1),
    },
    'delete-inactive-users': {
        'task': 'homepageapp.tasks.delete_inactive_users_func',
        'schedule': timedelta(hours=1)
    },

}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')