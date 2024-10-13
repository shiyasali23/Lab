from rest_framework import serializers
from .models import Symptom


class SymptomsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Symptom
        fields = ['name']


