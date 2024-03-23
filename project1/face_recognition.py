import cv2
import os
import numpy as np


# Function to prepare training data
def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    faces = []
    labels = []

    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue

        label = int(dir_name.replace("s", ""))
        subject_dir_path = data_folder_path + "/" + dir_name
        subject_images_names = os.listdir(subject_dir_path)

        for image_name in subject_images_names:
            if image_name.startswith("."):
                continue

            image_path = subject_dir_path + "/" + image_name
            image = cv2.imread(image_path)
            face, rect = detect_face(image)

            if face is not None:
                faces.append(face)
                labels.append(label)

    return faces, labels


# Function to detect face
def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    if len(faces) == 0:
        return None, None

    (x, y, w, h) = faces[0]
    return gray[y:y + w, x:x + h], faces[0]


# Path to the training dataset
data_folder_path = "dataset"

# Prepare training data
faces, labels = prepare_training_data(data_folder_path)

# Create LBPH recognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the recognizer
face_recognizer.train(faces, np.array(labels))

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale for better computation
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    face, rect = detect_face(frame)

    if face is not None:
        # Recognize the face
        label, confidence = face_recognizer.predict(face)

        # Display the name and confidence level
        if confidence < 100:
            label_text = "Person: " + str(label)
            confidence_text = "Confidence: {:.2f}".format(confidence)
        else:
            label_text = "Unknown"
            confidence_text = ""

        cv2.putText(frame, label_text, (rect[0], rect[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.putText(frame, confidence_text, (rect[0], rect[1] + rect[3] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 255, 0), 2)

    # Display the output
    cv2.imshow('Facial Recognition', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
