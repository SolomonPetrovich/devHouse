from django.urls import include, path
from .views import *
import rest_framework

urlpatterns = [
    path('api/posts', PostList.as_view()),
    path('api/posts/<int:pk>', PostRetrieveDestroy.as_view()),
    path('api/posts/<int:pk>/vote', VoteCreate.as_view()), 
    path("api_auth/", include('rest_framework.urls'))
]