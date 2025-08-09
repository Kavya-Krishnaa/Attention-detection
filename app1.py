import streamlit as st
import cv2
import mediapipe as mp
import time
from focus_detection import detect_face_status

st.set_page_config(page_title="Focus Buddy", layout="wide")
st.title("🎯 Attention detection – Real-time Focus Monitor")

start = st.button("Start Monitoring")
FRAME_WINDOW = st.image([])

if start:
    cap = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        processed_frame, status = detect_face_status(frame, face_mesh)

        cv2.putText(processed_frame, f'Status: {status}', (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

        stframe.image(processed_frame, channels='BGR')
        time.sleep(0.03)  # Smooth frame rate

    cap.release()