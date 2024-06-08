import cv2
import numpy as np


def process_image(image_path: str) -> None:
    # Load the image from the provided file path
    img = cv2.imread(image_path)

    # Define a kernel for morphological operations
    kernel = np.ones((5, 5), np.uint8)  # Fixed typo in np.unit8 to np.uint8

    # Convert the image to grayscale
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale image
    imgblur = cv2.GaussianBlur(imggray, (7, 7), 0)  # Fixed typo in cv2.GauusianBlur to cv2.GaussianBlur

    # Apply Canny edge detection to the original image
    imgcanny = cv2.Canny(img, 150, 200)

    # Perform dilation on the Canny edge image
    imgdilation = cv2.dilate(imgcanny, kernel, iterations=1)

    # Perform erosion on the dilated image
    imgeroded = cv2.erode(imgdilation, kernel, iterations=1)  # Fixed cv2.dilate to cv2.erode

    # Display the processed images
    cv2.imshow('GrayImage', imggray)
    cv2.imshow('BlurImage', imgblur)
    cv2.imshow('CannyImage', imgcanny)
    cv2.imshow('DilationImage', imgdilation)
    cv2.imshow('ErodedImage', imgeroded)

    # Wait for a key press to close the image windows
    cv2.waitKey(0)


if __name__ == '__main__':
    image_path = "Resources/image1.png"  # Replace with the path to your image
    process_image(image_path)
