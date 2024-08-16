from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
import logging

from .models import User, Biometrics
from .serializers import UserSerializer, BiometricsSerializer

logger = logging.getLogger(__name__)


def get_user_details(user):
    try:
        latest_biometrics = Biometrics.objects.filter(user=user).order_by('-id').first()
        biometrics_values_data = []
        food_scores_data = []
        if latest_biometrics:
            biometrics_values = BiometricsValue.objects.filter(biometrics_entry__biometrics=latest_biometrics)
            biometrics_values_data = BiometricsValueSerializer(biometrics_values, many=True).data

            food_scores = FoodScore.objects.filter(biometrics_entry__biometrics=latest_biometrics)
            food_scores_data = FoodScoreSerializer(food_scores, many=True).data

        return {
            'latest_biometrics': BiometricsSerializer(latest_biometrics).data if latest_biometrics else None,
            'biometrics_values': biometrics_values_data,
            'food_scores': food_scores_data,
        }

    except Exception as exc:
        logger.error(f"Error fetching user details: {str(exc)}", exc_info=True)
        return None


@api_view(['POST'])
def signup(request):
    email = request.data.get('email')

    if User.objects.filter(email=email).exists():
        return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            response = get_user_details(user)
            if response is None:
                return Response({'error': 'An unexpected error occurred while fetching user details.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            response['token'] = token.key
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as exc:
            logger.error(f"Error during user signup: {str(exc)}", exc_info=True)
            return Response({'error': 'An unexpected error occurred during signup.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)

    if user and user.is_active:
        try:
            token, _ = Token.objects.get_or_create(user=user)
            response = get_user_details(user)
            if response is None:
                return Response({'error': 'An unexpected error occurred while fetching user details.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            response['token'] = token.key
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as exc:
            logger.error(f"Error during user login: {str(exc)}", exc_info=True)
            return Response({'error': 'An unexpected error occurred during login.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def create_biometrics(request, pk):
    try:
        user = User.objects.get(id=pk)
        data = request.data.copy()
        data['user'] = user.id  
        serializer = BiometricsSerializer(data=data)
        if serializer.is_valid():
            biometrics = serializer.save()
            response = get_user_details(user)
            if response is None:
                return Response({'error': 'An unexpected error occurred while fetching user details.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as exc:
        logger.error(f"Error creating biometrics: {str(exc)}", exc_info=True)
        return Response({'error': 'An unexpected error occurred while creating biometrics.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def deactivate_user(request, pk=None):
    try:
        if pk:
            user = User.objects.get(pk=pk)
        else:
            email = request.data.get('email')
            user = User.objects.get(email=email)
        
        user.is_active = False
        user.save()
        return Response({'message': 'User account has been deactivated successfully.'}, status=status.HTTP_200_OK)
    
    except ObjectDoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as exc:
        logger.error(f"Error during user deactivation: {str(exc)}", exc_info=True)
        return Response({'error': 'An unexpected error occurred during user deactivation.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)