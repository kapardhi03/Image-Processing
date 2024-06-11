import cv2 as cv
import numpy as np 

img = cv.imread("Photos/space.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Laplacion
lap = cv.Laplacian(gray, ddepth=cv.CV_64F)
lap = np.uint8(np.absolute(lap)) ## coz img cannot have -ve values
cv.imshow("Laplasian", lap)



# sobel 
sobelx = cv.Sobel(gray, ddepth=cv.CV_64F, dx=1, dy=0)
sobely = cv.Sobel(gray, ddepth=cv.CV_64F, dx=0, dy=1)

cv.imshow("SobelX", sobelx)
cv.imshow("SobelY", sobely)


combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow("combined", combined_sobel)


# canny is more used and sabby then

cv.waitKey(12000)