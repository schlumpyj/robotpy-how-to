## Using code to send back webcam stream ##

[Docs and other example code](https://github.com/robotpy/robotpy-cscore)

1. Navigate to where your robotpy installer.py is. Mostly likely it will be in `Downloads/robotpy-VERSION_NUMBER/robotpy-VERSION_NUMBER/installer.py`

2. Type `py -3 installer.py --download-opkg python36-robotpy-cscore`

3. Connect to robot wifi and type `py -3 installer.py --install-opkg python36-robotpy-cscore`

4. Upload code like that seen in the `code-camera.py` file to the robot. You can do this easily by putting it in the directory where you write your robot code.

5. In your `robot.py` file, add a [line like this](https://github.com/bb20basketball/2017-Robot-Code/blob/master/robot.py#L51) with your file name. This will launch the code.
