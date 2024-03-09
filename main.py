import cv2

def record_video(output_path):
    # Open the webcam (default camera index is 0, you can change it if needed)
    cap = cv2.VideoCapture(0)

    # Get the webcam's frame width and height
    frame_width = int(cap.get(16))
    frame_height = int(cap.get(9))

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MJPEG')  # You can change the codec as needed
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (frame_width, frame_height))

    # Record video until the user presses 'q'
    while True:
        ret, frame = cap.read()

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
    output_path = "F:\ELE3000\VideoTest"  # Change the path and filename as needed

    # Start recording video
    record_video(output_path)

