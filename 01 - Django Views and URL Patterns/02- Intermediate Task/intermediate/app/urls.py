from django.urls import path
from .views import greet_user

urlpatterns = [
    path('greet/<str:username>/', greet_user, name='greet_user'),
]
