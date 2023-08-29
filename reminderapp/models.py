from django.db import models

# Create your models here.


class Event(models.Model):

    user = models.CharField(max_length=50, default='Guest')
    event_name = models.CharField(max_length=100)
    event_date = models.CharField(max_length=50, default='2023-01-01')
    event_time = models.CharField(max_length=50, default='12:00')
    reminder_date = models.CharField(max_length=50, default='2023-01-01')
    reminder_time = models.CharField(max_length=50, default='12:00')


