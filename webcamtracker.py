import cv2
import dlib
from scipy.spatial import distance
import numpy as np
import time

import firebase_admin 
from firebase_admin import credentials

# Replace 'path/to/your/serviceAccountKey.json' with the actual path to your downloaded JSON file
cred = credentials.Certificate(r'C:\Users\betha\Downloads\alertarival2-firebase-adminsdk-ns8qt-07e362da7b.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://alertarival2-default-rtdb.firebaseio.com'
})

from firebase_admin import db
ref = db.reference ("/Test1")

data = ref.get()

# Function to calculate the eye aspect ratio (EAR)
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Load the face and eye detectors from dlib
face_detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Open the front camera (use index 1)
cap = cv2.VideoCapture(1)

# Duration closed detection parameters
duration_closed_threshold = 2  # Adjust the duration closed threshold (in seconds) as needed

duration_closed_counter = 0
start_time = time.time()
eyes_closed = False

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_detector(gray)

    for face in faces:
        # Get facial landmarks
        landmarks = predictor(gray, face)

        # Extract the left and right eye landmarks
        left_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)]
        right_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)]

        # Convert the eye landmarks to NumPy arrays
        left_eye = np.array(left_eye, dtype=np.int32)
        right_eye = np.array(right_eye, dtype=np.int32)

        # Calculate the eye aspect ratio for each eye
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)

        # Average the eye aspect ratio for both eyes
        avg_ear = (left_ear + right_ear) / 2.0

        # Draw the eyes on the frame
        cv2.polylines(frame, [left_eye], isClosed=True, color=(0, 255, 0), thickness=2)
        cv2.polylines(frame, [right_eye], isClosed=True, color=(0, 255, 0), thickness=2)

        # Display the eye aspect ratio on the frame
        cv2.putText(frame, f'EAR: {avg_ear:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Check if the eyes are closed (EAR below a certain threshold)
        if avg_ear < 0.25:
            duration_closed_counter += time.time() - start_time
            if not eyes_closed:
                cv2.putText(frame, "Eyes Closed", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                eyes_closed = True
        else:
            eyes_closed = False
            duration_closed_counter = 0
            start_time = time.time()

        # Check for drowsiness
        if duration_closed_counter >= duration_closed_threshold:
            # Update Firebase only when drowsiness is detected
            ref.set({
                'alert': 'true',
            })
            cv2.putText(frame, "Drowsiness detected - Eyes closed for too long", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 0, 255), 2)

    cv2.imshow("Eye Tracker", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
