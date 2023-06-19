'''
This module contains the 'MotionDetectorApp' class for the motion detection user interface.

Usage:
    - Creates an instance of 'MotionDetectorApp'
    - Uses the 'run' method to start the application
'''

import tkinter as tk
import os
import cv2
from tkinter import messagebox

class MotionDetectorApp:
    def __init__(self):
        #Initializes the motion detector application
        self.logged_in = False #Variable to track if the user is logged in
        self.camera = cv2.VideoCapture(0) #Initializes the video capture from the default camera (index 0)
        self.recording = False #Variable to track if recording is in progress

        self.window = tk.Tk() #Creates the main application window
        self.window.title("Motion Detector")  #Sets the title of the window

        #Creates UI elements
        self.start_button = tk.Button(self.window, text="Real-time video", command=self.start_detection)
        self.start_button.pack(pady=10) #Button to start real-time video motion detection

        self.view_button = tk.Button(self.window, text="View Recordings", command=self.view_recordings, state=tk.DISABLED)
        self.view_button.pack(pady=10) #Button to view recorded videos (disabled by default)

        self.clear_button = tk.Button(self.window, text="Clear Recordings", command=self.confirm_clear_recordings, state=tk.DISABLED)
        self.clear_button.pack(pady=10) #Button to clear recorded videos (disabled by default)

        self.frame = tk.Frame(self.window)
        self.frame.pack(pady=20, padx=60)  #Frame to hold login-related UI elements

        self.username_label = tk.Label(self.frame, text="Username:")
        self.username_label.pack(pady=6, padx=10) #Label for username entry

        self.entry1 = tk.Entry(self.frame)
        self.entry1.pack(pady=6, padx=10) #Entry field for username

        self.password_label = tk.Label(self.frame, text="Password:")
        self.password_label.pack(pady=6, padx=10) #Label for password entry

        self.entry2 = tk.Entry(self.frame, show="*")
        self.entry2.pack(pady=6, padx=10) #Entry field for password

        self.button = tk.Button(self.frame, text="Login", command=self.login)
        self.button.pack(pady=6, padx=10) #Button to start login


    def start_detection(self):
        '''
        Starts the real-time video motion detection

        Requires the user to be logged in
        '''
        if self.logged_in:
            self.recording = True #Sets recording varablle to true
            self.start_button.config(state=tk.DISABLED) #Disables start button
            self.view_button.config(state=tk.DISABLED) #Disables view button
            self.clear_button.config(state=tk.DISABLED) #Disables clear button

            while self.recording:
                ret, frame = self.camera.read() #Reads video frame from the camera
                cv2.imshow("Video Feed", frame) #Displays the video frame in a window

                if cv2.waitKey(1) == ord("q"):
                    break

            cv2.destroyAllWindows() #Closes the video feed window
            self.start_button.config(state=tk.NORMAL) #Enables start button
            self.view_button.config(state=tk.NORMAL) #Enables view button
            self.clear_button.config(state=tk.NORMAL) #Enables clear button
        else:
            self.display_message("Please log in first.")

    def view_recordings(self):
        #Opens the directory containing the recorded videos in the default file explorer.
        directory = os.path.join(os.getcwd(), "recordings")
        if os.path.exists(directory) and os.path.isdir(directory):
            os.startfile(directory)  # Open the directory in the default file explorer
        else:
            self.display_message("No recordings found.")

    def confirm_clear_recordings(self):
        #Displays a confirmation message box before clearing the recorded videos
        response = messagebox.askquestion("Confirmation", "Are you sure you want to clear the recordings?")
        if response == "yes":
            self.clear_recordings()

    def clear_recordings(self):
        #Clears all the recorded videos from the recordings directory
        directory = os.path.join(os.getcwd(), "recordings")
        if os.path.exists(directory) and os.path.isdir(directory):
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            self.display_message("Recordings cleared successfully.")
        else:
            self.display_message("No recordings found.")

    def login(self):
        '''
        Logs user in to the motion detection application

        Checks the entered username and password (the one currently is username: woodroffe, password: 2023)
        '''
        username = self.entry1.get()
        password = self.entry2.get()
        if username == "woodroffe" and password == "2023":
            self.logged_in = True # Sets logged_in variable to True
            self.display_message("Logged in successfully.")
            self.start_button.config(state=tk.NORMAL) #Enables start button
            self.view_button.config(state=tk.NORMAL) #Enables view button
            self.clear_button.config(state=tk.NORMAL) #Enables clear button
        else:
            self.display_message("Invalid username or password.")

    def display_message(self, message):
        '''
        Displays a message in the application.

        Arguments:
            message: The message to be displayed
        '''
        self.message_label.config(text=message)

    def run(self):
        #Runs the whole motion detector module
        self.message_label = tk.Label(self.frame, text="")
        self.message_label.pack(pady=6, padx=10)
        self.window.mainloop()

if __name__ == "__main__":
    app = MotionDetectorApp() #Creates an instance of the MotionDetectorApp class
    app.run() #Runs the motion detector application