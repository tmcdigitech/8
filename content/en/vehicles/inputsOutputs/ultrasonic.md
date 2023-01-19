---
title: Ultrasonic sensor
weight: 40
---
*adapted from [PyBricks](https://pybricks.com/ev3-micropython/ev3devices.html#ultrasonic-sensor)*

The Ultrasonic Sensor is a digital sensor that can measure the distance to an object in front of it. It does this by sending out high frequency sound waves and measuring how long it takes the sound to reflect back to the sensor. The sound frequency is too high for you to hear. 

Distance to an object is measured in millimeters (mm). This allows you to program your robot to stop at a certain distance from a wall.

{{< figure src="https://pybricks.com/ev3-micropython/_images/sensor_ev3_ultrasonic.png" title="An EV3 ultrasonic sensor" >}}

## Import
```python
from pybricks.ev3devices import UltrasonicSensor
```

## Setup
```python
# Initialize the Ultrasonic Sensor.
obstacle_sensor = UltrasonicSensor(Port.S4)
```

## Functions
### `distance()`<br/>`distance(silent)`
Measures the distance between the sensor and an object using ultrasonic sound waves.

Parameters:
- silent (bool): `False` by default. Choose `True` to turn the sensor off after measuring the distance. This reduces interference with other ultrasonic sensors. If you do this too frequently, the sensor can freeze. If this happens, unplug it and plug it back in.

Returns:
- distance in mm

### `presence()`
Checks for the presence of other ultrasonic sensors by detecting ultrasonic sounds.

If the other ultrasonic sensor is operating in silent mode, you can only detect the presence of that sensor while it is taking a measurement.

Returns:
- `True` if ultrasonic sounds are detected, `False` if not.

## Example

```python
# Drive forward until an object is no more than 30cm away
robot.drive(200, 0)
while obstacle_sensor.distance() > 300:
    pass
robot.stop()
```
