from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import numpy as np
import cv2
from ultralytics import YOLO

app = FastAPI()

# Initialize YOLOv8 model
model = YOLO('./models/yolov8n.pt')

@app.post("/get_camera_model/")
async def predict(file: UploadFile = File(...)):
    # Convert file to a numpy array and decode
    image = np.frombuffer(await file.read(), np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    # Perform inference
    results = model(image)[0]
    predictions = []

    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
        label = model.names[int(box.cls)]
        predictions.append({
            "label": label,
            "box": [x1, y1, x2, y2]
        })

    return {"predictions": predictions}
