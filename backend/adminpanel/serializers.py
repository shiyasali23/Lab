from rest_framework import serializers
from .models import (
    Category, SubCategory, Condition, Biochemical, 
    BiochemicalCondition, Food, Nutrient, FoodNutrient, 
    FoodWeight, NutrientWeight
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = SubCategory
        fields = '__all__'


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'


class BiochemicalSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Biochemical
        fields = '__all__'


class BiochemicalConditionSerializer(serializers.ModelSerializer):
    biochemical = BiochemicalSerializer(read_only=True)
    biochemical_id = serializers.PrimaryKeyRelatedField(
        queryset=Biochemical.objects.all(), source='biochemical', write_only=True
    )
    condition = ConditionSerializer(read_only=True)
    condition_id = serializers.PrimaryKeyRelatedField(
        queryset=Condition.objects.all(), source='condition', write_only=True
    )

    class Meta:
        model = BiochemicalCondition
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(read_only=True)
    subcategory_id = serializers.PrimaryKeyRelatedField(
        queryset=SubCategory.objects.all(), source='subcategory', write_only=True
    )

    class Meta:
        model = Food
        fields = '__all__'


class FoodWeightSerializer(serializers.ModelSerializer):
    biochemical = BiochemicalSerializer(read_only=True)
    biochemical_id = serializers.PrimaryKeyRelatedField(
        queryset=Biochemical.objects.all(), source='biochemical', write_only=True
    )
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(
        queryset=Food.objects.all(), source='food', write_only=True
    )

    class Meta:
        model = FoodWeight
        fields = '__all__'



class NutrientSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Nutrient
        fields = '__all__'
        

class NutrientWeightSerializer(serializers.ModelSerializer):
    biochemical = BiochemicalSerializer(read_only=True)
    biochemical_id = serializers.PrimaryKeyRelatedField(
        queryset=Biochemical.objects.all(), source='biochemical', write_only=True
    )
    nutrient = NutrientSerializer(read_only=True)
    nutrient_id = serializers.PrimaryKeyRelatedField(
        queryset=Nutrient.objects.all(), source='nutrient', write_only=True
    )

    class Meta:
        model = NutrientWeight
        fields = '__all__'


class FoodNutrientSerializer(serializers.ModelSerializer):
    nutrient = NutrientSerializer(read_only=True)
    nutrient_id = serializers.PrimaryKeyRelatedField(
        queryset=Nutrient.objects.all(), source='nutrient', write_only=True
    )
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(
        queryset=Food.objects.all(), source='food', write_only=True
    )

    class Meta:
        model = FoodNutrient
        fields = '__all__'



