from django.urls import path
from . import views

urlpatterns = [
    # Users 
    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
    
    # Biometrics
    path('biometrics/', views.biometrics_list, name='biometrics-list'),
    path('biometrics/<int:pk>/', views.biometrics_detail, name='biometrics-detail'),
    
    # Food Scores
    path('food-scores/', views.food_score_list, name='food-score-list'),
    path('food-scores/<int:pk>/', views.food_score_detail, name='food-score-detail'),
    
    # Biochemicals
    path('biochemicals/', views.biochemical_list, name='biochemical-list'),
    path('biochemicals/<int:pk>/', views.biochemical_detail, name='biochemical-detail'),
    
    # Foods
    path('foods/', views.food_list, name='food-list'),
    path('foods/<int:pk>/', views.food_detail, name='food-detail'),
]
