## Robot Install ##

----- Make sure the laptop is setup before installing the robot software ----

1. Go to `Downloads/robotpy-VERSION_NUMBER/robotpy-VERSION_NUMBERs/` in the FILE EXPLORER where the VERSION_NUMBER will be like 2017.1.2

2. Now connect to the robot’s WiFi network and type `py -3 installer.py install-robotpy`

3. Make a new folder that says something like `XXXXCode` where XXXX is like 2018 anywhere on the computer, but Desktop is a good place for it (easy to find).

4. Find `IDLE` on the computer and click enter

5. Then do CTRL+N for a new file

6. Start programming, making sure that you have `#!/usr/bin/env python3` at the top of your new python file

7. Save As the file to your XXXXCode directory you just created (Only robot.py as a saved file name will deploy to the robot, any other names will not be!)

8. To upload the code, go to the code folder, and under command do `py -3 robot.py deploy` while in the directory of your code in the command prompt

9. If the Deploy was successful, you should be able to drive the robot as needed

10. To test code without deploying to the robot, just do `py robot.py sim` to run the nice simulator to test your code.
