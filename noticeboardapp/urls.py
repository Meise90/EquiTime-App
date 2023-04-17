from django.urls import path

from . import views

app_name = 'noticeboardapp'

urlpatterns = [
    # C
    path('add-notice/', views.add_notice_view, name='add-notice-view'),

    # R
    path('noticeboard/', views.noticeboard_view, name='noticeboard-view'),

    # U
    path('<str:notice_title>/<int:notice_id>/update/', views.update_notice_view, name='update-notice-view'),

    # D
    path('<str:notice_title>/<int:notice_id>/delete/', views.delete_notice_view, name='delete-notice-view'),
    path('delete-notices/', views.delete_all_notices, name='delete-all-notices'),

]