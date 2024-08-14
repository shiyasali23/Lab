from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Biometrics, BiometricsEntry, BiometricsValue, FoodScore

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'gender', 'is_active', 'is_staff')
    list_filter = ('gender', 'city', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'date_of_birth', 'gender')}),
        ('Address', {'fields': ('city', 'address')}),
        ('Additional info', {'fields': ('job', 'height_cm', 'weight_kg')}),
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
    list_display = ('user', 'created')
    list_filter = ('created',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name')

@admin.register(BiometricsEntry)
class BiometricsEntryAdmin(admin.ModelAdmin):
    list_display = ('biometrics', 'created')
    list_filter = ('created',)
    search_fields = ('biometrics__user__email', 'biometrics__user__first_name', 'biometrics__user__last_name')

@admin.register(BiometricsValue)
class BiometricsValueAdmin(admin.ModelAdmin):
    list_display = ('biochemical', 'value', 'scaled_value', 'biometrics_entry', 'created')
    list_filter = ('biochemical', 'created')
    search_fields = ('biochemical__name', 'biometrics_entry__biometrics__user__email', 'biometrics_entry__biometrics__user__first_name', 'biometrics_entry__biometrics__user__last_name')

@admin.register(FoodScore)
class FoodScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'score', 'created')
    list_filter = ('food', 'created')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'food__name')
