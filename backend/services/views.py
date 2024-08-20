import logging
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404


from .models import User, Biometrics, BiometricsValue, FoodScore
from adminpanel.models import Biochemical
from adminpanel.serializers import BiochemicalSerializer
from .serializers import UserSerializer, BiometricsSerializer, BiometricsValueSerializer, FoodScoreSerializer

logger = logging.getLogger(__name__)

def get_token_from_request(request):
    token_key = request.headers.get('Authorization', '').split(' ')[-1]
    return get_object_or_404(Token, key=token_key)


def get_error_message(error_dict):
    if isinstance(error_dict, dict):
        for field, errors in error_dict.items():
            if isinstance(errors, list):
                return f"{field}: {errors[0]}"
            elif isinstance(errors, str):
                return f"{field}: {errors}"
    return str(error_dict)


def handle_response(data=None, error=None, status_code=status.HTTP_200_OK):
    if error:
        error_message = get_error_message(error)
        logger.error(f"Error: {error_message}")
        return Response({'error': error_message}, status=status_code)
    return Response(data, status=status_code)

def get_user_details(user):
    try:
        latest_biometrics = Biometrics.objects.filter(user=user).order_by('-id').first()
        biochemicals = Biochemical.objects.all()
        biometrics_values = BiometricsValue.objects.filter(biometrics=latest_biometrics) if latest_biometrics else []
        biometrics_values_dict = {value.biochemical.id: value for value in biometrics_values}
        biometrics_values_data = []
        for biochemical in biochemicals:
            value_entry = biometrics_values_dict.get(biochemical.id)
            biometrics_values_data.append({
                'biochemical': BiochemicalSerializer(biochemical).data,
                'value': value_entry.value if value_entry else None,
                'scaled_value': value_entry.scaled_value if value_entry else None,
                'expired_date': value_entry.expired_date if value_entry else None
            })
        latest_biometrics_data = BiometricsSerializer(latest_biometrics).data if latest_biometrics else None
        food_scores_data = FoodScoreSerializer(FoodScore.objects.filter(biometrics=latest_biometrics), many=True).data if latest_biometrics else []

        return {
            'user': UserSerializer(user).data,
            'latest_biometrics': latest_biometrics_data,
            'biometrics_values': biometrics_values_data,
            'food_scores': food_scores_data,
        }
    except Exception as exc:
        logger.exception(f"Error fetching user details: {exc}")
        return None


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_user(request):
    try:
        token = get_token_from_request(request)
        response_data = get_user_details(token.user)
        return handle_response(response_data, status_code=status.HTTP_200_OK)
    except Exception as exc:
        return handle_response(error=exc, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def logout(request):
    try:
        token = get_token_from_request(request)
        token.delete()
        return Response({"detail": "Logout successful!"}, status=status.HTTP_200_OK)
    except Exception as exc:
        return Response({"detail": str(exc)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def deactivate_user(request):
    try:
        token = get_token_from_request(request)
        user = token.user
        
        if user.is_active:
            user.is_active = False
            user.save()
            token.delete()
            return Response({'message': 'Account successfully deactivated.'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Account is already inactive.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as exc:
        return Response({'detail': str(exc)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PATCH'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def update_user(request):
    try:
        token = get_token_from_request(request)
        user = token.user
        
        if user.is_active:
            serializer = UserSerializer(user, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(f"Validation error: {serializer.errors}")
            return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Account is inactive.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as exc:
        logger.exception("Unexpected error in update_user")
        return Response({'detail': str(exc)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data={**request.data, 'is_active': True, 'is_staff': False})
    if serializer.is_valid():
        try:
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            response_data = get_user_details(user)
            if response_data:
                response_data['token'] = token.key
                return handle_response(response_data, status_code=status.HTTP_201_CREATED)
        except Exception as exc:
            return handle_response(error=exc, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return handle_response(error=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
    if user and user.is_active:
        try:
            token, _ = Token.objects.get_or_create(user=user)
            response_data = get_user_details(user)
            if response_data:
                response_data['token'] = token.key
                return handle_response(response_data)
        except Exception as exc:
            return handle_response(error=exc, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return handle_response(error='Invalid credentials.', status_code=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def create_biometrics(request):
    try:
        token = get_token_from_request(request)
        user = token.user
        
        if user.is_active:
            data = {**request.data, 'user': user.id}
            serializer = BiometricsSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Account is inactive.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as exc:
        return Response({'detail': str(exc)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# biochemicals = {
#     {
#         name : 'x',
#         id : 1,
#     },
#     {
#         name : 'w',
#         id : 2,
#     },
#     {
#         name : 'z',
#         id : 3,
#     },
# }


# biometrics_values = {
#     {
#         'biochemical':{
#             'name': 'x',
#             'id': 1,
#         }
#         'value' :34,
#         'scaled_value' : 0.34
#     },
#     {
#         biochemical :{
#             'name': 'w',
#             'id': 2,
#         }
#         'value' :4,
#         'scaled_value' : 0.4
#     },
#     {
#         biochemical : {
#             'name': 'z',
#         'id': 3,
#         }
#         'value' : null,
#         'scaled_value' :  null,
#     },
# }