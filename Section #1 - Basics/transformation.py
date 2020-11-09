import cv2 as cv
import numpy as np

img = cv.imread("..\\Resources\\Photos\\park.jpg")

cv.imshow("Boston", img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)

# +x --> Right
# +y --> Down
translated = translate(img, 100, 50)
cv.imshow("Translated", translated)

# Rotation
# +angle --> Clock Wise
def rotate(img, angle, rotPoint = None):
    dimension = img.shape[:2][::-1]
    if not(rotPoint):
        rotPoint = (dimension[0]//2, dimension[1]//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    return cv.warpAffine(img, rotMat, dimension)

# +x --> Right
# +y --> Down
rotated = rotate(img, 180)
cv.imshow("Rotated", rotated)

# Resizing 
resized = cv.resize(img, (500, 1000), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)

# Flip
# 0 --> x-axis
# 1 --> y-axis
# -1 --> x and y axis
flipped = cv.flip(img, -1)
cv.imshow("Flipped", flipped)

# Cropping Image
crop = img[100:300,200:400]
cv.imshow("Cropped", crop)


cv.waitKey(0)