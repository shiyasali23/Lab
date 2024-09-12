from django.contrib import admin
from .models import MachineLearningModel, Prediction, ImageInput

@admin.register(MachineLearningModel)
class MachineLearningModelAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'version', 'algorithm', 'framework', 
        'accuracy', 'precision', 'recall', 'status', 
        'created_at', 'updated_at'
    )
    list_filter = ('algorithm', 'framework', 'status', 'created_at')
    search_fields = ('name', 'version', 'algorithm', 'framework')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        (None, {'fields': ('id', 'name', 'version')}),
        ('Model Details', {'fields': ('algorithm', 'framework', 'model_file_url', 'status')}),
        ('Performance', {'fields': ('accuracy', 'precision', 'recall')}),
        ('Features', {'fields': ('feature_names', 'feature_impacts', 'feature_maps', 'output_maps')}),
        ('Hyperparameters', {'fields': ('hyperparameters',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'model', 'created_at', 'prediction', 'probability')
    list_filter = ('created_at', 'model__name')
    search_fields = ('user__first_name', 'user__last_name', 'model__name', 'prediction', 'probability')
    ordering = ('-created_at',)
    raw_id_fields = ('user', 'model', 'image_input')
    autocomplete_fields = ('user', 'model')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {'fields': ('user', 'model', 'created_at')}),
        ('Input Data', {'fields': ('input_data', 'image_input')}),
        ('Prediction Result', {'fields': ('prediction', 'probability')}),
    )


@admin.register(ImageInput)
class ImageInputAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'image')
    list_filter = ('created_at',)
    search_fields = ('id',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {'fields': ('image',)}),
        ('Timestamps', {'fields': ('created_at',)}),
    )
