'''
This module contains the 'Recorder' class for recording frames into video files.

Usage:
    - Creates an instance of 'Recorder' with the desired frame size
    - Uses the 'start_recording' method to start recording frames
    - Uses the 'record_frame' method to record individual frames
    - Uses the 'stop_recording' method to stop the recording and save the video file
    - Releases the recorder using the 'release' method when done

'''

import cv2
import time
import datetime
import os

class Recorder:
    def __init__(self, frame_size):
        '''
        Initializes the recorder with the desired frame size.

        Arguments:
            frame_size: The size of the frames (width, height).
        '''
        self.fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.frame_size = frame_size
        self.out = None

    def start_recording(self):
        '''
        Starts recording frames to a video file

        The video files will be saved with the current timestamp as the filename (format is %d-%m-%Y-%H-%M-%S)
        '''
        current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        directory = "recordings"
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = os.path.join(directory, f"{current_time}.mp4")
        self.out = cv2.VideoWriter(filename, self.fourcc, 5, self.frame_size)
        print("Motion detected!")

    def stop_recording(self):
        #Stops the recording and releases the video 
        if self.out is not None:
            self.out.release()
            self.out = None
            print('No motion detected!')

    def record_frame(self, frame):
        '''
        Record an individual frame.

        Arguments:
            frame: The frame to be recorded
        '''
        if self.out is not None:
            self.out.write(frame)

    def is_recording(self):
        '''
        Checks to see if the recorder is currently recording

        Returns:
            True if recording, false otherwise
        '''
        return self.out is not None

    def release(self):
        #Releases and frees resources
        if self.out is not None:
            self.out.release()