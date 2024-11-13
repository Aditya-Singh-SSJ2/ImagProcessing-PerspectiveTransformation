import cv2
import numpy as np

# Reading a video file with cv2
vidcap = cv2.VideoCapture("myDemoVideo.mp4")
success, image = vidcap.read()

while success:
    success, image = vidcap.read()
    frame = cv2.resize(image, (640,480))

    # Perspective Transformation

    # selecting coordinates
    tl = (222, 387)
    bl = (70, 472)
    tr = (400, 380)
    br = (538, 472)

    cv2.circle(frame, tl, 5, (0,0,255), -1)
    cv2.circle(frame, bl, 5, (0,0,255), -1)
    cv2.circle(frame, tr, 5, (0,0,255), -1)
    cv2.circle(frame, br, 5, (0,0,255), -1)

    # Apply Perspective transformation - Geometrical transformation
    pts1 = np.float32([tl, bl, tr, br])
    pts2 = np.float32([[0,0], [0,480], [640,0], [640,480]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    transformed_frame = cv2.warpPerspective(frame, matrix, (640,480))

    cv2.imshow("Frame", frame)
    cv2.imshow("Transformed_Frame", transformed_frame)

    if cv2.waitKey(1)==27: #ESC Key
        break