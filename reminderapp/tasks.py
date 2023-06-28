from celery import shared_task
from django.core.mail import send_mail
from EquiTimeProject import settings
from django.contrib.auth.models import User
from reminderapp.models import Event
from twilio.rest import Client
import os


@shared_task(bind=True)
def send_reminder_mail_func(self, event_id, user_id):

    event = Event.objects.get(id=event_id)
    user = User.objects.get(id=user_id)

    mail_subject = f"Hi, this is your reminder on <{event.event_name}>"
    message = f"Hello {user},\n\n" \
              f"You have <{event.event_name}> on {event.event_date} at {event.event_time}!\n\n" \
              f"Sent from your EquiTime App."
    to_email = user.email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )

    return "Done"


@shared_task(bind=True)
def send_reminder_sms_func(self, event_id, user_id):

    event = Event.objects.get(id=event_id)
    user = User.objects.get(id=user_id)

    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Hi {user}, you have '{event.event_name}' on {event.event_date} at {event.event_time}!",
        from_=os.environ.get("TWILIO_HOST_NUMBER"),
        to=os.environ.get("POLISH_TEST_NUMBER"),

    )

    return "Done"
