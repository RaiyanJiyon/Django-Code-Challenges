from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('features/', features, name='features'),
    path('pricing/', pricing, name='pricing'),
]
