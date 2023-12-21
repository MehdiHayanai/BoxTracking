import cv2


# Callback function to handle mouse events
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(f"x: {x}, y: {y}")


# Load your image
frames = []
video_path = "video/box_video_data.avi"
cap = cv2.VideoCapture(video_path)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # read the frame as gray image
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames.append(frame_gray)

image = frames[3]
# Create a window and set the mouse callback function
cv2.namedWindow("Hover Image")
cv2.setMouseCallback("Hover Image", on_mouse)

# Display the image and wait for a mouse event
cv2.imshow("Hover Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
