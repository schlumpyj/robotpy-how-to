## Basic Webcam ##

In many games, a Webcam can be very useful for the driver to see what they are doing. We also have a great big driver station monitor made just for this purpose of being able to see where your eyesight fails you.

There is two main approaches in RobotPy to this issue and I've used both.

1. Use code to send back the webcam stream

2. Use mjpg-streamer to send back webcam stream

If possible, please use the mjpg-streamer. I did not like using the code way. In the beginning of the 2017 season, the Python creator cut support for it, but it appears that he updated it so it should work again.

The code way is awesome if you want to draw a crosshairs on the image or do some basic vision with OpenCV. Just keep in mind that it does tax the roboRIO CPU and can slow down the robot if you do too much processing!
