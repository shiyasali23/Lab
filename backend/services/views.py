from .models import User, Biometrics, FoodScore
from .serializers import UserSerializer, BiometricsSerializer, FoodScoreSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

import logging
import traceback

logger = logging.getLogger(__name__)

def handle_error(context, exception):
    error_msg = str(exception)
    traceback_msg = traceback.format_exc()
    logger.error(f"Unhandled error in {context}: {error_msg}\n{traceback_msg}")
    return {'error': error_msg}

def generic_list_view(request, model, serializer_class):
    try:
        if request.method == 'GET':
            objects = model.objects.all()
            serializer = serializer_class(objects, many=True)
            data = [{key: value for key, value in item.items() if key not in ('category', 'subcategory', 'created')} for item in serializer.data]
            return Response(data)

        elif request.method == 'POST':
            if isinstance(request.data, list):
                serializer = serializer_class(data=request.data, many=True)
            else:
                serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error(f"Error in POST request for {model.__name__}: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(handle_error('generic_list_view', e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def generic_detail_view(request, model, serializer_class, pk):
    try:
        obj = model.objects.get(pk=pk)
    except model.DoesNotExist:
        error_msg = f"{model.__name__} with pk {pk} does not exist"
        logger.error(error_msg)
        return Response({'error': error_msg}, status=status.HTTP_404_NOT_FOUND)

    try:
        if request.method == 'GET':
            serializer = serializer_class(obj)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = serializer_class(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                logger.error(f"Error in PUT request for {model.__name__} with pk {pk}: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response(handle_error('generic_detail_view', e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

########################################################################################################

@api_view(['GET', 'POST'])
def user_list(request):
    return generic_list_view(request, User, UserSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    return generic_detail_view(request, User, UserSerializer, pk)

@api_view(['GET', 'POST'])
def biometrics_list(request):
    return generic_list_view(request, Biometrics, BiometricsSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def biometrics_detail(request, pk):
    return generic_detail_view(request, Biometrics, BiometricsSerializer, pk)

@api_view(['GET', 'POST'])
def foodscore_list(request):
    return generic_list_view(request, FoodScore, FoodScoreSerializer)


@api_view(['GET', 'PUT', 'DELETE'])
def foodscore_detail(request, pk):
    return generic_detail_view(request, FoodScore, FoodScoreSerializer, pk)

@api_view(['POST'])
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user': UserSerializer(user).data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(handle_error('signup', e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({
                        'token': token.key,
                        'user': UserSerializer(user).data
                    })
                else:
                    return Response({'error': 'This account is inactive.'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(handle_error('login', e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
