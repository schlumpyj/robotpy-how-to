#!/usr/bin/env python3

import wpilib # <---- main library with all the necessary code for controlling FRC robots
import wpilib.buttons # <---- for joystick buttons
from robotpy_ext.autonomous import AutonomousModeSelector # <--- Easily allows you to select auto mode from laptop

class MyRobot(wpilib.IterativeRobot): # <---- IternativeRobot means that it loops over and over by itself like a while loop

    def robotInit(self):

        """
            Define all motor controllers, joysticks, Pneumatics, etc. here so you can use them in teleop/auton
        """

        self.drive_motor1 = wpilib.Talon(0) # <--- or whatever motor controller you are using
        self.drive_motor2 = wpilib.Talon(1)

        self.robot_drive = wpilib.RobotDrive(self.drive_motor1, self.drive_motor2) # <--- says to robot that these motors work together to drive robot

        self.xboxController = wpilib.Joystick(0) # <--- joystick, does not have to be an xbox controller

        self.components = { # Add all the objects you are going to want in autonomous like sensors, the robot drive, etc.
            'drive': self.robot_drive #give it a nickname as well. In this case, we "nicknamed" self.robot_drive as 'drive' so in auto you will do self.drive
        }

        self.automodes = AutonomousModeSelector('auto-modes', self.components) #pass in the folder with all your auto modes and the components you want in auto

    def autonomousPeriodic(self):

        self.automodes.run()

if __name__ == "__main__":
    wpilib.run(MyRobot) #runs the code!
