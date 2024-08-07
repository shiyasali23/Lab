from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Biometrics, FoodScore, Biochemical, Food
from .serializers import UserSerializer, BiometricsSerializer, FoodScoreSerializer, BiochemicalSerializer, FoodSerializer

# User Views
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Biometrics Views
@api_view(['GET', 'POST'])
def biometrics_list(request):
    if request.method == 'GET':
        biometrics = Biometrics.objects.all()
        serializer = BiometricsSerializer(biometrics, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BiometricsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def biometrics_detail(request, pk):
    try:
        biometrics = Biometrics.objects.get(pk=pk)
    except Biometrics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BiometricsSerializer(biometrics)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BiometricsSerializer(biometrics, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        biometrics.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# FoodScore Views
@api_view(['GET', 'POST'])
def food_score_list(request):
    if request.method == 'GET':
        food_scores = FoodScore.objects.all()
        serializer = FoodScoreSerializer(food_scores, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FoodScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def food_score_detail(request, pk):
    try:
        food_score = FoodScore.objects.get(pk=pk)
    except FoodScore.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodScoreSerializer(food_score)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FoodScoreSerializer(food_score, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        food_score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Biochemical Views
@api_view(['GET', 'POST'])
def biochemical_list(request):
    if request.method == 'GET':
        biochemicals = Biochemical.objects.all()
        serializer = BiochemicalSerializer(biochemicals, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BiochemicalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def biochemical_detail(request, pk):
    try:
        biochemical = Biochemical.objects.get(pk=pk)
    except Biochemical.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BiochemicalSerializer(biochemical)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BiochemicalSerializer(biochemical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        biochemical.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Food Views
@api_view(['GET', 'POST'])
def food_list(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def food_detail(request, pk):
    try:
        food = Food.objects.get(pk=pk)
    except Food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodSerializer(food)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)