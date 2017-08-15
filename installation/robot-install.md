## Robot Install ##

----- Make sure the laptop is setup before installing the robot software ----

1. Go to `Downloads/robotpy-VERSION_NUMBER/robotpy-VERSION_NUMBERs/` in the FILE EXPLORER where the VERSION_NUMBER will be like 2017.1.2

2. Now connect to the robot’s WiFi network and type `py -3 installer.py install-robotpy`

3. If you plan on using the fancy CAN Talons, simply install using the opkg option with the installer.py. See the [exact command here.](https://github.com/robotpy/robotpy-ctre#setup-roborio) *Don't forget to import ctre into your code later on!*

4. Make a new folder that says something like `XXXXCode` where XXXX is like 2018 anywhere on the computer, but Desktop is a good place for it (easy to find).

5. Find `IDLE` on the computer and click enter

6. Then do CTRL+N for a new file

7. Start programming, making sure that you have `#!/usr/bin/env python3` at the top of your new python file

8. Save As the file to your XXXXCode directory you just created (Only robot.py as a saved file name will deploy to the robot, any other names will not be!)

9. To upload the code, go to the code folder, and under command do `py -3 robot.py deploy` while in the directory of your code in the command prompt

10. If the Deploy was successful, you should be able to drive the robot as needed

11. To test code without deploying to the robot, just do `py robot.py sim` to run the nice simulator to test your code.
