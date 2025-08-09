import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh

# Eye landmark indices (MediaPipe FaceMesh)
LEFT_EYE = [33, 133]
RIGHT_EYE = [362, 263]

def detect_face_status(frame, face_mesh, draw_landmarks=False):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    status = "No Face"
    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
            h, w, _ = frame.shape
            left_eye = face_landmarks.landmark[LEFT_EYE[0]]
            right_eye = face_landmarks.landmark[RIGHT_EYE[0]]
            
            left_eye_coords = (int(left_eye.x * w), int(left_eye.y * h))
            right_eye_coords = (int(right_eye.x * w), int(right_eye.y * h))

            if draw_landmarks:
                cv2.circle(frame, left_eye_coords, 3, (0, 255, 0), -1)
                cv2.circle(frame, right_eye_coords, 3, (0, 255, 0), -1)

            # Simple rule: if eyes are aligned horizontally, user is likely focused
            dx = abs(left_eye_coords[0] - right_eye_coords[0])
            dy = abs(left_eye_coords[1] - right_eye_coords[1])
            ratio = dy / dx if dx != 0 else 0

            if ratio < 0.08:
                status = "Focused"
            else:
                status = "Distracted"
    return frame, status
