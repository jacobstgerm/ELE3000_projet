import cv2

# Code from Patrick Artner https://stackoverflow.com/questions/48049886/how-to-correctly-check-if-a-camera-is-available
def testDevice(source):
   cap = cv2.VideoCapture(source) 
   if cap is None or not cap.isOpened():
       print('Warning: unable to open video source: ', source)

def record_video(output_path):
    # Open the webcam (default camera index is 0, you can change it if needed)
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Couldn't open")
    
    # Get the webcam's frame width and height
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # You can change the codec as needed
    videoFileName = 'test.mp4'
    out = cv2.VideoWriter(videoFileName, fourcc, frame_rate, (frame_width, frame_height))

    # Record video until the user presses 'q'
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Not able to read frame")
            break
        
        # Display the frame (optional, you can comment this line if you don't need to display)
        cv2.imshow('Video Recording', frame)

        # Write the frame to the output video file
        out.write(frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Specify the output path for the video file
    #output_path = "F:\\ELE3000\\VideoTest"  # Change the path and filename as needed

    # Start recording video
    #record_video(output_path)
    
    #Test camera
    #testDevice(2)
    import numpy as np
    import cv2

    cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
#fourcc = cv2.cv.CV_FOURCC(*'DIVX')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,0)

        # write the flipped frame
            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

