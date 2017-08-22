## Advanced Programming ##

So you you have a driving robot that has functional, basic autonomous and a decent HTML dashboard....now what?

Here are some great upgrades you can do to make your robot perform the very best it can.

1. **Automate tasks.** In 2016, we have a firing sequence where the robot would open up the pistons and rev up the motors for a few seconds. This was all preprogrammed so the driver just needed to press one button. Without this feature, firing a boulder would be even more inconsistent because you would have to guess when the motors were revved up.

2. **Use the Gyro(NavX)** to create a straight driving robot for both autonomous and human controlled periods. Most often, robots will drift to one side and thus makes driving harder and autonomous less accurate. I did this for the 2017 robot. Use a PID loop to keep it steady.

3. **Ultrasonic Sensors.** Another 2017 addition, these cheap sensors allow you to detect when you are getting close to something like a wall or another robot. I used it to see if I was within like 9 inches of the peg and it worked every time. Pretty easy to program and works great.

4. **Touch or button sensors.** Need to see if you have a game object in your possession? A simple touch sensor works great and helps a lot. For 2017, being able to see that there was a gear in what awesome when visibility was low.

5. **Encoders!** Need to drive a certain distance no matter what the battery voltage is at? Or need a fly wheel shooter to go at a certain RPM? I used an encoder on the 2017 robot so I could drive forward about 114 inches before turning. The variation between runs was a solid +/- 1 inch. In 2016, I used an encoder for shooting our boulder at a consistent RPM. You should start out using a PID loop for this and then, if you want even more accuracy, use a motion profile.

6. **Various other sensors.** Force sensors, color sensors, beam-break sensor, 360 degree LiDAR could all come in handy depending on the task as well as making your self look impressive for the judges. Just make sure that whatever sensor you decided on is reliable and easy to program!

7. **Vision.** This is probably the last upgrade to do. Vision is incredibly complicated and, at least in my couple years of experience, very unreliable. However, that doesn't mean that you can give it a try and see if it helps improve your robot.

  If you are going to do it, I recommend using GRIP which allows you to basically drag n' drop OpenCV filters and there is a tutorial to follow. I ran the GRIP program once on the laptop (2016) and once on the robot with a Raspberry Pi. The onboard Pi worked much better because the latency was less and it was more hands free. However, I was not able to check and see what it was seeing so if the lighting conditions changed and it just didn't work, I was not able to see what was happening.
