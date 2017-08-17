## Web Server ##

If you want to be able to see the webcam and other data from the Driver Station, you are going to need a web server running on the driver station laptop.

### Installation ###

[Here it outlines a new, easier way to install the pynetworktables2js on Windows.](https://github.com/robotpy/pynetworktables2js#installation)

I have never used that easy install, but it looks solid. Just make sure to use the --help option to see how to designate the IP address of the robot.

**Also, you will probably need to install pynetworktables using pip like `pip install pynetworktables` and both Python 2 and 3 versions**

### Code Example ###

I have put in here a basic example of a webcam and autonomous mode selector. You can add elements like dials and gauges like I did in 2017 for things like PSI and whatnot. You will need to make sure you are sending that data from the robot's networktables. [If you don't know what that is or how to do it, look here.]()

See the full [2017 Webpage code here.](https://github.com/bb20basketball/Virtual-Birds-Eye-View/blob/master/www/index.html)
