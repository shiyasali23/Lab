from rest_framework import serializers
from .models import User, Biometrics, BiometricsEntry, FoodScore
from adminpanel.serializers import BiochemicalSerializer, FoodSerializer
from adminpanel.models import Biochemical, Food
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'phone_number', 'city', 'address',
            'job', 'date_of_birth', 'height_cm', 'weight_kg', 'gender', 'is_active', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
        



class BiometricsEntrySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

    class Meta:
        model = BiometricsEntry
        fields = [
            'id', 'user', 'user_id', 'health_score', 'created'
        ]

class BiometricsSerializer(serializers.ModelSerializer):
    biochemical = BiochemicalSerializer(read_only=True)
    biochemical_id = serializers.PrimaryKeyRelatedField(queryset=Biochemical.objects.all(), source='biochemical', write_only=True)
    biometricsentry = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Biometrics
        fields = [
            'id', 'biochemical', 'biochemical_id', 'biometricsentry', 'value',
            'scaled_value', 'expired_date', 'created'
        ]
        read_only_fields = ['scaled_value', 'created']

    def create(self, validated_data):
        user = self.context['user']
        biometrics_entry, created = BiometricsEntry.objects.get_or_create(user=user)
        biometrics = Biometrics.objects.create(biometricsentry=biometrics_entry, **validated_data)
        return biometrics


class FoodScoreSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), source='food', write_only=True)
    biometricsentry = BiometricsEntrySerializer(read_only=True)
    biometricsentry_id = serializers.PrimaryKeyRelatedField(queryset=BiometricsEntry.objects.all(), source='biometricsentry', write_only=True)

    class Meta:
        model = FoodScore
        fields = [
            'id', 'biometricsentry', 'biometricsentry_id', 'food', 'food_id', 'score', 'created'
        ]
        read_only_fields = ['created']
