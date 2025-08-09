Attention-detector
  -Developed attention detecting system to detect the user is focused or distracted
  
Basic Details
  Kavya Krishna N U -College of Engineering and Management Punnapra (KTU)
  
Project Description
  Attention detector is a real-time attention detection system that uses MediaPipe’s Face Mesh and OpenCV to analyze eye positions in a webcam feed, displaying whether a user is   "Focused" or "Distracted" via a Streamlit web interface alerting students and employees when they get distracted.

The Problem (that doesn't exist)
Students and IT workers are so overwhelmed by their ability to stare blankly at screens that they sometimes drift into the dangerous territory of laziness, distracted by shiny notifications or daydreams of pizza!

The Solution (that nobody asked for)
Attention detector polices your focus like a hawk! It uses MediaPipe’s Face Mesh to track eye positions, calculates an eye distance ratio, and slaps a "Focused" or "Distracted" label on your webcam feed in a sleek Streamlit interface. Drift off? A bold warning message pops up to snap you back to reality!

Technical Details
Technologies/Components Used

For Software:
Languages used:Languages used: Python
Frameworks used: Streamlit, OpenCV, MediaPipe
Libraries used: streamlit, cv2, mediapipe, numpy, time
Tools used: Python 3.10, pip, webcam

Implementation
For Software:
Project Structure

Implementation Details
Focus Detection Logic (focus_detection.py):
Captures a video frame and converts it to RGB for MediaPipe processing.
Uses MediaPipe’s Face Mesh to detect facial landmarks, focusing on left and right eye landmarks (indices 33 and 133 for left eye, 362 and 263 for right eye).
Calculates the eye distance ratio (dy/dx) between the eyes to determine focus:
If the ratio is < 0.08, the user is "Focused" (eyes aligned).
Otherwise, the user is "Distracted" (eyes misaligned, indicating head tilt or looking away).
Optionally draws green dots on eye landmarks for visualization (disabled by default).

Streamlit Interface (app.py):
Displays a title ("Attention detection – Real-time Focus Monitor") and a "Start Monitoring" button.
Streams the webcam feed in real-time using st.image.
Overlays the focus status ("Focused" or "Distracted") on the video feed using OpenCV’s cv2.putText.
When "Distracted" is detected, a warning message (e Tale: Streamlit does not support pop-ups; we use st.warning to display "Hey, stay focused!" in the interface.
Uses a 0.03-second delay (time.sleep) to ensure smooth frame rendering.

Warning Message: When the status is "Distracted," a warning message appears in the Streamlit interface to alert the user. This is implemented using Streamlit’s st.warning function for a prominent visual cue.

Run
1. Start the Streamlit application:  
bash
streamlit run app.py

Project Documentation
For Software:

Screenshots 
https://drive.google.com/drive/my-drive/focused1.png -  Streamlit interface showing the user marked as "Focused" with the status overlaid on the webcam feed.

https://drive.google.com/drive/my-drive/focused2.png - Streamlit interface showing the user marked as "Focused" with the status overlaid on the webcam feed.

https://drive.google.com/drive/my-drive/distracted.png -  Streamlit interface showing the user marked as "Distracted" with a warning message displayed below the video feed.



Project Demo
Video
- The demo video demonstrates real-time focus detection, showing the webcam feed in Streamlit with "Focused" or "Distracted" labels.


