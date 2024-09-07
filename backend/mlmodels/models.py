from django.db import models
from adminpanel.models import BaseModel


class MachineLearningModel(BaseModel):
    # Model Information
    name = models.CharField(max_length=100, unique=True)  
    version = models.CharField(max_length=20, default='1.0')  

    # Metadata
    algorithm = models.CharField(max_length=100)  
    framework = models.CharField(max_length=50)
    hyperparameters = models.JSONField(blank=True, null=True)  
    model_file_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    # Performance Metrics
    accuracy = models.FloatField(blank=True, null=True)  
    f1_score = models.FloatField(blank=True, null=True)  
    precision = models.FloatField(blank=True, null=True)  
    recall = models.FloatField(blank=True, null=True)  
    roc_auc = models.FloatField(blank=True, null=True)  

    # Model Status
    status = models.CharField(max_length=20, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')  

    class Meta:
        indexes = [
            models.Index(fields=['name', 'version']),
        ]

    def __str__(self):
        return f'{self.name} (v{self.version})'


class Prediction(BaseModel):
    model = models.ForeignKey(MachineLearningModel, on_delete=models.CASCADE)  
    user = models.ForeignKey('services.User', on_delete=models.CASCADE)  
    

    input_data = models.JSONField()
    image_input = models.OneToOneField('ImageInput', on_delete=models.CASCADE, null=True, blank=True)
  
    prediction_result = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)  


    status = models.CharField(max_length=20, choices=[('success', 'Success'), ('error', 'Error')], default='success')  
    error_message = models.TextField(blank=True, null=True)  

    class Meta:
        indexes = [
            models.Index(fields=['user', 'created_at']),
        ]

    def __str__(self):
        return f'Prediction by {self.user.get__full_name()} using {self.model.name} on {self.created_at}'

class ImageInput(BaseModel):
    image = models.ImageField(upload_to='predictions/', blank=True, null=True)  # Store the image file
    uploaded_at = models.DateTimeField(auto_now_add=True)  # When the image was uploaded

    def __str__(self):
        return f'ImageData {self.id} uploaded at {self.uploaded_at}'