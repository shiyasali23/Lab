from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max
import logging

from .models import User, Biometrics, BiometricsEntry, BiometricsValue, FoodScore
from .serializers import (
    UserSerializer, BiometricsSerializer, BiometricsEntrySerializer, 
    BiometricsValueSerializer, FoodScoreSerializer
)

logger = logging.getLogger(__name__)

def handle_exception(exc):
    """
    Handle exceptions and return appropriate responses.
    """
    if isinstance(exc, ObjectDoesNotExist):
        return Response({'error': str(exc)}, status=status.HTTP_404_NOT_FOUND)
    logger.error(f"Unhandled error: {str(exc)}", exc_info=True)
    return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def get_serializer_and_validate(serializer_class, data):
    """
    Create a serializer instance, validate data, and return serializer or errors.
    """
    serializer = serializer_class(data=data)
    if serializer.is_valid():
        return serializer, None
    return None, serializer.errors

@api_view(['POST'])
def signup(request):
    serializer, errors = get_serializer_and_validate(UserSerializer, request.data)
    if serializer:
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)
    if user and user.is_active:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data
        })
    return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'POST'])
def biometrics_list(request):
    if request.method == 'GET':
        biometrics = Biometrics.objects.all()
        serializer = BiometricsSerializer(biometrics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer, errors = get_serializer_and_validate(BiometricsSerializer, request.data)
        if serializer:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def biometrics_entry_list(request):
    if request.method == 'GET':
        entries = BiometricsEntry.objects.all()
        serializer = BiometricsEntrySerializer(entries, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer, errors = get_serializer_and_validate(BiometricsEntrySerializer, request.data)
        if serializer:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def biometrics_entry_values(request, pk):
    try:
        biometrics_entry = BiometricsEntry.objects.get(pk=pk)
    except BiometricsEntry.DoesNotExist:
        return handle_exception(ObjectDoesNotExist('BiometricsEntry not found'))
    
    values = biometrics_entry.values.all()
    serializer = BiometricsValueSerializer(values, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def latest_food_scores(request):
    latest_scores = FoodScore.objects.filter(
        id__in=FoodScore.objects.values('user').annotate(
            latest_id=Max('id')
        ).values('latest_id')
    ).select_related('user', 'food')
    
    serializer = FoodScoreSerializer(latest_scores, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_latest_food_score(request):
    user_id = request.query_params.get('user_id')
    if not user_id:
        return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        latest_score = FoodScore.objects.filter(user_id=user_id).latest('id')
    except FoodScore.DoesNotExist:
        return handle_exception(ObjectDoesNotExist('No food score found for this user'))
    
    serializer = FoodScoreSerializer(latest_score)
    return Response(serializer.data)
