from django.urls import path
from .views import *

urlpatterns = [
    path('', all_blogs),
    path('<int:pk>', blog_detail, name='blog_detail')
]
