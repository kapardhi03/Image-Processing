import cv2 as cv

capture = cv.VideoCapture("videos/SIH_YT.mov")

while True:
    try:
        #returns a boolean and frame 
        isTrue, frame = capture.read()

        #display that particular frame
        cv.imshow('Video', frame)

        #To stop inf running while, for 20 ms pause od when 'd; is pressed the while gets terminated
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    
    except Exception as e:
        print(f"Error Occured {e}")
        break

#releasing
capture.release()
#destroying all the windows
cv.destroyAllWindows()