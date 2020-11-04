import sys
sys.path.append('..\\..\\virtual_opencv\\Lib\\site-packages\\cv2')

import cv2 as cv
import numpy as np

"""
img = cv.imread("..\\Resources\\Photos\\cat.jpg")
cv.imshow("Cat", img)
"""

# Three
blank = np.zeros((500, 500, 3), dtype = "uint8")

blank[200:, 300:] = 255,0,0

cv.rectangle(blank, (0, 0), (255, 255), (0,255,0), thickness = 1)
# Fill is thickness = -1
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 255), thickness = -1)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness = -1)
cv.line(blank, (0, 0), (blank.shape[1], blank.shape[0]), (255, 255, 255), thickness = 5)
cv.putText(blank, "Hello", (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255,0), 2)
cv.imshow("Blank", blank)

cv.waitKey(0)
