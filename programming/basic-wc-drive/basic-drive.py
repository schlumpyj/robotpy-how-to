#!/usr/bin/env python3

import wpilib # <---- main library with all the necessary code for controlling FRC robots
import wpilib.buttons # <---- for joystick buttons

class MyRobot(wpilib.IterativeRobot): # <---- IternativeRobot means that it loops over and over by itself like a while loop

    def robotInit(self):

        """
            Define all motor controllers, joysticks, Pneumatics, etc. here so you can use them in teleop/auton
        """

        self.drive_motor1 = wpilib.Talon(0) # <--- or whatever motor controller you are using
        self.drive_motor2 = wpilib.Talon(1)

        self.robot_drive = wpilib.RobotDrive(self.drive_motor1, self.drive_motor2) # <--- says to robot that these motors work together to drive robot

        self.xboxController = wpilib.Joystick(0) # <--- joystick, does not have to be an xbox controller


    def teleopInit(self):

        """
            Put code in here that you want ran once before teleop starts.
            I use it for timers and counters.
        """
        pass

    def teleopPeriodic(self):

        """
            Human controlled period
        """

        self.robot_drive.arcadeDrive(self.xboxController.getY(), self.xboxController.getX(), True) # <--- sends the command to drive the robot

if __name__ == "__main__":
    wpilib.run(MyRobot) #runs the code!
