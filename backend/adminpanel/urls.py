from django.urls import path
from . import views

urlpatterns = [
    # Category URLs
    path('categories/', views.category_list, name='category-list'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),

    # SubCategory URLs
    path('subcategories/', views.subcategory_list, name='subcategory-list'),
    path('subcategories/<int:pk>/', views.subcategory_detail, name='subcategory-detail'),

    # Condition URLs
    path('conditions/', views.condition_list, name='condition-list'),
    path('conditions/<int:pk>/', views.condition_detail, name='condition-detail'),

    # Biochemical URLs
    path('biochemicals/', views.biochemical_list, name='biochemical-list'),
    path('biochemicals/<int:pk>/', views.biochemical_detail, name='biochemical-detail'),

    # Food URLs
    path('foods/', views.food_list, name='food-list'),
    path('foods/<int:pk>/', views.food_detail, name='food-detail'),

    # Nutrient URLs
    path('nutrients/', views.nutrient_list, name='nutrient-list'),
    path('nutrients/<int:pk>/', views.nutrient_detail, name='nutrient-detail'),
    
    # Food Nutrient URLs
    path('nutrients/', views.food_nutrient_list, name='food_nutrient-list'),
    path('nutrients/<int:pk>/', views.food_nutrient_detail, name='food_nutrient-detail'),

    # Weight URLs
    path('weights/', views.weight_list, name='weight-list'),
    path('weights/<int:pk>/', views.weight_detail, name='weight-detail'),
]
