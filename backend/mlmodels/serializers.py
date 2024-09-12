from rest_framework import serializers
from .models import MachineLearningModel, Prediction

class MachineLearningModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineLearningModel
        fields = '__all__'
        
        
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(MachineLearningModelSerializer, self).__init__(*args, **kwargs)
        
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
  

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

class PredictionSerializer(serializers.ModelSerializer):
    accuracy = serializers.SerializerMethodField()  
    model_id = serializers.SerializerMethodField()  

    class Meta:
        model = Prediction
        fields = ('prediction', 'probability', 'accuracy','model_id', 'created_at') 

    def get_accuracy(self, obj):
        return obj.model.accuracy
    
    def get_model_id(self, obj):
        return obj.model.id

