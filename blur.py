"""
we use the blur to reduce the noise
"""
import cv2 as cv
import numpy as np
img = cv.imread("Photos/space.jpg")
cv.imshow("Original", img )

# 1. Averaging :
"""
The intesity or the value of the current grid will be the average value of all the surrounding pixels
Window is created for all
"""
# The second parameter will be the window size
average = cv.blur(img, (7,7))
cv.imshow("Blur", average)

print("Img-Shape", np.shape(img))
print("Blur-Shape", np.shape(average))
# both the images will have the same shape as expected 



# 2.Guassian Blur
"""
Does the same thing as avg
Each surrounding picture is given a weight, and avg of that weight is takn 
We get the less blur but more natural
"""
guass = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("GB", guass)



# 3. Median blur
"""
Same thing as avg,  but it finds the median of other picture .
more effective in removing the noise comparitively.
"""
median = cv.medianBlur(img, 3) # 7X7 not meant for 7
cv.imshow("MB", median)


# 4. Bilateral 
"""
It applies the blur by retaining the edges
"""
bilateral = cv.bilateralFilter(img, 20, 35, 25)
cv.imshow("BB", bilateral)

cv.waitKey(12000)