from django.shortcuts import render, redirect
from datetime import date, datetime
from noticeboardapp.models import Notice
from django.contrib.auth.decorators import login_required



# Create your views here.


@login_required
def add_notice_view(request):


    if request.method == "GET":

        today = date.today()
        current_day = today.strftime("%A")

        return render(
            request,
            'noticeboard/add_notice.html',
            context={
                'today': today,
                'current_day': current_day,
            }
        )

    if request.method == "POST":

        title = request.POST.get('title')
        notice = request.POST.get('notice')
        current_user = request.user
        timestamp = datetime.now()

        if notice:
            Notice.objects.create(content=notice, timestamp=timestamp, title=title, user=current_user)

            notices = Notice.objects.all().order_by('-timestamp')
            today = date.today()
            current_day = today.strftime("%A")

            return render(
                request,
                'noticeboard/board.html',
                context={
                    'notices': notices,
                    'today': today,
                    'current_day': current_day,
                    'current_user': current_user,
                }
            )

        return redirect('noticeboardapp:noticeboard-view')


@login_required
def noticeboard_view(request):

    notices = Notice.objects.all().order_by('-timestamp')
    current_user = request.user
    today = date.today()
    current_day = today.strftime("%A")

    if request.method == "GET":

        if request.user.is_authenticated:

            return render(
                request,
                'noticeboard/board.html',
                context={
                    'notices': notices,
                    'today': today,
                    'current_day': current_day,
                    'current_user': current_user,
                }
            )

        else:
            return redirect('homepageapp:login-view')



@login_required
def update_notice_view(request, notice_title, notice_id):

    notice = Notice.objects.get(title=notice_title, id=notice_id)

    if request.method == "GET":
        return render(
            request,
            'noticeboard/update_notice.html',
            context={
                'notice': notice,
            }
        )

    if request.method == "POST":
        new_notice_title = request.POST.get('title')
        new_notice_content = request.POST.get('content')

        if new_notice_title:
            notice.title = new_notice_title
            notice.save()

        if new_notice_content:
            notice.content = new_notice_content
            notice.save()

        return redirect('noticeboardapp:noticeboard-view')


@login_required
def delete_notice_view(request, notice_title, notice_id):

    notice = Notice.objects.get(title=notice_title, id=notice_id)

    if request.method == "GET":

        return render(
            request,
            'noticeboard/delete_notice.html',
            context={
                'notice': notice,
            }
        )

    if request.method == "POST":
        notice.delete()

        return redirect('noticeboardapp:noticeboard-view')


@login_required
def delete_all_notices(request):

    notices = Notice.objects.all()

    if request.method == "POST":
        if notices and request.user.is_staff:
            notices.delete()
        else:
            return render(
                request,
                'noticeboard/no_permission_to_delete_all_notices.html',
            )

        return redirect('noticeboardapp:noticeboard-view')



    if request.method == "GET":
        return render(
            request,
            'noticeboard/delete_all_notices.html',
        )

