from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import logging

from .serializers import MachineLearningModelSerializer

logger = logging.getLogger(__name__)

@api_view(['POST'])
def register_model(request):
    try:
        response = requests.get('http://localhost:8001/register_models/')
        response.raise_for_status()         
        if response.status_code == 200:
            data = response.json()           
            for item in data:
                item['status'] = 'active' 
            model_serializer = MachineLearningModelSerializer(data=data, partial=True, many=True)
            if model_serializer.is_valid():
                model_serializer.save()
                for registered_model in model_serializer.data:
                    logger.info(f"Registered model: {registered_model['name']}")
                return Response({"message": "Models registered successfully!"}, status=201)
            else:
                logger.error(f"Model serializer errors: {model_serializer.errors}")
                return Response(model_serializer.errors, status=400)
        else:
            logger.error(f"Failed to register models with FastAPI. Status code: {response.status_code}")
            return Response({"error": "Failed to register models from FastAPI"}, status=response.status_code)
    except requests.RequestException as e:
        logger.error(f"Failed to register model: {e}")
        return Response({"error": "Failed to connect to FastAPI service"}, status=500)
