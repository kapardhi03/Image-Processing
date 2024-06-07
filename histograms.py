"""
we can construct histogram for grayscale and rgb images 
"""
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/space.jpg")
cv.imshow("IMG", img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

# # GrayScale histogram
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title("GrayScale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


# Color Histogram (RGB)
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()



# we can also mask the image and get the histogram for the images

cv.waitKey(12000)