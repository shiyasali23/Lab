from django.urls import path
from .views import (
    signup, login, biometrics_list, biometrics_entry_list, 
    biometrics_entry_values, latest_food_scores, user_latest_food_score
)

urlpatterns = [
    # User authentication
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),

    # Biometrics
    path('biometrics/', biometrics_list, name='biometrics-list'),
    path('biometrics/<int:pk>/', biometrics_list, name='biometrics-detail'),

    # Biometrics Entries
    path('biometrics-entries/', biometrics_entry_list, name='biometrics-entry-list'),
    path('biometrics-entries/<int:pk>/', biometrics_entry_list, name='biometrics-entry-detail'),
    path('biometrics-entries/<int:pk>/values/', biometrics_entry_values, name='biometrics-entry-values'),

    # Biometrics Values
    path('biometrics-values/', biometrics_entry_list, name='biometrics-value-list'),
    path('biometrics-values/<int:pk>/', biometrics_entry_list, name='biometrics-value-detail'),

    # Food Scores
    path('foodscores/', latest_food_scores, name='foodscore-list'),
    path('foodscores/<int:pk>/', latest_food_scores, name='foodscore-detail'),
    path('foodscores/latest/', latest_food_scores, name='foodscore-latest'),
    path('foodscores/user-latest/', user_latest_food_score, name='foodscore-user-latest'),
]
