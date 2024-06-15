from django.urls import path
from .views import ContactView
from django.views.generic import TemplateView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('success/', TemplateView.as_view(template_name = 'success.html'), name='success'),
]
