from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path("todos/", ToDoListCreate.as_view()),
    path("todos/<int:pk>", ToDoRetrieveUpdateDestroyAPIView.as_view()),
    path("todos/<int:pk>/complete", ToDoComplete.as_view()),
    path("todos/completed", ToDoCompletedList.as_view()),

    path("signup/", signup),
    path("login/", login)
]