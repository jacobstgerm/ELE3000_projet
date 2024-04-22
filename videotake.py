import cv2 as cv
import winsound
import datetime
import os
from os import listdir

def videotake(profile, fourcc, cap, fps, width, height):
    date = ((datetime.datetime.now().strftime("%x")).replace('/', '_') + '_')
    i = 0
    folder_dir = f"C:/Git/ELE3000/ELE3000_projet/Video/{profile}"
    # try:
    for images in os.listdir(folder_dir):
        i+=1
    # except:
    #     i=0
    out = cv.VideoWriter(f'C:/Git/ELE3000/ELE3000_projet/Video/{profile}/{date}{i}.avi', fourcc, fps, (width, height))
    # first_frame = True
    winsound.PlaySound('C:/Git/ELE3000/beep-09.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    while cap.isOpened():

        ret, frame = cap.read()
        # if first_frame:
        #     winsound.PlaySound('C:/Git/ELE3000/beep-09.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        #     first_frame = False
 # if frame is read correctly ret is True
        if ret:
            cv.imshow('frame', frame)
            out.write(frame)
            if cv.waitKey(1) == ord('q'):
                break
        else:
            break
    cap.release()
    cv.destroyAllWindows()