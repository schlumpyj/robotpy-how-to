#!/usr/bin/env python3

import wpilib # <---- main library with all the necessary code for controlling FRC robots
import wpilib.buttons # <---- for joystick buttons

class MyRobot(wpilib.IterativeRobot): # <---- IternativeRobot means that it loops over and over by itself like a while loop

    def robotInit(self):

        """
            Define all motor controllers, joysticks, Pneumatics, etc. here so you can use them in teleop/auton
        """

        self.xboxController = wpilib.Joystick(0) # <--- joystick, does not have to be an xbox controller

        self.fire_single_piston = wpilib.buttons.JoystickButton(self.xboxController, 1) # Xbox controller button Number 1 (A)
        self.fire_double_piston_forward = wpilib.buttons.JoystickButton(self.xboxController, 2) # Xbox controller button Number 2 (B)
        self.fire_double_piston_backward = wpilib.buttons.JoystickButton(self.xboxController, 3) # Xbox controller button Number 3 (X)

        self.single_solenoid_piston = wpilib.Solenoid(1) # Solenoid on port 1
        self.double_solenoid_piston = wpilib.DoubleSolenoid(2,3) # Double Solenoid on port 2 and 3

    def teleopPeriodic(self):

        """
            Human controlled period
        """

        if (self.fire_single_piston.get()): # if pressed, set direction forward
            self.single_solenoid_piston.set(True)
        else:
            self.single_solenoid_piston.set(False)


        if (self.fire_double_piston_forward.get()):
            self.double_solenoid_piston.set(wpilib.DoubleSolenoid.Value.kForward)

        elif (self.fire_double_piston_backward.get()):
            self.double_solenoid_piston.set(wpilib.DoubleSolenoid.Value.kReverse)


if __name__ == "__main__":
    wpilib.run(MyRobot) #runs the code!
