from rest_framework import serializers
from .models import MachineLearningModel

class MachineLearningModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineLearningModel
        fields = '__all__'  

    def create(self, validated_data):
        name = validated_data.get('name')
        version = validated_data.get('version')
        id = validated_data.get('id')

        model_instance = MachineLearningModel.objects.filter(name=name, version=version, id=id).first()

        if model_instance:
            return model_instance
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
