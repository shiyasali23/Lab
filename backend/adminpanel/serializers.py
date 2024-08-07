from rest_framework import serializers
from .models import Category, SubCategory, Biochemical, Condition, Food, Nutrient,FoodNutrient, Weight


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
    hyper_conditions = ConditionSerializer(many=True, read_only=True)
    hypo_conditions = ConditionSerializer(many=True, read_only=True)

    class Meta:
        model = Biochemical
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(read_only=True)
    subcategory_id = serializers.PrimaryKeyRelatedField(
        queryset=SubCategory.objects.all(), source='subcategory', write_only=True
    )

    class Meta:
        model = Food
        fields = '__all__'


class NutrientSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    class Meta:
        model = Nutrient
        fields = '__all__'


class FoodNutrientSerializer(serializers.ModelSerializer):
    nutrient_name = serializers.SerializerMethodField()
    food_name = serializers.SerializerMethodField()

    class Meta:
        model = FoodNutrient
        fields = ['nutrient_name', 'food_name','value']  # Only include the fields you want

    def get_nutrient_name(self, obj):
        return obj.nutrient.name if obj.nutrient else None

    def get_food_name(self, obj):
        return obj.food.name if obj.food else None






class WeightSerializer(serializers.ModelSerializer):
    biochemical = BiochemicalSerializer(read_only=True)
    biochemical_id = serializers.PrimaryKeyRelatedField(
        queryset=Biochemical.objects.all(), source='biochemical', write_only=True
    )
    nutrient = NutrientSerializer(read_only=True)
    nutrient_id = serializers.PrimaryKeyRelatedField(
        queryset=Nutrient.objects.all(), source='nutrient', write_only=True
    )
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(
        queryset=Food.objects.all(), source='food', write_only=True
    )

    class Meta:
        model = Weight
        fields = '__all__'
