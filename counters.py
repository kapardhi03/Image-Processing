"""
Counters are just as edges but mathematically they are two different things
Identify edges
"""
import cv2 as cv
import numpy as np 

img = cv.imread("Photos/space.jpg")
cv.imshow("Space", img)


blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow("Blank", blank)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)


# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

#Edges
canny = cv.Canny(img, 125, 175)
cv.imshow("Edges", canny)



"""THreshold is used to bunarize a image"""
ret, threshold = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thres", threshold)


"""Counters are py list of all the counters in the image"""
"""ReterExternals - only outer"""
Counters, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"Number of counters in the image are {len(Counters)}")



cv.drawContours(blank, Counters, -1, (0,0,255), 1)
cv.imshow("Counters Drawn", blank)

cv.waitKey(12000)