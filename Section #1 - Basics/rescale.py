import cv2 as cv 

# Images, Live and Existing videos
def rescaleFrame(frame, scale = 0.75):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Live video only
def changeRes(width, height):
	capture.set(3, width)
	capture.set(4, height)

# Live webcam capture
#capture = cv.VideoCapture(0)
#changeRes(0.75, 1)

capture = cv.VideoCapture("../Resources/Videos/dog.mp4")
isTrue, frame = capture.read()
while isTrue:
	cv.imshow("Dog1", frame)
	#cv.imshow("Dog1", frame)
	#cv.imshow("Dog2", rescaleFrame(frame))
	isTrue, frame = capture.read()
	if cv.waitKey(20) & 0xFF == ord("q"):
		break

capture.release()
cv.destroyAllWindows()