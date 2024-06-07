import cv2 as cv
import numpy as np

img = cv.imread("Photos/space.jpg")
cv.imshow("IMG", img)

# Important thing is dimensions of the mask must be same as the dimensions of the image
blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank", blank)


# now drawing a circle over the blank image and call it as mask
mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 250, 255, -1)
# cv.imshow("Mask", mask)


rect_mask = cv.rectangle(blank.copy(), (img.shape[1]//2+200, img.shape[0]//2+150), (img.shape[1]//2-400, img.shape[0]//2-250), 255, -1)
cv.imshow("Rectangle_Mask", rect_mask)


masked_img = cv.bitwise_and(img, img, mask=mask )
cv.imshow("Masked Sattellite", masked_img)


rect_masked = cv.bitwise_and(img, img, mask=rect_mask)
cv.imshow("Rect_MAsk", rect_masked)



cv.waitKey(0)