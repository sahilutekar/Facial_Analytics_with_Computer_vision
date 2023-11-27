

import cv2
import imutils

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open a video file for processing (you can also use a webcam by changing the line)
cap = cv2.VideoCapture("C:/Users/sahil/Downloads/Bad Landlording.mp4")
# cap = cv2.VideoCapture(0)

# Initialize a counter to keep track of the number of people detected
count = 0

# Loop through each frame in the video
while True:
    # Read the current frame
    ret, frame = cap.read()
    
    # Break the loop if there are no more frames
    if not ret:
        break

    # Resize the frame for better performance
    frame = imutils.resize(frame, width=500)
    
    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Update the people count based on the number of detected faces
    count = len(faces)

    # Display the people count on the frame
    cv2.putText(frame, "People Count: {}".format(count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    
    # Show the frame with rectangles drawn around faces
    cv2.imshow("Frame", frame)

    # Save the frame with detected faces
    cv2.imwrite(f"output_frame_{count}.png", frame)

    # Check for the 'q' key press to exit the program
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

# Read a reference image for comparison (assuming it's a ground truth image)
reference_image = cv2.imread("C:/Users/sahil/Desktop/people_counting_withcv/gt.png", cv2.IMREAD_GRAYSCALE)



