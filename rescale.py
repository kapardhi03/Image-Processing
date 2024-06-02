import cv2 as cv

# img = cv.imread("Photos/3d5ca831-30f1-4664-b36a-cac81e4cc35e.jpg")
# cv.imshow('Weather', img)

#default function to rescale
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale) #width
    heigth = int(frame.shape[0] * scale) #heigth
    dimensions = (width, heigth)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def resize_img(pth):
    img = cv.imread(pth)
    cv.imshow('Weather', img)
    resized_img = rescaleFrame(img)
    cv.imshow("Resized", resized_img)

def resize_vid(pth):
    capture = cv.VideoCapture(pth)
    while True:
        try:
            #returns a boolean and frame 
            isTrue, frame = capture.read()

            #display that particular frame
            cv.imshow('Video', frame) #original

            resized_frame = rescaleFrame(frame)
            cv.imshow('Rescaled Video', resized_frame)

            #To stop inf running while, for 20 ms pause od when 'd; is pressed the while gets terminated
            if cv.waitKey(20) & 0xFF==ord('d'):
                break
        
        except Exception as e:
            print(f"Error Occured {e}")
            break

img = "Photos/3d5ca831-30f1-4664-b36a-cac81e4cc35e.jpg"
capture = "videos/SIH_YT.mov"
# resize_img(img)
resize_vid(capture)