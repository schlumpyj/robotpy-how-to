## Basic Auto and Chooser ##

This is a basic usage of how we make autonomous modes. The code has a selector that is sent back to the laptop where the driver can select which mode to run. This worked great in the 2017 and never failed us. This does require you to have a web server running on the laptop to select it, however.

The great thing about doing it this way is that all the auto modes are in different files and the auto selector automatically finds them for you and handles all the logic.

More information on this approach, [called "Stateful Autonomous" here.](http://robotpy.readthedocs.io/projects/utilities/en/latest/robotpy_ext.autonomous.html#module-robotpy_ext.autonomous.stateful_autonomous)
