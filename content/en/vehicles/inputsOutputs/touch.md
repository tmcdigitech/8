---
title: Touch sensor
weight: 30
---
*adapted from [PyBricks](https://pybricks.com/ev3-micropython/ev3devices.html#touch-sensor)*

A sensor lets an EV3 program measure and collect data about its surroundings. The Touch Sensor detects when its red button
has been pressed or released.

{{< figure src="https://pybricks.com/ev3-micropython/_images/sensor_ev3_touch.png" title="An EV3 touch sensor" >}}

## Import
```python
from pybricks.ev3devices import TouchSensor
```

## Setup
```python
# Initialize Touch Sensor
touch_sensor = TouchSensor(Port.S1)
```

## Functions
### `pressed()`
Checks if the sensor is pressed.

Returns:
- `True` if the sensor is pressed, `False` if it is not pressed.

## Example
```python
# Beep when touch sensor is pressed
while True:
    if button.pressed():
        ev3.speaker.beep()
```
```python
# Drive forward until touch sensor is pressed
robot.drive(1000, 0)
while not touch_sensor.pressed():
    pass
robot.stop()
```
