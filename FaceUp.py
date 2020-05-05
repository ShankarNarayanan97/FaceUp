# -*- coding: utf-8 -*-
"""
Created on Tue May 5 19:16:42 2020

@author: S Shankar Narayanan
"""

# Importing the neccessary libraries
import cv2
import matplotlib.pyplot as plt
import cvlib as cv

image_path = 'put your image URL here' # Giving a place for the program to look
im = cv2.imread(image_path)
plt.imshow(im)  
plt.show() # Before face detection

faces, confidences = cv.detect_face(im)
# I am now looping through detected faces and adding a bounding box
for i in faces:
    (startX,startY) = i[0],i[1]
    (endX,endY) = i[2],i[3]
    # draw rectangle over face
    cv2.rectangle(im, (startX,startY), (endX,endY), (0,255,0), 2)
# display output        
plt.imshow(im)
plt.show() # After face detection
