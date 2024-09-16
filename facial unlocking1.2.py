import cv2
import os

# Load the pre-trained face cascade provided by OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

# Function to detect faces in the frame
def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Variable to keep track of the detected face
detected_face = False

# Create a folder to save the pictures if it doesn't exist
os.makedirs('pictures', exist_ok=True)

# Main loop to capture video frames until a face is detected
while not detected_face:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Detect faces in the frame
    faces = detect_faces(frame)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Facial Recognition', frame)

    # Check for the 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Check if a face is detected
    if len(faces) > 0:
        # Save the image
        cv2.imwrite('pictures/face.jpg', frame)
        detected_face = True

# Release the video capture and close the window
video_capture.release()
cv2.destroyAllWindows()
