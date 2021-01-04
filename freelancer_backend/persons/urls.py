from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view(), name='users'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('profiles/', ProfileList.as_view(), name='profiles'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('experience_items/', ExperienceItemList.as_view(), name='experience_items'),
]
