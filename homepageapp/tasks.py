from celery import shared_task
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


@shared_task(bind=True)
def delete_inactive_users_func(self):

    current_time = timezone.now()
    users = User.objects.all()
    for user in users:
        if user.is_active is False and current_time - datetime.timedelta(days=1) > user.date_joined:
            user.delete()

    return "Done"


