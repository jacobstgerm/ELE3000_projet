import cv2 as cv
import winsound
import time
from videotake import videotake

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


    while True:
        profile = input("Choose profile (1 to 10)\n")
        try:
            if (int(profile) >= 1 and int(profile) <= 10):
                break
        except:
            print("Input is not numerical")
        print("Profile could not be recognized")
    print(f"Profile number {profile} selected")
        

    videotake(profile, fourcc, cap)
 
# When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
