import cv2 as cv

img = cv.imread("../Photos/weather.jpg")

resized = cv.resize(img, (500,500))
cv.imshow("REsied", resized)


resized = cv.resize(img, (700,700), interpolation=cv.INTER_CUBIC)
cv.imshow("New Resized", resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped img", cropped)

cv.waitKey(12000)