from rest_framework import serializers
from .models import User, Biometrics, FoodScore
from adminpanel.serializers import BiochemicalSerializer, FoodSerializer
from adminpanel.models import Biochemical, Food

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'city', 'address', 'job', 
                  'date_of_birth', 'height', 'weight', 'gender', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user




class BiometricsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    biochemical = BiochemicalSerializer(read_only=True)
    biochemical_id = serializers.PrimaryKeyRelatedField(
        queryset=Biochemical.objects.all(), source='biochemical', write_only=True
    )

    class Meta:
        model = Biometrics
        fields = '__all__'

class FoodScoreSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(
        queryset=Food.objects.all(), source='food', write_only=True
    )

    class Meta:
        model = FoodScore
        fields = '__all__'