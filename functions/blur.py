import cv2 as cv

img = cv.imread("../Photos/weather.jpg")
cv.imshow("BGR-Img", img)

# Blur the image 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

cv.waitKey(12000)