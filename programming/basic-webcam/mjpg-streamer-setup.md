## MJPG-streamer Webcam Setup ##

[MJPG-streamer page](https://github.com/robotpy/roborio-packages/tree/2017/ipkg/mjpg-streamer)

1. Navigate to where your robotpy installer.py is. Mostly likely it will be in `Downloads/robotpy-VERSION_NUMBER/robotpy-VERSION_NUMBER/installer.py`

2. Type `py -3 installer.py --download-opkg mjpg-streamer`

3. Connect to robot wifi and type `py -3 installer.py --install-opkg mjpg-streamer`

4. Reboot system with webcam plugged in on a USB port. The stream will, by default, be at `ROBOT_IP_ADDRESS:5800` where `ROBOT_IP_ADDRESS` could be 10.44.80.2

### To change resolution or frame rate ###

1. SSH into the roboRIO using a program like Putty on Windows. (user: admin, password: *no password*)

2. Type `vi /etc/default/mjpg-streamer`

3. Things should be pretty easy from then on. Google how to exit and save in vi editor if you are stuck trying to save or exit the file. Reboot for changes to take effect. Also look at the page I linked above, it has helped commands.
