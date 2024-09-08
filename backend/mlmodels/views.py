import requests
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MachineLearningModel
from .serializers import MachineLearningModelSerializer

logger = logging.getLogger(__name__)

@api_view(['POST'])
def register_model(request):
    serializer = MachineLearningModelSerializer(data=request.data, partial=True)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    model_data = {key: value for key, value in serializer.validated_data.items() if key not in ['created_at', 'updated_at', 'status']}
    
    try:
        # Send model data to FastAPI service
        response = requests.post('http://localhost:8001/register_models/', json=model_data)
        response.raise_for_status()  
        
        if response.status_code == 200:
            data = response.json()
            
            for item in data:
                item['status'] = 'active' 
                
            # Use many=True for bulk serialization
            model_serializer = MachineLearningModelSerializer(data=data, partial=True, many=True)
            if model_serializer.is_valid():
                model_serializer.save()
                return Response({"detail": "Models registered successfully."}, status=status.HTTP_201_CREATED)
            else:
                logger.error(f"Model serializer errors: {model_serializer.errors}")
                return Response(model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            logger.error(f"Failed to register models with FastAPI. Status code: {response.status_code}")
            return Response({"detail": "Failed to register models with FastAPI."}, status=status.HTTP_400_BAD_REQUEST)
    except requests.RequestException as e:
        logger.error(f"Failed to register model: {e}")
        return Response({"detail": f"Failed to register model: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
