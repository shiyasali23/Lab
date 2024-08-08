from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Biometrics, FoodScore

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'gender')
    list_filter = ('gender', 'city', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'date_of_birth', 'gender')}),
        ('Address', {'fields': ('city', 'address')}),
        ('Additional info', {'fields': ('job', 'height', 'weight')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth', 'gender', 'is_staff', 'is_superuser'),
        }),
    )
@admin.register(Biometrics)
class BiometricsAdmin(admin.ModelAdmin):
    list_display = ('user', 'biochemical', 'value', 'scaled_value', 'created')
    list_filter = ('biochemical', 'created')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'biochemical__name')

@admin.register(FoodScore)
class FoodScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'score', 'created')
    list_filter = ('food', 'created')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'food__name')