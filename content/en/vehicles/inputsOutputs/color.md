---
title: Color sensor
weight: 50
---
*adapted from [PyBricks](https://pybricks.com/ev3-micropython/ev3devices.html#color-sensor)*

A sensor lets an EV3 program measure and collect data about is surroundings. The Color Sensor can detect color and reflected light.

{{< alert color="warning" >}}
### Color vs colour
In almost all programming, American spellings are used. So as programmers we use **color** and **colors**, even though we would normally spell the words *colour* and *colours*.
{{< /alert >}}

{{< figure src="https://pybricks.com/ev3-micropython/_images/sensor_ev3_color.png" title="An EV3 color sensor" >}}

## Import
```python
from pybricks.ev3devices import ColorSensor
```

## Setup
```python
# Initialize the sensors.
line_sensor = ColorSensor(Port.S1)
```

## Functions
### `reflection()`
Measures the reflection of a surface using a red light.

Returns:
- reflection, ranging from 0 (no reflection) to 100 (high reflection).

### `rgb()`
Measures the reflection of a surface using a red, green, and then a blue light.

Returns:
- tuple of reflections for red, green, and blue light, each ranging from 0.0 (no reflection) to 100.0 (high reflection).<br/>
  (r, g, b)

### `color()`
Measures the color of a surface.

Returns:
- `Color.BLACK`, `Color.BLUE`, `Color.GREEN`, `Color.YELLOW`, `Color.RED`, `Color.WHITE`, `Color.BROWN`, or `None` if no color is detected.

### `ambient()`
Measures the ambient light intensity.

Returns:
- ambient light intensity, ranging from 0 (dark) to 100 (bright).

## Example
```python
# Go forward while reflected light is less than 10.
ev3.speaker.beep()
robot.drive(100,0)
while line_sensor.reflection() < 10:
    wait(10)
robot.stop()
```

<!-- Three modes: **Color**, **Reflected Light** intensity and **Ambient Light** intensity.

– **Color Mode**: Recognizes 7 colors (black, brown, blue, green, yellow, red, white) and No Color

– **Reflected Light**: Measures the intensity of the light reflected back from a lamp that emits a red light. (0=very dark and 100=very light)

– **Ambient Light**: Measures the strength of the light that enters the sensor from the environment. (0=very dark and 100=very light) -->

