from django.urls import path
from . import views

urlpatterns = [
    # User URLs
    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),

    # Biometrics URLs
    path('biometrics/', views.biometrics_list, name='biometrics-list'),
    path('biometrics/<int:pk>/', views.biometrics_detail, name='biometrics-detail'),

    # BiometricsEntry URLs
    path('biometrics-entries/', views.biometrics_entry_list, name='biometrics-entry-list'),
    path('biometrics-entries/<int:pk>/', views.biometrics_entry_detail, name='biometrics-entry-detail'),

    # BiometricsValue URLs
    path('biometrics-values/', views.biometrics_value_list, name='biometrics-value-list'),
    path('biometrics-values/<int:pk>/', views.biometrics_value_detail, name='biometrics-value-detail'),

    # FoodScore URLs
    path('foodscores/', views.foodscore_list, name='foodscore-list'),
    path('foodscores/<int:pk>/', views.foodscore_detail, name='foodscore-detail'),

    # Signup and Login URLs
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
