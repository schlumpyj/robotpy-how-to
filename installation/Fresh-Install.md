## Fresh Install (When Laptop is New or it is a new build season) ##

1. Install the [National Instruments Update FRC Suite](http://www.ni.com/download/first-robotics-software-2015/5112/en/)

2. Do the necessary things to install it (Extract, Run, Accept, Etc.)

3. Find Key Softare in Suite after install such as Driver Station, Router Update.

4. Install Router Update ([Instructions](https://wpilib.screenstepslive.com/s/4485/m/13503/l/144986-programming-your-radio-for-home-use))

5. Install RoboRIO Update ([Instructions](https://wpilib.screenstepslive.com/s/4485/m/13503/l/144984-imaging-your-roborio))

6. Follow [Laptop Instructions](https://github.com/bb20basketball/robotpy-how-to/blob/master/installation/laptop-install.md)

7. Follow [Robot Instructions](https://github.com/bb20basketball/robotpy-how-to/blob/master/installation/robot-install.md)

8. Change the roboRIO to a static IP address. 10.44.80.2 is the standard.  Simply go to the roboRIO web interface ([which looks like this](https://wpilib.screenstepslive.com/s/4485/m/24166/l/262266-roborio-webdashboard)) by first going to `roborio-4480-frc.local` and then navigating to the network tab. You will have to login as admin with no password just like SSH. Write the 10.44.80.2 on a piece of tape and put it on the physical roboRIO so that you remember the address and so FTA's know that you are using static addresses rather than the inferior dynamic IPs.

  From then on, you can more quickly access the roboRIO web interface by going to 10.44.80.2. You can also use this address for your own HTML dashboard.

9. **Get Programming!**
