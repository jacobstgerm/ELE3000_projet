import cv2 as cv

def showImage(filepath):
    img = cv.imread(filepath)
    cv.imshow('Result', img)
    cv.waitKey(0)
    cv.destroyAllWindows()