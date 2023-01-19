---
title: A starting example
weight: 60
---
This is a simple example which:
1. beeps,
2. moves forward 100mm (10cm),
3. moves backward 100mm,
4. turns 360° on the spot,
5. beeps again.

Each of these steps happens to correspond
with a line of code:
```python
ev3.speaker.beep()
robot.straight(100)
robot.straight(-100)
robot.turn(360)
ev3.speaker.beep()
```

## Complete program
Here is the complete program, complete with headings
marking the major parts of the program structure.
You can see on lines 44, 47, and 50 there are lines
of code that are commented out because we don't need
them, but they might be handy in the future!

```python {linenos=table}
#!/usr/bin/env pybricks-micropython 
# ^ Shebang line above ^

##############################################
# Docstring
##############################################
""" 
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program 
----------------------------------------------------------------- 

This program requires LEGO® EV3 MicroPython v2.0. 
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3 

Building instructions can be found at: 
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot 
""" 

##############################################
# Import code
##############################################

from pybricks.hubs import EV3Brick 
from pybricks.ev3devices import Motor 
from pybricks.parameters import Port 
from pybricks.robotics import DriveBase 
from pybricks.tools import wait

##############################################
# Setup
##############################################

# Initialize the EV3 Brick. 
ev3 = EV3Brick() 

# Initialize the motors. 
left_motor = Motor(Port.B) 
right_motor = Motor(Port.C) 

# Initialize the drive base. 
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Initialize the Touch Sensor. 
# touch_sensor = TouchSensor(Port.S1) 

# Initialize the Colour Sensor. 
# color_sensor = ColorSensor(Port.S3) 

# Initialize the ultrasonic sensor.  
# ultrasonic_sensor = UltrasonicSensor(Port.S4) 

##############################################
# Program body
##############################################

ev3.speaker.beep()
robot.straight(100)
robot.straight(-100)
robot.turn(360)
ev3.speaker.beep()
```
