from django.db import models


# Create your models here.

class Notice(models.Model):

    title = models.CharField(max_length=50, default='Notice')
    user = models.CharField(max_length=50, default='Guest')
    content = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
