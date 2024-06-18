from django.urls import path
from .views import student_form, success_view

urlpatterns = [
    path('student/', student_form, name='student_form'),
    path('success/', success_view, name='success'),
]
