from celery import shared_task
from scheduleapp.models import Activity


@shared_task(bind=True)
def delete_all_func(self):

    activities = Activity.objects.all()
    if activities:
        activities.delete()

    return "Done"