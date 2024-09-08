from rest_framework import serializers
from .models import MachineLearningModel, Prediction, ImageInput

class MachineLearningModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineLearningModel
        fields = '__all__'  

class ImageInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageInput
        fields = '__all__'  

class PredictionSerializer(serializers.ModelSerializer):
    model = MachineLearningModelSerializer()
    image_input = ImageInputSerializer()

    class Meta:
        model = Prediction
        fields = '__all__'  


