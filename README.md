# Facial_Analytics_with_Computer_vision
## Overview

This Python script uses the OpenCV library to perform face detection in a video stream, counting the number of faces in each frame and displaying the count. Additionally, it saves frames with detected faces as image files.

## Dependencies

- OpenCV (`cv2`): For computer vision tasks.
- imutils: For convenient resizing of images.

## Usage

1. Install the required libraries:

   ```bash
   pip install opencv-python imutils
Run the script:

bash

    python people_counting.py

    The script opens a video file (or webcam) and processes each frame, detecting faces and displaying the count on the frame.

    Press 'q' to exit the program.

Configuration

    You can change the input video file by modifying the cap = cv2.VideoCapture("your_video_path.mp4") line.

Output

    The script saves each frame with detected faces as an image file in the working directory.

Notes

    Face detection accuracy may vary based on the quality of the input video and the chosen parameters.
