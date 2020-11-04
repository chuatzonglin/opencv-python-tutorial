import sys
sys.path.append('..\\..\\virtual_opencv\\Lib\\site-packages\\easygui')

import easygui

myvar = easygui.enterbox("What, is your favorite color?")

print(myvar)
"""
import sys
sys.path.append('..\\..\\virtual_opencv\\Lib\\site-packages\\cv2')

import cv2 as cv 
import numpy as np 
img = cv.imread("..\\Resources\\Photos\\cat.jpg")
cv.imshow("Cat", img)
"""
"""

# Three 
blank = np.zeros((500, 500, 3), dtype = "uint8")

blank[200:, 300:] = 255,0,0

cv.imshow("Blank", blank)


cv.waitKey(0)
"""