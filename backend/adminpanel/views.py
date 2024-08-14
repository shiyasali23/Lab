from .models import (
    Category, SubCategory, Biochemical, Condition, Food, Nutrient, 
    FoodNutrient, FoodWeight, NutrientWeight, BiochemicalCondition
)
from .serializers import (
    CategorySerializer, SubCategorySerializer, BiochemicalSerializer,
    ConditionSerializer, FoodSerializer, NutrientSerializer,
    FoodNutrientSerializer, FoodWeightSerializer, NutrientWeightSerializer,
    BiochemicalConditionSerializer
)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import logging

logger = logging.getLogger(__name__)

# Generic views for list and detail
def generic_list_view(request, model, serializer_class):
    if request.method == 'GET':
        objects = model.objects.all()
        serializer = serializer_class(objects, many=True)
        data = [{key: value for key, value in item.items() if key not in ('category','subcategory','created')} for item in serializer.data]
        return Response(data)
    
    elif request.method == 'POST':
        if isinstance(request.data, list):
            serializer = serializer_class(data=request.data, many=True)
        else:
            serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        logger.error(f"Error in POST request for {model.__name__}: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def generic_detail_view(request, model, serializer_class, pk):
    try:
        obj = model.objects.get(pk=pk)
    except model.DoesNotExist:
        error_msg = f"{model.__name__} with pk {pk} does not exist"
        logger.error(error_msg)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializer_class(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializer_class(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        logger.error(f"Error in PUT request for {model.__name__} with pk {pk}: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# API views for each model
@api_view(['GET', 'POST'])
def category_list(request):
    return generic_list_view(request, Category, CategorySerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    return generic_detail_view(request, Category, CategorySerializer, pk)

@api_view(['GET', 'POST'])
def subcategory_list(request):
    return generic_list_view(request, SubCategory, SubCategorySerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def subcategory_detail(request, pk):
    return generic_detail_view(request, SubCategory, SubCategorySerializer, pk)

@api_view(['GET', 'POST'])
def biochemical_list(request):
    return generic_list_view(request, Biochemical, BiochemicalSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def biochemical_detail(request, pk):
    return generic_detail_view(request, Biochemical, BiochemicalSerializer, pk)

@api_view(['GET', 'POST'])
def condition_list(request):
    return generic_list_view(request, Condition, ConditionSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def condition_detail(request, pk):
    return generic_detail_view(request, Condition, ConditionSerializer, pk)

@api_view(['GET', 'POST'])
def biochemical_condition_list(request):
    return generic_list_view(request, BiochemicalCondition, BiochemicalConditionSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def biochemical_condition_detail(request, pk):
    return generic_detail_view(request, BiochemicalCondition, BiochemicalConditionSerializer, pk)

@api_view(['GET', 'POST'])
def food_list(request):
    return generic_list_view(request, Food, FoodSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def food_detail(request, pk):
    return generic_detail_view(request, Food, FoodSerializer, pk)

@api_view(['GET', 'POST'])
def nutrient_list(request):
    return generic_list_view(request, Nutrient, NutrientSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def nutrient_detail(request, pk):
    return generic_detail_view(request, Nutrient, NutrientSerializer, pk)

@api_view(['GET', 'POST'])
def food_nutrient_list(request):
    return generic_list_view(request, FoodNutrient, FoodNutrientSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def food_nutrient_detail(request, pk):
    return generic_detail_view(request, FoodNutrient, FoodNutrientSerializer, pk)

@api_view(['GET', 'POST'])
def food_weight_list(request):
    return generic_list_view(request, FoodWeight, FoodWeightSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def food_weight_detail(request, pk):
    return generic_detail_view(request, FoodWeight, FoodWeightSerializer, pk)

@api_view(['GET', 'POST'])
def nutrient_weight_list(request):
    return generic_list_view(request, NutrientWeight, NutrientWeightSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def nutrient_weight_detail(request, pk):
    return generic_detail_view(request, NutrientWeight, NutrientWeightSerializer, pk)
