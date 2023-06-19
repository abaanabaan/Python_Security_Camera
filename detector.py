'''
This module contains the 'Detector' class for detecting faces and bodies in frames.

Usage:
    - Creates an instance of 'Detector'
    - Use the 'detect' method to detect faces and bodies in a grayscale frame
'''

import cv2

class Detector:
    def __init__(self):
        #Initializes the detector by loading the Haar cascade classifiers for face and body detection.
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.body_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_fullbody.xml")

    def detect(self, gray_frame):
        '''
        Detects faces and bodies in the provided grayscale frame.
        Arguments:
            gray_frame: Grayscale frame for detection.

        Returns:
            Tuple: A tuple containing the detected faces and bodies as rectangles (x, y, width, height).
        '''
        faces = self.face_cascade.detectMultiScale(gray_frame, 1.3, 5)
        bodies = self.body_cascade.detectMultiScale(gray_frame, 1.3, 5)
        return faces, bodies