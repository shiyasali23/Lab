from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import cv2
from ultralytics import YOLO
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the YOLO model
try:
    model = YOLO('./models/yolov8n.pt')  # Adjust model path if needed
    logger.info("YOLO model initialized successfully.")
except Exception as e:
    logger.error("Error initializing YOLO model: %s", e)
    raise

# Pydantic response model
class DetectionResponse(BaseModel):
    data: list[str]  # Renamed to match what you're returning

@app.post("/detect/", response_model=DetectionResponse)
async def predict(file: UploadFile = File(...)):
    try:
        # Read and decode the uploaded image
        image = await file.read()
        np_image = np.frombuffer(image, np.uint8)
        img = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

        # YOLO inference
        results = model(img)

        detected_items = set()
        for result in results:
            for detection in result.boxes:
                name = model.names[int(detection.cls)]
                confidence = detection.conf

                # Only include detections with confidence > 0.5
                if confidence > 0.5:
                    detected_items.add(name)

        response_items = list(detected_items)  # Convert set to list

        # Return the detection results
        if response_items:
            logger.info("Detection successful: %d items detected.", len(response_items))
            return DetectionResponse(data=response_items)  # Correct return field
        else:
            logger.info("No items detected.")
            return DetectionResponse(data=[])  # Correct return field

    except Exception as e:
        logger.error("Error during detection: %s", e)
        raise HTTPException(status_code=500, detail="An error occurred during detection.")
