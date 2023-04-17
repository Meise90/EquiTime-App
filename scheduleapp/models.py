from django.db import models


# Create your models here.
class Activity(models.Model):

    content = models.CharField(max_length=500)
    week_day = models.CharField(max_length=25)
    user = models.CharField(max_length=50, default='Guest')


