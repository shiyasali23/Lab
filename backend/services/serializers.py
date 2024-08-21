from rest_framework import serializers
from .models import User, Biometrics, FoodScore, FoodRecommendation
from adminpanel.serializers import BiochemicalSerializer, FoodSerializer
from adminpanel.models import Biochemical, Food

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'phone_number', 'city', 'address',
            'job', 'date_of_birth', 'height_cm', 'weight_kg', 'gender', 'is_active', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}


class BiometricsSerializer(serializers.ModelSerializer):
    biochemical = BiochemicalSerializer(read_only=True)
    biochemical_id = serializers.PrimaryKeyRelatedField(queryset=Biochemical.objects.all(), source='biochemical', write_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

    class Meta:
        model = Biometrics
        fields = [
            'id', 'biochemical', 'biochemical_id', 'user', 'user_id', 'value', 
            'scaled_value', 'expired_date', 'created'
        ]


class FoodRecommendationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

    class Meta:
        model = FoodRecommendation
        fields = '__all__'


class FoodScoreSerializer(serializers.ModelSerializer):
    food_recommendation = FoodRecommendationSerializer(read_only=True)
    food_recommendation_id = serializers.PrimaryKeyRelatedField(queryset=FoodRecommendation.objects.all(), source='food_recommendation', write_only=True)
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), source='food', write_only=True)

    class Meta:
        model = FoodScore
        fields = '__all__'
