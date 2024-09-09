import cv2
from ultralytics import YOLO
import pandas as pd
from food_score import sorted_scaled_biometrics

# Read the CSV file and get the food names and scores
food_score_df = pd.read_csv('dataset/user_1_food_score.csv')  # Adjust the path as necessary
food_score = food_score_df[['name', 'score']].copy()
name = "Shiyas"
corner_text = "You have low Fiber, vitamin A \nhigh sucrose levels"

# Create a dictionary for faster lookup
food_score_dict = dict(zip(food_score['name'], food_score['score']))

# Calculate quantiles once
q50 = food_score['score'].quantile(0.5)
q75 = food_score['score'].quantile(0.75)

def assign_prediction(score):
    if score < 0:
        return ("strictly avoid", (0, 0, 128)) if score < q50 else ("better to avoid", (0, 128, 255))
    else:
        return ("eat plenty", (0, 255, 0)) if score > q75 else ("eat moderately", (0, 255, 127))

# Initialize YOLOv8 model
model = YOLO('yolov8n.pt')

# Initialize webcam
cap = cv2.VideoCapture(0)

def add_corner_label(frame, text, position='top-right'):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.2  # Increased font scale
    font_thickness = 2
    text_color = (255, 255, 255)
    bg_color = (0, 0, 0)
    padding = 20  # Increased padding

    # Split text into lines
    lines = text.split('\n')
    
    # Calculate text size
    line_heights = [cv2.getTextSize(line, font, font_scale, font_thickness)[0][1] for line in lines]
    total_height = sum(line_heights) + padding * (len(lines) + 1)
    max_width = max([cv2.getTextSize(line, font, font_scale, font_thickness)[0][0] for line in lines])
    total_width = max_width + padding * 2

    # Determine position
    if position == 'top-right':
        start_x = frame.shape[1] - total_width - padding
        start_y = padding
    elif position == 'bottom-right':
        start_x = frame.shape[1] - total_width - padding
        start_y = frame.shape[0] - total_height - padding

    # Create semi-transparent overlay
    overlay = frame.copy()
    cv2.rectangle(overlay, (start_x, start_y), (start_x + total_width, start_y + total_height), bg_color, -1)
    cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)  # Increased opacity

    # Add text
    y = start_y + padding + line_heights[0]
    for i, line in enumerate(lines):
        cv2.putText(frame, line, (start_x + padding, y), font, font_scale, text_color, font_thickness, cv2.LINE_AA)
        y += line_heights[i] + padding

    return frame

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 inference on the frame
    results = model(frame)[0]

    # Create a new image to draw on
    annotated_frame = frame.copy()

    # Iterate through detected boxes and filter based on food names
    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
        label = model.names[int(box.cls)].lower()

        # Check if the label is in food_score_dict
        if label in food_score_dict:
            score = food_score_dict[label]
            prediction_text, color = assign_prediction(score)

            # Create a transparent rectangle for detection
            overlay = annotated_frame.copy()
            cv2.rectangle(overlay, (x1, y1), (x2, y2), color, -1)
            cv2.addWeighted(overlay, 0.3, annotated_frame, 0.7, 0, annotated_frame)
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)

            # Prepare text with line breaks
            text = f"I think it's {label}.\n{prediction_text}"
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1.2
            font_thickness = 2
            text_lines = text.split('\n')

            # Calculate text box dimensions
            text_sizes = [cv2.getTextSize(line, font, font_scale, font_thickness)[0] for line in text_lines]
            text_box_width = max(size[0] for size in text_sizes) + 20
            text_box_height = sum(size[1] for size in text_sizes) + 20 * len(text_lines)

            # Position text box
            text_box_x = min(x2, annotated_frame.shape[1] - text_box_width)
            text_box_y = max(y1 - text_box_height, 0)

            # Draw text box
            cv2.rectangle(annotated_frame, (text_box_x, text_box_y),
                          (text_box_x + text_box_width, text_box_y + text_box_height),
                          color, -1)

            # Add text
            y_offset = text_box_y + 30
            for line in text_lines:
                cv2.putText(annotated_frame, line,
                            (text_box_x + 10, y_offset),
                            font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)
                y_offset += text_sizes[text_lines.index(line)][1] + 20

    # Add corner label
    corner_label_text = f"Hi {name}\n{corner_text}"
    annotated_frame = add_corner_label(annotated_frame, corner_label_text, position='top-right')

    # Display the annotated frame
    cv2.imshow("LAB's YOLOv8 Inference", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()