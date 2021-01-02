from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view(), name='users'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('profiles/', ProfileList.as_view(), name='profiles'),
]
