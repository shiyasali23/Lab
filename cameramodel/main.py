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
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    model = YOLO('./models/yolov8n.pt')
    logger.info("YOLO model initialized successfully.")
except Exception as e:
    logger.error("Error initializing YOLO model: %s", e)
    raise

class DetectionResponse(BaseModel):
    class Item(BaseModel):
        name: str
        confidence: float
        bbox: list

    items: list[Item]
    message: str = None

@app.post("/detect/", response_model=DetectionResponse)
async def predict(file: UploadFile = File(...)):
    try:
        image = await file.read()
        np_image = np.frombuffer(image, np.uint8)
        img = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

        results = model(img)

        detections = {}
        for result in results:
            for detection in result.boxes:
                name = model.names[int(detection.cls)]
                confidence = detection.conf
                bbox = detection.xyxy[0].tolist()

                if name not in detections:
                    detections[name] = {
                        "confidence": confidence,
                        "bbox": bbox
                    }
                else:
                    if confidence > detections[name]["confidence"]:
                        detections[name] = {
                            "confidence": confidence,
                            "bbox": bbox
                        }

        response_items = [
            DetectionResponse.Item(name=name, confidence=det["confidence"], bbox=det["bbox"])
            for name, det in detections.items()
        ]

        if response_items:
            logger.info("Detection successful: %d items detected.", len(response_items))
            return DetectionResponse(items=response_items)
        else:
            logger.info("No items detected.")
            return DetectionResponse(items=[], message="No objects detected.")

    except Exception as e:
        logger.error("Error during detection: %s", e)
        raise HTTPException(status_code=500, detail="An error occurred during detection.")
