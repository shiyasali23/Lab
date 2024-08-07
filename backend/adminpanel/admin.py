from django.contrib import admin
from .models import Category, SubCategory, Condition, Biochemical, Food, Nutrient, FoodNutrient, Weight

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
    list_display = ('name', 'category', 'female_min', 'female_max', 'male_min', 'male_max', 'created')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    ordering = ('name',)
    filter_horizontal = ('hyper_conditions', 'hypo_conditions')

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'created')
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
    list_display = ('food', 'nutrient', 'value')
    search_fields = ('food__name', 'nutrient__name')
    list_filter = ('food', 'nutrient')
    ordering = ('food', 'nutrient')

@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display = ('weight', 'biochemical', 'nutrient', 'food', 'created')
    search_fields = ('biochemical__name', 'nutrient__name', 'food__name')
    list_filter = ('biochemical', 'nutrient', 'food')
    ordering = ('weight',)
