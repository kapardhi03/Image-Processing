import cv2 as cv
from matplotlib import pyplot as plt


def COLOR_GRAY2HSV(gray_img):
    """
    Convert a grayscale image to the HSV color space.

    Args:
        gray_img: The input grayscale image.

    Returns:
        The converted HSV image.
    """
    # Convert grayscale to BGR
    gray_bgr = cv.cvtColor(gray_img, cv.COLOR_GRAY2BGR)
    
    # Convert BGR to HSV
    hsv_img = cv.cvtColor(gray_bgr, cv.COLOR_BGR2HSV)
    
    return hsv_img

def main():
    img = cv.imread("Photos/space.jpg")
    cv.imshow("Space", img)

    # Convert BGR to Grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray", gray)

    # Convert Grayscale to HSV
    hsv = COLOR_GRAY2HSV(gray)
    cv.imshow("HSV", hsv)

    # Demonstrate the conversion process
    plt.subplot(131), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title("Original")
    plt.subplot(132), plt.imshow(gray, cmap='gray'), plt.title("Grayscale")
    plt.subplot(133), plt.imshow(cv.cvtColor(hsv, cv.COLOR_HSV2RGB)), plt.title("Grayscale to HSV")
    plt.tight_layout()
    plt.show()

    # ... rest of the code ...

    cv.waitKey(1200)

if __name__ == '__main__':
    main()
