from django.urls import path
from . import views

urlpatterns = [
    path('cr/',views.credential, name='index'),  # Define your app-specific URL patterns here
    # Add more URL patterns as needed
]
