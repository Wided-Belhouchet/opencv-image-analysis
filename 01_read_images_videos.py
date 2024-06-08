import cv2


def read_image(image_path: str) -> None:
    """
    Display on image given its file path
    Args:
        image_path(str):the path to the image file.
    """
    # Load the image from provided file path
    img = cv2.imread(image_path)
    # Display the image
    cv2.imshow("Image", img)
    # wait for a key to press to close the image window
    cv2.waitKey(0)


def read_video(video_path: str) -> None:
    """
    display an image given its file path ...
    """
    # define the frame dimension
    framewidth = 640
    frameheight = 480
    # create a videoCapture object to read the video from the provided file path
    cap = cv2.VideoCapture(video_path)
    while True:
        # Read a frame from the video
        success, img = cap.read()
        # Check if the frame was read successfully
        if not success:
            break
        # Resize the frame to specified dimensions
        img = cv2.resize(img, (framewidth, frameheight))
        # display the frame
        cv2.imshow("Video", img)
        # check for the 'q' key press to exit the video
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def read_webcam(framewidth: int = 640, frameheight: int = 480, brightness: int = 150) -> None:
    """
    display an image given its file path ...
    """
    # create a videoCapture object to read the video from the provided file path
    cap = cv2.VideoCapture(0)
    # set the frame dimensions
    cap.set(3, framewidth)
    cap.set(4, frameheight)

    # set the frame brightness level
    cap.set(10, brightness)
    while True:
        # Read a frame from the video
        success, img = cap.read()
        # Check if the frame was read successfully
        if not success:
            break
        # Resize the frame to specified dimensions
        img = cv2.resize(img, (framewidth, frameheight))
        # display the frame
        cv2.imshow("Video", img)
        # check for the 'q' key press to exit the video
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    # read_image("Resources/image1.png")
    # read_image("Resources/image2.png")
    read_webcam()
