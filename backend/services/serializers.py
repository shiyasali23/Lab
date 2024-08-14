from rest_framework import serializers
from .models import User, Biometrics, BiometricsEntry, BiometricsValue, FoodScore
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

class BiometricsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

    class Meta:
        model = Biometrics
        fields = '__all__'

class BiometricsValueSerializer(serializers.ModelSerializer):
    biochemical = BiochemicalSerializer(read_only=True)
    biochemical_id = serializers.PrimaryKeyRelatedField(queryset=Biochemical.objects.all(), source='biochemical', write_only=True)

    class Meta:
        model = BiometricsValue
        exclude = ('biometrics_entry',)

class BiometricsEntrySerializer(serializers.ModelSerializer):
    biometrics = BiometricsSerializer(read_only=True)
    biometrics_id = serializers.PrimaryKeyRelatedField(queryset=Biometrics.objects.all(), source='biometrics', write_only=True)
    values = BiometricsValueSerializer(many=True)

    class Meta:
        model = BiometricsEntry
        fields = ['id', 'biometrics', 'biometrics_id', 'values']

    def create(self, validated_data):
        values_data = validated_data.pop('values')
        biometrics_entry = BiometricsEntry.objects.create(**validated_data)
        BiometricsValue.objects.bulk_create([
            BiometricsValue(biometrics_entry=biometrics_entry, **value_data)
            for value_data in values_data
        ])
        return biometrics_entry

class FoodScoreSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), source='food', write_only=True)

    class Meta:
        model = FoodScore
        fields = '__all__'
