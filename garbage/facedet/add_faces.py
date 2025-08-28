# COLLECTING NAMES AND FACE DATA

import cv2
import pickle # file storing library pkl
import numpy as np
import os # it can be used to check whether some file is available in some folder

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

faces_data = [] # empty list
i = 0

name = input("Enter your name: ")

while True:
    ret, frame = video.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # conv BGR to greyscale
    faces = facedetect.detectMultiScale(gray, 1.3, 5) # giving threashold 1.3-5
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, : ] # parameters[top->top+height=bottom, left->left+width=right, channels (left blank to include all channels i.e RGB~ 3-2-1) ]
        resized_img = cv2.resize(crop_img, (50, 50)) # parameters(image, tuple of dimension to resize in)
        if len(faces_data) <= 50 and i%10 == 0: # it will take 10 images [and] each after 10 frames 
            faces_data.append(resized_img) # storing resized image in a list
        i = i+1 # calculating frames
        cv2.putText(frame, str(len(faces_data)), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (50,50,255), 1) # parameters(frame, text to display, coordinates to put text in, fontFace, fontScale, fontColor, fontThickness)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1) # parameters(cordinates, dimension, color, thickness) rectangle on face
    cv2.imshow('Add Faces', frame)
    if cv2.waitKey(1) == ord('q') or len(faces_data) == 50: # millisec, when array has 10 elements i.e 10 images
        break
video.release()
cv2.destroyAllWindows()

faces_data = np.asarray(faces_data) # making faces_data a numpy array for efficiency
faces_data = faces_data.reshape(50, -1) # as we are taking 10 images the vector size should be 10, so we'll reshape the array

# NAME DATA
# checking if name.pkl is in our data folder using os library
if 'names.pkl' not in os.listdir('data/'): 
    names = [name]*50 # converting name to a list (of vector)
    with open('data/names.pkl', 'wb') as f: # we have defined f as an alias
        pickle.dump(names, f) # parameters(object, file) here object=name
else:
    with open('data/names.pkl', 'rb') as f:
        names = pickle.load(f)
    # storing/dumping data
    names = names+[name]*50 # concatinate new data (name) to old if old exist
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)

# FACE DATA
# checking if name.pkl is in our data folder using os library
if 'faces_data.pkl' not in os.listdir('data/'): 
    with open('data/faces_data.pkl', 'wb') as f: # we have defined f as an alias
        pickle.dump(faces_data, f) # parameters(object, file) here object=name
else:
    with open('data/faces_data.pkl', 'rb') as f:
        faces = pickle.load(f)
    # storing/dumping data
    faces = np.append(faces, faces_data, axis=0) # concatinate new data (name) to old if old exist
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces, f)







