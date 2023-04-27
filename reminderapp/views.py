from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import date, datetime, time
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from reminderapp.models import Event
from reminderapp.tasks import send_reminder_mail_func
from django.conf import settings
import json
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def add_event_view(request):

    if request.method == "GET":
        return render(
            request,
            'reminderapp/add_event.html'
        )

    if request.method == "POST":

        current_user = request.user
        event = request.POST.get('event')

        if event:
            Event.objects.create(event_name=event, user=current_user)

        return redirect('reminderapp:all-events-view')


@login_required
def all_events_view(request):

    events = Event.objects.all().order_by('event_date')
    today = date.today()
    current_day = today.strftime("%A")

    return render(
        request,
        'reminderapp/all_events.html',
        context={
            'events': events,
            'today': today,
            'current_day': current_day,
        }
    )


@login_required
def event_detail_view(request, event_id):

    event = Event.objects.get(id=event_id)

    name = event.event_name
    planned = event.event_date
    planned_at_time = event.event_time
    remind_on = event.reminder_date
    remind_at = event.reminder_time

    return render(
        request,
        'reminderapp/event_detail.html',
        context={
            'name': name,
            'planned': planned,
            'remind_on': remind_on,
            'remind_at': remind_at,
            'planned_at_time': planned_at_time,
        }
    )


@login_required
def event_update_view(request, event_id):

    event = Event.objects.get(id=event_id)
    user = request.user

    if request.method == "GET":

        name = event.event_name
        planned = event.event_date
        planned_at_time = event.event_time
        remind_on = event.reminder_date
        remind_at = event.reminder_time

        return render(
            request,
            'reminderapp/update_event.html',
            context={
                'name': name,
                'planned': planned,
                'planned_at_time': planned_at_time,
                'remind_on': remind_on,
                'remind_at': remind_at,
            }
        )

    if request.method == "POST":

        new_event = request.POST.get('event')
        new_date = request.POST.get('date')
        new_time = request.POST.get('event_time')
        new_reminder_date = request.POST.get('reminder_date')
        new_reminder_time = request.POST.get('reminder_time')


        if new_event:
            event.event_name = new_event
            event.save()

        if new_date:
            event.event_date = new_date
            event.save()

        if new_time:
            event.event_time = new_time
            event.save()

        if new_reminder_date:
            event.reminder_date = new_reminder_date
            event.save()

        if new_reminder_time:
            event.reminder_time = new_reminder_time
            event.save()


        dynamic_task_id = datetime.now()

        hour = int(event.reminder_time[0:2])
        minute = int(event.reminder_time[3:5])
        day = int(event.reminder_date[8:10])
        month = int(event.reminder_date[5:7])

        user_id = user.id

        schedule, created = CrontabSchedule.objects.get_or_create(hour=hour, minute=minute, day_of_month=day,
                                                                  month_of_year=month,
                                                                  timezone='Europe/Warsaw')
        task = PeriodicTask.objects.create(crontab=schedule, name=f"schedule_reminder_mail_task_{dynamic_task_id}",
                                           task='reminderapp.tasks.send_reminder_mail_func', one_off=True,
                                           args=json.dumps(([event_id, user_id])))

        name = event.event_name
        planned = event.event_date
        planned_at_time = event.event_time
        remind_on = event.reminder_date
        remind_at = event.reminder_time

        return render(
            request,
            'reminderapp/event_detail.html',
            context={
                'name': name,
                'planned': planned,
                'planned_at_time': planned_at_time,
                'remind_on': remind_on,
                'remind_at': remind_at,

            }
        )



@login_required
def event_delete_view(request, event_id):

    event = Event.objects.get(id=event_id)

    if request.method == "GET":
        return render(
            request,
            'reminderapp/delete_event.html',
            context={
                'event': event,
            }
        )

    if request.method == "POST":

        event.delete()
        return redirect('reminderapp:all-events-view')



