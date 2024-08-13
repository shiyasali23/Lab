from rest_framework import serializers
from .models import User, Biometrics, BiometricsEntry, BiometricsValue, FoodScore
from adminpanel.serializers import BiochemicalSerializer, FoodSerializer
from adminpanel.models import Biochemical, Food
from django.db import transaction

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'city', 'address', 'job',
                  'date_of_birth', 'height', 'weight', 'gender', 'is_active', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user

class BiometricsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )

    class Meta:
        model = Biometrics
        fields = '__all__'

class BiometricsEntrySerializer(serializers.ModelSerializer):
    biometrics = BiometricsSerializer(read_only=True)
    biometrics_id = serializers.PrimaryKeyRelatedField(
        queryset=Biometrics.objects.all(), source='biometrics', write_only=True
    )
    values = serializers.SerializerMethodField()

    class Meta:
        model = BiometricsEntry
        fields = ['id', 'biometrics', 'biometrics_id', 'values']

    def get_values(self, obj):
        return BiometricsValueSerializer(obj.values.all(), many=True).data

    def validate(self, data):
        biochemical_ids = [value['biochemical_id'] for value in data['values']]
        if not Biochemical.objects.filter(id__in=biochemical_ids).count() == len(biochemical_ids):
            raise serializers.ValidationError('One or more Biochemical IDs are invalid.')
        return data

    def create(self, validated_data):
        values_data = validated_data.pop('values')
        biometrics_entry = BiometricsEntry.objects.create(**validated_data)

        # Create BiometricsValue instances
        values_to_create = []
        for value_data in values_data:
            biochemical_id = value_data.get('biochemical_id')
            try:
                Biochemical.objects.get(id=biochemical_id)
            except Biochemical.DoesNotExist:
                raise serializers.ValidationError(f'Biochemical with id {biochemical_id} does not exist.')

            values_to_create.append(BiometricsValue(
                biochemical_id=biochemical_id,
                value=value_data.get('value'),
                biometrics_entry=biometrics_entry
            ))

        try:
            with transaction.atomic():
                BiometricsValue.objects.bulk_create(values_to_create)
        except Exception as e:
            raise serializers.ValidationError(f"Error creating values: {str(e)}")

        return biometrics_entry

class BiometricsValueSerializer(serializers.ModelSerializer):
    biochemical = BiochemicalSerializer(read_only=True)
    biochemical_id = serializers.PrimaryKeyRelatedField(
        queryset=Biochemical.objects.all(), source='biochemical', write_only=True
    )
    biometrics_entry = BiometricsEntrySerializer(read_only=True)
    biometrics_entry_id = serializers.PrimaryKeyRelatedField(
        queryset=BiometricsEntry.objects.all(), source='biometrics_entry', write_only=True
    )

    class Meta:
        model = BiometricsValue
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
