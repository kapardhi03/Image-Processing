import cv2 as cv

img = cv.imread("Photos/space.jpg")
cv.imshow("img", img)

#Thresholding is used to make any picture into a binary image, ig the pixel val is lessthan threshold it is 0 else 1
#Two types of threshold 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# 1.Simple Threshold              150 is threshold
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)


# inversing the threshold sets which are less thatn thres to 255
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Thresh_in", thresh_inv)



# 2.Adaptive Thresholding
adaptive_thres = cv.adaptiveThreshold(gray, 255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv.THRESH_BINARY, blockSize=11, C=3)
cv.imshow("Adaptive Thresholding", adaptive_thres)


cv.waitKey(120000)