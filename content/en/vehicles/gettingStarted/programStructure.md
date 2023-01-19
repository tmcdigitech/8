---
title: Structure of program
weight: 40
---
## Overview
The basic structure of any EV3 program is:
- the *shebang* line
- the docstring
- import libraries
- setup
- program body (the part where you tell the robot what to do)

## Shebang #!
The [**shebang**](https://en.wikipedia.org/wiki/Shebang_(Unix)) line is a piece of Unix
trickery from about 1980 which has stuck around because it is
rather useful. You don't need to understand what it is doing
or why it is there, but it is **vitally important**
(in big letters) that this line appears exactly as it does
below, and that it is at the very start of the program
file (no blank lines above it, or spaces in front of it).

```c
#!/usr/bin/env pybricks-micropython
```

If your program doesn't work, check this first!

## Docstring
The next lines, within the `"""` (three double-quote marks), are explanatory text
about what the program in this file does. It is customary
to do this in Python for the benefit of anyone else who might
come across your code (including you in the future), but your
program will work if you don't.

```python
""" 
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program 
----------------------------------------------------------------- 

This program requires LEGO® EV3 MicroPython v2.0. 
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3 

Building instructions can be found at: 
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot 
""" 
```

## Importing
*see [import]({{< ref "/glossary/import" >}}) for more detail*

Any but the simplest of programs will use code from one
or more modules. A *module* is chunk of code that does
some useful stuff that lots of different developers
would want to do again and again: do maths,
search for and sort data,
connect to and work with databases, use various
bits of hardware (like an EV3 brick!).
There is a standard library included with
Python, where the most common modules can be found, and
you can download and use other modules when you need to.

```python {hl_lines="2"}
from pybricks.hubs import EV3Brick 
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase 
from pybricks.tools import wait 
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
```
In the code above, you can get the sense that `pybricks`
is a very large library with lots of different parts.
One of those parts is called `parameters`, and on the
highlighted line we tell the computer we will need two
things from the parameter part of the pybricks module:
the things called `Port` and `Stop`. The dot notation is
how you show things that are parts of other things:
- `pybricks.parameters` means the `parameters` part of `pybricks`;
- `pybricks.parameters.Stop` means the `Stop` part of the `parameters` part of `pybricks`.

## Setup
Now that we have all the bits of code we will need, we
need to tell the computer about the things we'll be using
and where they're connected.

We need to set up:
- the EV3 brick itself,
- the motors
- the `DriveBase`, if it's a vehicle,
- the sensors that we are using,
making sure that the ports you
list in this part of the code match up with where you've
actually connected each of the components.

Since we are making a vehicle that drives, rather than,
say, a stationary factory robot on an assembly line, we
set up the motors for our wheels using a `DriveBase`,
which has a lot of handy driving-around kind of functions.

```python
# Initialize the EV3 Brick. 
ev3 = EV3Brick() 

# Initialize the motors. 
left_motor = Motor(Port.B) 
right_motor = Motor(Port.C) 

# Initialize the drive base. 
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Initialize the Touch Sensor. 
touch_sensor = TouchSensor(Port.S1) 

# Initialize the Colour Sensor. 
color_sensor = ColorSensor(Port.S3) 

# Initialize the ultrasonic sensor.  
ultrasonic_sensor = UltrasonicSensor(Port.S4) 
```
