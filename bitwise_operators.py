"""
And OR XOR NOT
used when working with masks
"""
import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 225, -1)

circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)


# AND
""" Place them on top and returns the intersection """
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("AND", bitwise_and)

# OR
""" Returns the union """
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("OR", bitwise_or)


#XOR 
""" returns non intersectiopn region """
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("XOR", bitwise_xor)


# NOT
""" doesnt returrns anythiong but inverts the bnary color"""
bitwise_not = cv.bitwise_not(circle)
cv.imshow("NOT", bitwise_not)

cv.waitKey(120000)