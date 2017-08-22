## Common Programming Problems ##

I have encountered hundreds of programming problems in my day and a few show up quite often. Unfortunately, I don't remember all of the common problems given that I haven't programmed the robot in many months.

I would recommend adding to this page as you find new common problems.

1. **My Robot Turning is reversed.** This happened more than any other problem. If you have a West Coast Drive (Tank Drive) setup, all you should need to do is switch the PWM wires on the roboRIO. You can do it in programming, but it makes maintaining your code harder.

  In code it is something like switching this `arcadeDrive(self.joystick.getY(), self.joystick.getX())` to this `arcadeDrive(self.joystick.getY(), -1*self.joystick.getX())`. X of course is your turning axis when Y is your throttle.

2. **I click enable on the Driver Station, but nothing happens.** This one is a hard one to say for sure what is happening. For this past season, a big problem was that the Driver Station would stop my Xbox Controller values. In other words, when I moved the Xbox Controller, it didn't show that I moved it on the Joystick tab of the Driver Station. The fix here was to just restart the Driver Station software.

  Sometimes, your robot doesn't enable because you hit a code error. Check the Driver Station console to see what the error might be.

3. **The Radio is flashing is has already booted for a few minutes, but I can't connect to it.** This can be a couple of things.

    1. You haven't reflashed the radio from competition where it uses different software.

    2. The ethernet cable from the roboRIO to the radio isn't connected or the cable went bad.

    3. The radio looses power frequently causes reboots. This can be because the power plug isn't snug or the power coming in isn't clean 12V.

4. **My code doesn't deploy.** This can be due to many things.

      1. You are not connected to the robot's network.

      2. You are connected to the robot's network, but you are hitting the wrong address. For example, I have always setup my roboRIO to be static at 10.44.80.2, but when you reflash a RIO, it will be dynamic and always a different address. All you need to do is change the deploy file found near your code.

      3. There also has been some weird errors that have nothing to due with code. In this case, reboot the laptop and if it still happens, ask @virtuald (the creator of RobotPy) what might be happening.
