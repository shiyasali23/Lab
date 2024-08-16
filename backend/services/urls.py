from django.urls import path
from .views import (
    signup, 
    login, 
    create_biometrics, 
    deactivate_user
)

urlpatterns = [
    # User authentication
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),

    # Biometrics
    path('biometrics/create/<int:pk>/', create_biometrics, name='create-biometrics'),

    # User management
    path('deactivate-user/<int:pk>/', deactivate_user, name='deactivate-user'),
    path('deactivate-user/', deactivate_user, name='deactivate-user-by-email'),
]
