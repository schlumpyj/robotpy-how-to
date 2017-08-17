#!/usr/bin/env python3

import wpilib # <---- main library with all the necessary code for controlling FRC robots
import wpilib.buttons # <---- for joystick buttons
import networktables # <--- the library that allows us to do the cool data stuff
from robotpy_ext.common_drivers import navx # <--- needed to get data from our gyro

class MyRobot(wpilib.IterativeRobot): # <---- IternativeRobot means that it loops over and over by itself like a while loop

    def robotInit(self):

        self.robotStats = NetworkTable.getTable('SmartDashboard') #The table name is what you will reference on the laptop
        self.navx = navx.AHRS.create_spi() #the Gyro

    def disabledPeriodic(self):

        """
            Runs constantly while disabled
        """

        # Just sends back the current yaw of the navx
        self.robotStats.putNumber('NavXYaw', self.navx.getYaw())


if __name__ == "__main__":
    wpilib.run(MyRobot) #runs the code!
