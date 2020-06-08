import cv2
import os
import numpy
img = cv2.imread("all_predictions.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
T, boundary = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
cv2.imwrite("result.png",boundary)