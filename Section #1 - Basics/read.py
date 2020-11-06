import cv2 as cv 


## Images
#img = cv.imread("../Resources/Photos/cat_large.jpg")

# Name of window, image
#cv.imshow("Cat", img)

# Delay for a keyboard key to be played
#cv.waitKey(0)



## Videos

capture = cv.VideoCapture("../Resources/Videos/dog.mp4")

isTrue, frame = capture.read()
while isTrue:
	cv.imshow("Dog", frame)
	isTrue, frame = capture.read()

	# waitKey ==> Sleep
	if cv.waitKey(10) & 0xFF == ord("q"):
		break

capture.release()
cv.destroyAllWindows()