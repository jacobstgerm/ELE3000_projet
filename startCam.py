import cv2 as cv    

def startCam():
    cap = cv.VideoCapture(1)
    # cap.set(cv.CAP_PROP_FRAME_WIDTH,640)
    # cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    # width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    # height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    width = 640
    height = 480
    # print("Dimensions set", width, height)
    # print(cap.get(5))
    # cap.set(5,30.0)
    # fps = int(cap.get(5))
    fps = 30
    # print("Frame rate set", fps)
    fourcc = cv.VideoWriter_fourcc(*'DIVX')

    return [cap, width, height, fps, fourcc]