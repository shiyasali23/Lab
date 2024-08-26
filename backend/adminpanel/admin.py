from django.contrib import admin
from .models import (
    Category, SubCategory, Condition, Biochemical, Food, Nutrient, 
    FoodNutrient, FoodWeight, NutrientWeight, BiochemicalCondition
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    ordering = ('name',)

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Biochemical)
class BiochemicalAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'female_min', 'female_max', 'male_min', 'male_max', 'unit', 'validity_days', 'created')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    ordering = ('name',)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'nutriscore', 'normalized_nutriscore', 'created')
    search_fields = ('name', 'subcategory__name')
    list_filter = ('subcategory',)
    ordering = ('name',)

@admin.register(Nutrient)
class NutrientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'unit', 'created')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    ordering = ('name',)

@admin.register(FoodNutrient)
class FoodNutrientAdmin(admin.ModelAdmin):
    list_display = ('food', 'nutrient', 'value', 'normalized_value')
    search_fields = ('food__name', 'nutrient__name')
    list_filter = ('food', 'nutrient')
    ordering = ('food__name', 'nutrient__name')

@admin.register(FoodWeight)
class FoodWeightAdmin(admin.ModelAdmin):
    list_display = ('biochemical', 'food', 'bias', 'weight', 'created')
    search_fields = ('biochemical__name', 'food__name')
    list_filter = ('biochemical', 'food')
    ordering = ('biochemical__name', 'food__name')

@admin.register(NutrientWeight)
class NutrientWeightAdmin(admin.ModelAdmin):
    list_display = ('biochemical', 'nutrient', 'bias', 'weight', 'created')
    search_fields = ('biochemical__name', 'nutrient__name')
    list_filter = ('biochemical', 'nutrient')
    ordering = ('biochemical__name', 'nutrient__name')

@admin.register(BiochemicalCondition)
class BiochemicalConditionAdmin(admin.ModelAdmin):
    list_display = ('biochemical', 'condition', 'is_hyper', 'created')
    search_fields = ('biochemical__name', 'condition__name')
    list_filter = ('biochemical', 'condition', 'is_hyper')
    ordering = ('biochemical__name', 'condition__name', 'is_hyper')
