from django.db import models

class MachineLearningModel(models.Model):
    id = models.CharField(max_length=32, unique=True, primary_key=True)  
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    
    name = models.CharField(max_length=100, unique=True)
    version = models.CharField(max_length=20, default='1.0')
    
    algorithm = models.CharField(max_length=100, blank=True, null=True)
    framework = models.CharField(max_length=50, blank=True, null=True)
    
    feature_names = models.JSONField(blank=True, null=True)
    feature_impacts = models.JSONField(blank=True, null=True)
    
    feature_maps = models.JSONField(blank=True, null=True)
    output_maps = models.JSONField(blank=True, null=True)
    
    hyperparameters = models.JSONField(blank=True, null=True)
    
    model_file_url = models.URLField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    accuracy = models.FloatField(blank=True, null=True)
    precision = models.FloatField(blank=True, null=True)
    recall = models.FloatField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')  

    class Meta:
        indexes = [
            models.Index(fields=['name', 'version']),
        ]
        ordering = ['-created_at']  

    def __str__(self):
        return f'{self.name} (v{self.version})'


class Prediction(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    model = models.ForeignKey(MachineLearningModel, on_delete=models.CASCADE, related_name="predictions")
    user = models.ForeignKey('services.User', on_delete=models.CASCADE, related_name="predictions")
    
    input_data = models.JSONField(null=True, blank=True)
    image_input = models.OneToOneField('ImageInput', on_delete=models.SET_NULL, null=True, blank=True)

    prediction = models.TextField()
    probability = models.FloatField(null=True, blank=True, default=0.0)  

    class Meta:
        indexes = [
            models.Index(fields=['user', 'created_at']),
        ]
        ordering = ['-created_at'] 

    def __str__(self):
        return f'Prediction by {self.user.get_full_name()} using {self.model.name} on {self.created_at}'


class ImageInput(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    image = models.ImageField(upload_to='predictions/') 
    
    def __str__(self):
        return f'Image uploaded at {self.created_at}'

    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
        ]
