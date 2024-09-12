from django.urls import path
from .views import register_model, models_list, get_prediction

urlpatterns = [
    path('register_model/', register_model, name='register_model'),
    path('models_list/', models_list, name='models_list'),
    path('predict/', get_prediction, name='models_list'),
]
