import cv2 as cv

img = cv.imread("../Photos/weather.jpg")
cv.imshow("BGR-Image", img)

# convert the BGR img to Gray image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

cv.waitKey(12000)