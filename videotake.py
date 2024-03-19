import cv2 as cv
import winsound
import time

def videotake(profile, fourcc, cap):
    out = cv.VideoWriter(f'C:/ELE3000/Video/{profile}/{time.time()}.avi', fourcc, 60.0, (1920, 1080))

    first_frame = False
    #print("Press 's' to start video")
    while cap.isOpened():
 # Capture frame-by-frame
        while not(first_frame):
            start = "s" + input("Press enter to start\n")
            if (start == "s"):
                first_frame = True
                winsound.PlaySound('C:/Git/ELE3000/beep-09.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

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