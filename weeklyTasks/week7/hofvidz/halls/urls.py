from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    
    path("login", LoginView.as_view(), name='login'),
    path("logout", LogoutView.as_view(), name="logout"),
    path("signup", SignUp.as_view(), name="signup"),

    path("halloffame/create", CreateHall.as_view(), name="create_hall"),

]