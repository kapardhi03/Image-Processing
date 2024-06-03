import cv2 as cv
import numpy as np

img = cv.imread("Photos/weather.jpg")
cv.imshow("IMG", img)

#Translation 
def translate(img, x, y):
    """
    img -> image
    x -> no. of pixels to shift in X axes
    y -> no. of pixels to shift in y axes
    """
    translattion_matrix = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) # (width, height)

    return cv.warpAffine(img, translattion_matrix, dimensions)

"""
-x -> Left
-y -> Up
x -> Right
y -> Down
"""

# translated = translate(img, 100, 100)
translated = translate(img, -100, 100)
cv.imshow("Translated Img", translated)


#Rotation 
"""Rotating an img by an angel"""
def rotate(img, angel, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint == None:
        rotPoint = (width//2, height//2)
    
    rotationMatrix = cv.getRotationMatrix2D(rotPoint, angel, scale=1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotationMatrix, dimensions)

"""
+ve angle -> counter clock
-ve angel -> clock wise
"""
rotated = rotate(img, -45)
cv.imshow("Rotated", rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow("Rotated Rotated", rotated_rotated)


# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC )
cv.imshow("Resized", resized)


#Flipping
"""
0 -> vertical flip 
1 -> horizontal flip
-1 -> Both Horizontal and vertical flip
"""
flip = cv.flip(img, 0) 
cv.imshow("vertical flip", flip)

flip = cv.flip(img, 1)
cv.imshow("Horizontal flip", flip)

cv.waitKey(12000)