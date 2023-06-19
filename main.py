'''
- Submission date: 

- Group members: Abaan Noman, Abdullah Shibib, Angkush Moosai

Program description: 
This program is a motion detection application that utilizes a camera feed. 
It begins by initializing the camera, detector, and recorder objects. 
The program then enters a loop to continuously read frames from the camera feed.
Each frame is converted to grayscale, and the detector detects faces and bodies in the grayscale frame. 
If motion is detected, the program starts recording. If no motion is detected, it checks if the specified duration has passed since motion stopped. 
If the duration has passed, the program stops recording and exits the loop.
The recorded frames are saved as videos. The program also draws rectangles around the detected faces on the frame and displays the frame in a window. 
The 'q' key can be used to exit the program.
Furthermore, the program releases the resources used by the recorder, camera, and windows. 
In addition, it provides a user interface for real-time video viewing, login functionality, and viewing/clearing recorded videos.

- No known bugs
'''
import cv2
import time
import datetime
from camera import Camera
from detector import Detector
from recorder import Recorder
from user_interface import MotionDetectorApp

#Creates and initializes instances of Camera, Detector, and Recorder
cap = Camera()  
detector = Detector()  
recorder = Recorder(cap.frame_size)  

# Initializes variables for motion detection
detection = False  #Variable to indicate if motion is currently detected
detection_stopped_time = None  #Time when motion stopped being detected
timer_started = False  #Variable to indicate if the timer has started for recording after motion stops
SECONDS_TO_RECORD_AFTER_DETECTION = 5  #Duration to record after motion stops (in seconds)

while True:
    #Reads a frame from the camera
    frame = cap.read_frame()

    #Converts the frame to grayscale for more efficient face and body detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detects faces and bodies in the grayscale frame
    faces, bodies = detector.detect(gray)

    if len(faces) + len(bodies) > 0:
        #Motion is being  detected
        if detection:
            timer_started = False  #Resets the timer if motion is still being detected
        else:
            detection = True  #Sets the variable to indicate motion detection
            recorder.start_recording()  #Starts recording when motion is first detected
    elif detection:
        #Motion is no longer detected
        if timer_started:
            #Checks to see if the specified duration has passed since motion stopped
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False  #Resets the motion detection variable
                timer_started = False  # Resets the timer variable
                recorder.stop_recording()  #Stops recording after the specified duration
                break  #Exits the loop and ends the program

        else:
            timer_started = True  #Starts the timer if motion has just stopped
            detection_stopped_time = time.time()  #Records the time when motion stopped

    recorder.record_frame(frame)  # Record the frame

    #Draws rectangles around the detected faces on the frame (looks cool)
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    cv2.imshow("Camera", frame)  #Displays the frame with the detected faces

    if cv2.waitKey(1) == ord('q'):
        break  #Exits the loop and end the program if 'q' key is pressed

#Release resources
recorder.release()  #Releases the recorder resources
cap.release()  #Releases the camera resources
cv2.destroyAllWindows()  #Closes all OpenCV windows

#Creates an instance of the MotionDetectorApp and runs it
app = MotionDetectorApp()
app.run()