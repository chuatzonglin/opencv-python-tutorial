import cv2 as cv

img = cv.imread("..\\Resources\\Photos\\park.jpg")
cv.imshow("Cat", img)

# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Gaussion Blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Gaussian Blur", blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# Dilation
dilated = cv.dilate(canny, (3,3), iterations=10)
cv.imshow("Dilated", dilated)

# Eroded
erode = cv.erode(dilated, (3,3), iterations=10)
cv.imshow("Eroded", erode)

# Resize
#cv.INTER_AREA ==> shrinking image
#cv.INTER_CUBIC & cv.INTER_LINEAR ==> Enlarge Image
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resize)

# Cropping Image
crop = img[100:300,200:400]
cv.imshow("Cropped", crop)

cv.waitKey(0)
