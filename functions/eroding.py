import cv2 as cv

img = cv.imread("../Photos/weather.jpg")
# cv.imshow("IMG", img)

canny = cv.Canny(img, 125, 175)
#Dialating
dilate = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilated", dilate)

eroded = cv.erode(dilate, (3,3), iterations=3)
cv.imshow("Eroded", eroded)

cv.waitKey(12000)