# FACE RECOGNIZATION

# For recognizing face we will use a KNN classification (and regression) algorithm
# KNN is available in a ML library named SciKit learn
# K-Nearest Neighbors (KNN) is a simple and widely used supervised machine learning algorithm used for classification and regression tasks. It's a type of instance-based learning, or lazy learning, where the algorithm makes predictions based on the majority class or average value of the k-nearest data points in the feature space.

# KNN has two phases 

# 1: Training Phase
#    During the training phase, the algorithm simply memorizes the training dataset, storing the feature vectors and their corresponding labels.

# 2: Prediction Phase
#    When making a prediction for a new data point, the algorithm identifies the k-nearest neighbors to that point in the feature space. The distance metric (such as Euclidean distance) is commonly used to measure the similarity between data points.
#    * For classification, the algorithm assigns the majority class among the k-neighbors to the new data point.
#    * For regression, the algorithm calculates the average (or weighted average) of the target values of the k-neighbors and assigns this value to the new data point.


# KNN is a lazy learning algorithm that memorizes the entire training dataset.

# Lazy learning is an approach where the algorithm does not create an explicit model during the training phase.
# Instead, it "memorizes" the entire training dataset.

# During the training phase, lazy learning algorithms do minimal work.
# They store the training instances and their corresponding labels without building an explicit model 
# or making significant computations.


from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import RadiusNeighborsClassifier

import cv2
import pickle # file storing library pkl

from datetime import datetime
import csv
import time
import os

from win32com.client import Dispatch

def speak(str1):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Loading Names data
with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)
    
# Loading Faces data
with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

imgBackground = cv2.imread('background.png')

COL_NAMES = ['NAME', 'TIME']

while True:
    ret, frame = video.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # conv BGR to greyscale
    faces = facedetect.detectMultiScale(gray, 1.3, 5) # giving threashold 1.3-5
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, : ] # parameters[top->top+height=bottom, left->left+width=right, channels (left blank to include all channels i.e RGB~ 3-2-1) ]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1,-1) # parameters(image, tuple of dimension to resize in) here we'll flatten and then resize the image to be in single vector i.e we'll pass 1 image at a time to our machine learning algorithm that is KNN
        output = knn.predict(resized_img)
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timeStamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        exist = os.path.isfile("Attendance/" + date + ".csv")
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 1)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (50,50,255), 2)
        cv2.rectangle(frame, (x,y-40), (x+w,y), (50,50,255), -1)
        cv2.putText(frame, str(output[0]), (x,y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1) # parameters(cordinates, dimension, color, thickness) rectangle on face
        attendance = [str(output[0]), str(timeStamp)] # adding attendance inside a list
    imgBackground[162:162+480, 55:55+640] = frame
    cv2.imshow('Face Recognition', imgBackground)
    k = cv2.waitKey(1)

    if k == ord('o'):
        speak(str(output[0]) + " your attendance is taken ....")
        time.sleep(2)
        if exist:
            with open("Attendance/" + date + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(attendance)
            csvfile.close()
        else:
            with open("Attendance/" + date + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)
            csvfile.close()
    if k == ord('q'): # millisec
        break

video.release()
cv2.destroyAllWindows()

