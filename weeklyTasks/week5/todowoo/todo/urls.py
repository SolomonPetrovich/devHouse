from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('todolist/', todolist, name='todolist'),
    path('createtodo/', createToDo, name='createToDo'),
    path('todo/<int:pk>', toDoDetail, name='toDoDetail'),
    path('todo/<int:pk>/complete', toDoComlete, name='toDoComlete'),
    path('todo/<int:pk>/delete', toDoDelete, name='toDoDelete'),
    path('completedToDos', completed, name='completed')
]