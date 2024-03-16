import cv2 as cv
import numpy as np
import os

if __name__ == "__main__":
    # Specify the output path for the video file
    #output_path = "F:\\ELE3000\\VideoTest"  # Change the path and filename as needed

    # Start recording video
    #record_video(output_path)
    #Code from cv2 documentation in parts https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
    #Data path code in parts from Jeru Luke https://stackoverflow.com/questions/41586429/opencv-saving-images-to-a-particular-folder-of-choice
    #path = "F:\ELE3000\VideoTest"
    cap = cv.VideoCapture(1)
    cap.set(3,1920)
    print("Dimensions set")
    cap.set(5,60.0)
    print("Frame rate set")
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('F:/ELE3000/VideoTest/output.avi', fourcc, 60.0, (1920, 1080))

    while cap.isOpened():
 # Capture frame-by-frame
        ret, frame = cap.read()
 
 # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        out.write(frame)
 # Display the resulting frame
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
 
# When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
    cv.destroyAllWindows()
