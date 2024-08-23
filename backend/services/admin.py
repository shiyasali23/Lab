from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Biometrics, BiometricsEntry, FoodScore

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'gender', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('gender', 'city', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number', 'city')
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

@admin.register(BiometricsEntry)
class BiometricsEntryAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'health_score', 'created')
    list_filter = ('created', 'user__gender')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__phone_number')
    ordering = ('-created',)

@admin.register(Biometrics)
class BiometricsAdmin(admin.ModelAdmin):
    list_display = ('get_user_full_name', 'biochemical', 'value', 'scaled_value', 'expired_date', 'created')
    list_filter = ('biochemical', 'created', 'biometricsentry__user__gender')
    search_fields = ('biometricsentry__user__email', 'biometricsentry__user__first_name', 'biometricsentry__user__last_name', 'biochemical__name')
    ordering = ('-created',)
    raw_id_fields = ('biometricsentry', 'biochemical')  
    autocomplete_fields = ['biometricsentry', 'biochemical']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('biometricsentry__user', 'biochemical')

    def get_user_full_name(self, obj):
        return obj.biometricsentry.user.get_full_name()
    get_user_full_name.admin_order_field = 'biometricsentry__user__last_name'  
    get_user_full_name.short_description = 'User'

@admin.register(FoodScore)
class FoodScoreAdmin(admin.ModelAdmin):
    list_display = ('get_user_full_name', 'food', 'score', 'created')
    list_filter = ('food', 'created')
    search_fields = ('biometricsentry__user__first_name', 'biometricsentry__user__last_name', 'food__name')
    ordering = ('-created',)
    raw_id_fields = ('biometricsentry', 'food')  
    autocomplete_fields = ['biometricsentry', 'food']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('biometricsentry__user', 'food')

    def get_user_full_name(self, obj):
        return obj.biometricsentry.user.get_full_name()
    get_user_full_name.admin_order_field = 'biometricsentry__user__last_name'  
    get_user_full_name.short_description = 'User'
