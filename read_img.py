import cv2

image = cv2.imread("Photos/3d5ca831-30f1-4664-b36a-cac81e4cc35e.jpg")

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()