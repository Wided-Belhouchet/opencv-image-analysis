import cv2


def process_image(image_path: str) -> None:
    """
    Load an image, display its original shape, resize it, and crop a region of the image.

    Args:
        image_path (str): the path of the image file
    """
    # Load the image from the provided file path
    img = cv2.imread(image_path)

    # Display the original image shape
    print("Original Image shape:", img.shape)

    # Resize the image to the specified dimensions
    imgresize = cv2.resize(img, (1000, 500))
    print("Resized Image shape:", imgresize.shape)

    # Crop a region of the image
    imgcropped = img[46:119, 352:495]

    # Display the original and cropped images
    cv2.imshow("Original Image", img)
    cv2.imshow("Resized Image", imgresize)
    cv2.imshow("Cropped Image", imgcropped)

    # Wait for a key press to close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image_path = "Resources/image2.png"
    process_image(image_path)
