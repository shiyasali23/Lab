from django.urls import path
from . import views

urlpatterns = [
    # User URLs
    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),

    # Biometrics URLs
    path('biometrics/', views.biometrics_list, name='biometrics-list'),
    path('biometrics/<int:pk>/', views.biometrics_detail, name='biometrics-detail'),

    # FoodScore URLs
    path('foodscores/', views.foodscore_list, name='foodscore-list'),
    path('foodscores/<int:pk>/', views.foodscore_detail, name='foodscore-detail'),

    # Signup and Login URLs
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
