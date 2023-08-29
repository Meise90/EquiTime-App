from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from scheduleapp.models import Activity
from django.http import JsonResponse
from datetime import date, datetime
from django.contrib.auth.decorators import login_required




# Create your views here.


@login_required
def schedule_create_view(request):

    if request.method == "GET":
        return render(
            request,
            'scheduleapp/add.html'
        )

    if request.method == "POST":

        activity = request.POST.get('activity')
        current_user = request.user

        if activity:
            Activity.objects.create(content=activity, user=current_user)

            return redirect('scheduleapp:schedule-full-view')

        return render(
            request,
            'scheduleapp/full_schedule.html'
        )


@login_required
def schedule_full_view(request):

    monday_activities = Activity.objects.filter(week_day='monday')
    tuesday_activities = Activity.objects.filter(week_day='tuesday')
    weds_activities = Activity.objects.filter(week_day='wednesday')
    thursday_activities = Activity.objects.filter(week_day='thursday')
    friday_activities = Activity.objects.filter(week_day='friday')
    saturday_activities = Activity.objects.filter(week_day='saturday')
    sunday_activities = Activity.objects.filter(week_day='sunday')
    today = date.today()
    current_day = today.strftime("%A")


    if request.user.is_authenticated:

        return render(
            request,
            'scheduleapp/full_schedule.html',
            context={
                'monday_activities': monday_activities,
                'tuesday_activities': tuesday_activities,
                'weds_activities': weds_activities,
                'thursday_activities': thursday_activities,
                'friday_activities': friday_activities,
                'saturday_activities': saturday_activities,
                'sunday_activities': sunday_activities,
                'today': today,
                'current_day': current_day,

            }
        )

    else:
        return redirect('homepageapp:login-view')


@login_required
def activity_detail_view(request, activity_id):

    activity = Activity.objects.get(id=activity_id)

    return render(
        request,
        'scheduleapp/activity.html',
        context={
            'activity': activity,
        }
    )


@login_required
def activity_update_view(request, activity_id):

    activity = Activity.objects.get(id=activity_id)

    if request.method == "GET":
        return render(
            request,
            'scheduleapp/update_activity.html',
            context={
                'activity': activity,
            }
        )

    if request.method == "POST":
        new_activity = request.POST.get('activity')

        if new_activity:
            activity.content = new_activity
            activity.save()

        return redirect('scheduleapp:schedule-full-view')



@login_required
def activity_delete_view(request, activity_id):

    activity = Activity.objects.get(id=activity_id)


    if request.method == "GET":
        return render(
            request,
            'scheduleapp/delete_activity.html',
            context={
                'activity': activity,
            }
        )

    if request.method == "POST":
        activity.delete()
        return redirect('scheduleapp:schedule-full-view')




@login_required
def monday_view(request):

    if request.method == "POST":

        monday_activity = request.POST.get('monday')
        current_user = request.user

        if monday_activity:
            Activity.objects.create(content=monday_activity, week_day='monday', user=current_user)

            return redirect('scheduleapp:schedule-full-view')

        return render(
            request,
            'scheduleapp/monday.html')

    if request.method == "GET":

        monday_activities = Activity.objects.filter(week_day='monday')

        return render(
            request,
            'scheduleapp/monday.html',
            context={
                'monday_activities': monday_activities
            }
        )


@login_required
def tuesday_view(request):

    if request.method == "POST":

        tuesday_activity = request.POST.get('tuesday')
        current_user = request.user

        if tuesday_activity:
            Activity.objects.create(content=tuesday_activity, week_day='tuesday', user=current_user)

            return redirect('scheduleapp:schedule-full-view')

        return render(
            request,
            'scheduleapp/tuesday.html')

    if request.method == "GET":

        tuesday_activities = Activity.objects.filter(week_day='tuesday')

        return render(
            request,
            'scheduleapp/tuesday.html',
            context={
                'tuesday_activities': tuesday_activities,
            }
        )


@login_required
def wednesday_view(request):

    if request.method == "POST":

        weds_activity = request.POST.get('wednesday')
        current_user = request.user

        if weds_activity:
            Activity.objects.create(content=weds_activity, week_day='wednesday', user=current_user)

            return redirect('scheduleapp:schedule-full-view')

        return render(
            request,
            'scheduleapp/wednesday.html')

    if request.method == "GET":

        weds_activities = Activity.objects.filter(week_day='wednesday')

        return render(
            request,
            'scheduleapp/wednesday.html',
            context={
                'weds_activities': weds_activities,
            }
        )


@login_required
def thursday_view(request):

    if request.method == "POST":

        thursday_activity = request.POST.get('thursday')
        current_user = request.user

        if thursday_activity:
            Activity.objects.create(content=thursday_activity, week_day='thursday', user=current_user)

            return redirect('scheduleapp:schedule-full-view')

        return render(
            request,
            'scheduleapp/thursday.html')

    if request.method == "GET":

        thursday_activities = Activity.objects.filter(week_day='thursday')

        return render(
            request,
            'scheduleapp/thursday.html',
            context={
                'thursday_activities': thursday_activities,
            }
        )


@login_required
def friday_view(request):

    if request.method == "POST":

        friday_activity = request.POST.get('friday')
        current_user = request.user

        if friday_activity:
            Activity.objects.create(content=friday_activity, week_day='friday', user=current_user)

            return redirect('scheduleapp:schedule-full-view')

        return render(
            request,
            'scheduleapp/friday.html')

    if request.method == "GET":

        friday_activities = Activity.objects.filter(week_day='friday')

        return render(
            request,
            'scheduleapp/friday.html',
            context={
                'friday_activities': friday_activities,
            }
        )


@login_required
def saturday_view(request):

    if request.method == "POST":

        saturday_activity = request.POST.get('saturday')
        current_user = request.user

        if saturday_activity:
            Activity.objects.create(content=saturday_activity, week_day='saturday', user=current_user)

            return redirect('scheduleapp:schedule-full-view')

        return render(
            request,
            'scheduleapp/saturday.html')

    if request.method == "GET":

        saturday_activities = Activity.objects.filter(week_day='saturday')

        return render(
            request,
            'scheduleapp/saturday.html',
            context={
                'saturday_activities': saturday_activities,
            }
        )


@login_required
def sunday_view(request):

    if request.method == "POST":

        sunday_activity = request.POST.get('sunday')
        current_user = request.user

        if sunday_activity:
            Activity.objects.create(content=sunday_activity, week_day='sunday', user=current_user)

            return redirect('scheduleapp:schedule-full-view')

        return render(
            request,
            'scheduleapp/sunday.html')

    if request.method == "GET":

        sunday_activities = Activity.objects.filter(week_day='sunday')

        return render(
            request,
            'scheduleapp/sunday.html',
            context={
                'sunday_activities': sunday_activities,
            }
        )


@login_required
def delete_all_activities(request):

    activities = Activity.objects.all()

    if request.method == "POST":
        if activities and request.user.is_staff:
            activities.delete()

            return redirect('scheduleapp:schedule-full-view')

        else:
            return render(
                request,
                'scheduleapp/no_permission.html'
            )


    if request.method == "GET":
        return render(
            request,
            'scheduleapp/delete_all.html',
        )


@login_required
def current_date_view(request):

    current_date = datetime.now()
    current_day = current_date.strftime("%A")

    if request.method == "GET":

        return render(
            request,
            'scheduleapp/full_schedule.html',
            context={
                'current_date': current_date,
                'current_day': current_day,
            }
        )