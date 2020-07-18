import cv2
from random import randrange

# Load some pre-trained data on frontal face from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

'''
######### FOR WEBCAM #########

# To capture video from webcam for face detection
webcam = cv2.VideoCapture(0)  # Argument 0 means it has to read from the webcam
key = cv2.waitKey(1)

## Iterate forever over frames(for video)
while True :

    # Read the current frame
    successful_frame_read, frame = webcam.read()

    # MUST covert the frame to grayscale (black and white)
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the given image.
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangles around the faces
    for (x,y,w,h) in face_coordinates :
        cv2.rectangle(frame, (x,y), (x+w,y+h), (randrange(256), randrange(256), randrange(256)), 10)

    # Display the image with faces identified
    cv2.imshow('FACE DETECTOR (PRESS Q TO QUIT)', frame)
    key = cv2.waitKey(1) # Displays each and every frame for 1 millisecond

    # Stop if Q key is pressed
    if key == 81 or key == 113 :    # ASCII code for Q:81 q:113
        break

# Release the VideoCapture object
webcam.release()
''' 

'''
########### FOR VIDEO ###########

# To capture video from webcam for face detection
video = cv2.VideoCapture('')  # pass the video
key = cv2.waitKey(1)

## Iterate forever over frames(for video)
while True :

    # Read the current frame
    successful_frame_read, frame = video.read()

    # MUST covert the frame to grayscale (black and white)
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the given image.
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangles around the faces
    for (x,y,w,h) in face_coordinates :
        cv2.rectangle(frame, (x,y), (x+w,y+h), (randrange(256), randrange(256), randrange(256)), 10)

    # Display the image with faces identified
    cv2.imshow('FACE DETECTOR (PRESS Q TO QUIT)', frame)
    key = cv2.waitKey(1) # Displays each and every frame for 1 millisecond

    # Stop if Q key is pressed
    if key == 81 or key == 113 :    # ASCII code for Q:81 q:113
        break

# Release the VideoCapture object
video.release()
'''

'''
########### FOR IMAGE ONLY ###########

# Choose an image to detect faces in
img = cv2.imread('threeppl.png')

# MUST covert the image to grayscale (black and white)
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the given image. face_coordinates gives the coordinates of the top-left and bottom-right points of the rectangle
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#print(face_coordinates)

# Draw rectangles around the faces
for (x,y,w,h) in face_coordinates :
    cv2.rectangle(img, (x,y), (x+w,y+h), (randrange(256), randrange(256), randrange(256)), 3)

# Display the image with faces identified
cv2.imshow('FACE DETECTOR (PRESS Q TO QUIT)',img)
cv2.waitKey()    # Press any key to quit
'''


print("Code completed")