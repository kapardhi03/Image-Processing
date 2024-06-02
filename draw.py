import cv2 as cv
import numpy as np

# np array with 500X500 zeros which give a blank img [ uint8 is dtype of an img]
blank = np.zeros((500,500,3), dtype='uint8')  # giving height, width, no.of color channels
# cv.imshow("BlankIMG", blank)

# img = cv.imread("Photos/weather.jpg")
# cv.imshow('Telangana Weather Man', img)

# 1/ Print the image a certain colour
# blank[:] = 0,255,0 # green
# cv.imshow("Green", blank)

# blank[:] = 0,0,255 #red
# cv.imshow("RED", blank)

# blank[:] = 0,0,0
# blank[200:250, 300:400] = 0,0,225 #red
# cv.imshow("Partial colored", blank)


# #Draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness=2)
# cv.imshow("Rectangle", blank)
# cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness=cv.FILLED) #or 
# cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness=-1)
# cv.imshow("Rectangle", blank)



# Draw a circle
# """Give coordinates of center"""
# cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
# cv.imshow("Circle", blank)


# draw a line
# cv.line(blank, (100,0), (250,250), (255,255,255), thickness=3)
# cv.imshow("Line", blank)



# write a Text 
cv.putText(blank, "Ghost!", (blank.shape[0]//2, blank.shape[1]//2), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), 2)
cv.imshow("Text", blank)


cv.waitKey(5000)