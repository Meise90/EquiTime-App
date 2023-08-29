from django.urls import path
from . import views

app_name = 'competitionapp'

urlpatterns = [
    # R
    path("current-competitions-in-Poland/", views.current_competitions_view, name="current-competitions-view")

]