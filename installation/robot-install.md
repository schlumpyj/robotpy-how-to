## Make sure the laptop is setup before installing the robot software ##

1. Now connect to the robot’s WiFi network and type `py installer.py install-robotpy`

2. Go to `Downloads/robotpy-wpilib-utilities/robotpy-wpilib-utilities/` in the FILE EXPLORER. 

3. Make a new folder that says something like `XXXXCode` where XXXX is like 2018

4. Find `IDLE` on the computer and click enter

5. Then do CTRL+N for a new file

6. Start programming, making sure that you have `#!/usr/bin/env python3` at the top of your new python file

7. Save As the file to your XXXXCode directory you just created (Only robot.py as a saved file name will deploy to the robot, any other names will not be!)

8. To upload the code, go to the code folder, and under command do `py robot.py deploy` while in the directory of your code in the command prompt

9. If the Deploy was successful, you should be able to drive the robot as needed

10. To test code without deploying, just do `py robot.py sim` to run the nice simulator to test your code.
