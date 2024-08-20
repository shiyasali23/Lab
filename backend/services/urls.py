from django.urls import path
from .views import (
    signup, 
    login, 
    create_biometrics, 
    deactivate_user,
    get_user,
    update_user,
    logout
)

urlpatterns = [
    # User authentication
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

        # User management
    path('user/', get_user, name='get-user'),
    path('user/deactivate/', deactivate_user, name='deactivate-user'),
    path('user/update/', update_user, name='update-user'),
    
    # Biometrics
    path('biometrics/create/', create_biometrics, name='create-biometrics'),  # Changed to POST without pk
    
]
