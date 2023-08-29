from django.urls import path
from . import views

app_name = 'reminderapp'

urlpatterns = [

    # C
    path('add-event/', views.add_event_view, name='add-event-view'),

    # R
    path('events/', views.all_events_view, name='all-events-view'),
    path('<int:event_id>/event/', views.event_detail_view, name='event-detail-view'),

    # U
    path('<int:event_id>/event/update/', views.event_update_view, name='event-update-view'),

    # D
    path('<int:event_id>/event/delete/', views.event_delete_view, name='event-delete-view'),

    ]