from django.urls import path

from . import views

app_name = 'scheduleapp'

urlpatterns = [

    # C
    path('add/', views.schedule_create_view, name='schedule-create-view'),

    # R
    path('schedule/', views.schedule_full_view, name='schedule-full-view'),
    path('<int:activity_id>/', views.activity_detail_view, name='activity-detail-view'),

    # U
    path('<int:activity_id>/update/', views.activity_update_view, name='activity-update-view'),

    # D
    path('<int:activity_id>/delete/', views.activity_delete_view, name='activity-delete-view'),

    path('monday/', views.monday_view, name='monday-view'),

    path('tuesday/', views.tuesday_view, name='tuesday-view'),

    path('wednesday/', views.wednesday_view, name='wednesday-view'),

    path('thursday/', views.thursday_view, name='thursday-view'),

    path('friday/', views.friday_view, name='friday-view'),

    path('saturday/', views.saturday_view, name='saturday-view'),

    path('sunday/', views.sunday_view, name='sunday-view'),

    path('refresh/', views.delete_all_activities, name='delete-all-activities'),

]