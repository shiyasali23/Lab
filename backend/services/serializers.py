from rest_framework import serializers
from .models import User, Biometrics, BiometricsValue, FoodScore
from adminpanel.serializers import BiochemicalSerializer, FoodSerializer
from adminpanel.models import Biochemical, Food

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'city', 'address', 'job',
                  'date_of_birth', 'height_cm', 'weight_kg', 'gender', 'is_active', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class BiometricsValueSerializer(serializers.ModelSerializer):
    biochemical = BiochemicalSerializer(read_only=True)
    biochemical_id = serializers.PrimaryKeyRelatedField(queryset=Biochemical.objects.all(), source='biochemical', write_only=True)
    biochemical_name = serializers.CharField(source='biochemical.name', read_only=True)


    class Meta:
        model = BiometricsValue
        fields = ['biochemical_name','biochemical_id', 'value', 'scaled_value', 'biometrics', 'expired_date']



class BiometricsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Biometrics
        fields = '__all__'
        
    def create(self, validated_data):
        values_data = validated_data.pop('values', [])
        user = validated_data.pop('user', None)
        biometrics = Biometrics.objects.create(user=user, **validated_data)
        if values_data:
            for value_data in values_data:
                BiometricsValue.objects.create(biometrics=biometrics, **value_data)

        return biometrics


class FoodScoreSerializer(serializers.ModelSerializer):
    biometrics = BiometricsSerializer(read_only=True)
    biometrics_id = serializers.PrimaryKeyRelatedField(queryset=Biometrics.objects.all(), source='biometrics', write_only=True)
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), source='food', write_only=True)

    class Meta:
        model = FoodScore
        fields = '__all__'
