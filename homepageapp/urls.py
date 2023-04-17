from django.urls import path
from . import views

app_name = 'homepageapp'

urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('register/', views.register_view, name='register-view'),
    path('logout/', views.logout_view, name='logout-view'),
    path('signin/', views.login_view, name='login-view'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('index/', views.index_view, name='index-view'),

]