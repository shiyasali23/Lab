from rest_framework import serializers
from .models import User, Biometrics, BiometricsEntry, FoodScore
from adminpanel.serializers import BiochemicalSerializer, FoodSerializer
from adminpanel.models import Biochemical, Food
from django.contrib.auth import authenticate
from django.db import transaction
from django.utils import timezone

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
    biometrics = serializers.ListField(child=serializers.DictField(), write_only=True)

    class Meta:
        model = BiometricsEntry
        fields = ['id', 'user', 'health_score', 'created', 'biometrics']

    def create(self, validated_data):
        user = self.context['user']
        biometrics_data = validated_data.pop('biometrics')
        
        with transaction.atomic():
            biometrics_entry = BiometricsEntry.objects.create(user=user, **validated_data)
            
            for data in biometrics_data:
                biochemical = Biochemical.objects.get(id=data['biochemical_id'])
                Biometrics.objects.create(
                    biochemical=biochemical,
                    biometricsentry=biometrics_entry,
                    value=data['value']
                )
        
        self.update_health_score(biometrics_entry)
        return biometrics_entry
    
    def update_health_score(self, biometrics_entry):
        try:
            current_time = timezone.now()

            # Get distinct biochemicals across all biometrics for this user
            unique_biochemicals = (
                Biometrics.objects.filter(biometricsentry__user=biometrics_entry.user)
                .values('biochemical')
                .distinct()
            )

            total_score = 0

            for biochemical in unique_biochemicals:
                # Get the latest biometric entry for each biochemical for this user, considering only non-expired entries
                latest_biometric = (
                    Biometrics.objects.filter(
                        biochemical=biochemical['biochemical'],
                        biometricsentry__user=biometrics_entry.user,
                        expired_date__gt=current_time
                    )
                    .order_by('-created')
                    .first()
                )

                if latest_biometric:
                    total_score += latest_biometric.scaled_value

            biometrics_entry.health_score = total_score
            biometrics_entry.save()

        except Exception as e:
            print(e)


class BiometricsSerializer(serializers.ModelSerializer):
    biochemical_id = serializers.PrimaryKeyRelatedField(queryset=Biochemical.objects.all(), source='biochemical')
    biochemical = BiochemicalSerializer(read_only=True)

    class Meta:
        model = Biometrics
        fields = [
            'id', 'biochemical', 'biochemical_id', 'value',
            'scaled_value', 'expired_date', 'created'
        ]







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
