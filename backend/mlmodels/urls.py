from django.urls import path
from .views import register_model

urlpatterns = [
    path('register_model/', register_model, name='register_model'),
]
