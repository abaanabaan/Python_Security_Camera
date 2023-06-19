'''
This module contains the 'Camera' class for capturing frames from a video source.

Usage:
    - Creates an instance of 'Camera'
    - Uses the 'read_frame' method to read frames from the video source
    - Releases the camera using the 'release' method when done

'''

import cv2

class Camera:
    def __init__(self, video_source=0):
        '''
        Initializes the camera by opening the video source (0 stands for default camera) and getting the frame size.

        Arguments:
            video_source: Video source (webcam in this case)
        '''
        self.cap = cv2.VideoCapture(video_source)
        self.frame_size = (int(self.cap.get(3)), int(self.cap.get(4)))

    def read_frame(self):
        '''
        Reads a frame from the video source

        Returns:
            The captured frame
        '''
        _, frame = self.cap.read()
        return frame

    def release(self):
        #Releases the camera and frees resources
        self.cap.release()