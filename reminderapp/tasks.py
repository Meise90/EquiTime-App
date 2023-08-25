from celery import shared_task
from django.core.mail import send_mail
from EquiTimeProject import settings
from django.contrib.auth.models import User
from .models import Event
from twilio.rest import Client
from homepageapp.models import PhoneModel


@shared_task(bind=True)
def send_reminder_mail_func(self, event_id, user_id):

    user = User.objects.get(id=user_id)
    event = Event.objects.get(id=event_id)

    mail_subject = f"Hi, this is your reminder on <{event.event_name}>"
    message = f"Hello {user},\n\n" \
              f"You have {event.event_name} on {event.event_date} at {event.event_time}!\n\n" \
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
    phone_number = PhoneModel.objects.get(user=user)

    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Hi {user}, you have '{event.event_name}' on {event.event_date} at {event.event_time}!",
        from_=settings.TWILIO_HOST_NUMBER,
        # Below should be 'phone_number' value taken from the db, but because I'm using free Twilio acc I cannot
        # send messages to any number, only registered ones. That's why it's hard-coded.
        to=settings.POLISH_TEST_NUMBER,

    )

    return "Done"
