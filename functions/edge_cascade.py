import cv2 as cv

img = cv.imread("../Photos/weather.jpg")
cv.imshow("BGR-Img", img)

#Edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)


cv.waitKey(12000)