from django.db import models

from adminpanel.models import BaseModel, Category



class Desease(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    discription = models.TextField(blank=True, null=True)    
    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

class Symptom(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='symptoms')    
    class Meta:
        indexes = [
            models.Index(fields=['name','category']),
        ]

    def __str__(self):
        return self.name
    
class Medication(BaseModel):
    name = models.CharField(max_length=255, unique=True)    
    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

class Precaution(BaseModel):
    name = models.CharField(max_length=255, unique=True)    
    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class Diet(BaseModel):
    name = models.CharField(max_length=255, unique=True)    
    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name






