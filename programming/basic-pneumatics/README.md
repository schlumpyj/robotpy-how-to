## Basic Pneumatics ##

There are a few things to know about Pneumatics when programming.

-- There are two types of solenoids (devices that control when a piston fires): Single and Double.

Single:

![Single Solenoid](https://cdn3.volusion.com/vyfsn.knvgw/v/vspfiles/photos/am-2304-2.jpg?1442240393)

Double:
![Double Solenoid](http://www.team358.org/files/pneumatic/Festo24v.jpg)

Doubles are nice for when you want something to keep the state even when the robot is disabled or off. Singles are usually for quick open and close operations and when you don't want the state to hold when the robot is disabled.


-- As soon as you create any solenoid object in your code, it will automatically create an invisible compressor object that works in the background. You don't have to do anything for it, but just know that even though is there is a compressor library in the RobotPy docs, you don't ever really use that.
