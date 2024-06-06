import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/space.jpg")
cv.imshow("Space", img)

# plt.imshow(img)  # this shows the RGB image but the opencv by default read every image as the bgr
# plt.show()


"""Grayscale to BGR and BGR to HSV"""


#BGR to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR to HSV ( Hue Saturation Value )
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)


# BGR to LAB -> l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)


rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

plt.imshow(rgb)  # now you get an inversion because we changed the bgr to rgb in opencv
plt.show()

cv.waitKey(1200)