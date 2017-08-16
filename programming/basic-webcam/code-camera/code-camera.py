import cv2
import numpy as np

from cscore import CameraServer

"""
    Code from 2017 Robot
"""

def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    camera = cs.startAutomaticCapture()

    camera.setResolution(160, 120)
    camera.setFPS(20)
    # Get a CvSink. This will capture images from the camera
    cvSink = cs.getVideo()

    # (optional) Setup a CvSource. This will send images back to the Dashboard
    outputStream = cs.putVideo("Rectangle", 320, 240)

    # Allocating new images is very expensive, always try to preallocate
    img = np.zeros(shape=(120, 160, 3), dtype=np.uint8)

    while True:

        time, img = cvSink.grabFrame(img)
        if time == 0:
            # Send the output the error.
            outputStream.notifyError(cvSink.getError());
            # skip the rest of the current iteration
            continue

        # Give the output stream a new image to display
        outputStream.putFrame(img)
