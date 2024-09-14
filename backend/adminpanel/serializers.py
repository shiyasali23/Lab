from rest_framework import serializers
from .models import (
    Category, SubCategory, Condition, Biochemical, 
    BiochemicalCondition, Food,FoodImage, Nutrient, FoodNutrient, 
    FoodWeight, NutrientWeight
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class SubCategorySerializer(serializers.ModelSerializer):
    category= serializers.SerializerMethodField()  
    
    class Meta:
        model = SubCategory
        fields = ['name' 'category']
        
    def get_category(self, obj):
        return obj.category.name
        


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'


class BiochemicalSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )  

    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Biochemical
        fields = ['name', 'id', 'category_name','category_id']  


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
    subcategory = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Food
        fields = '__all__'

    def get_subcategory(self, obj):
        return obj.subcategory.name

class FoodImageSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(
        queryset=Food.objects.all(), source='food', write_only=True  
    )

    class Meta:
        model = FoodImage
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



