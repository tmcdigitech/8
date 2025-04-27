---
title: Controller class
---

• [Download controller.py](controller.py)

**Controller** allows you to write games which will work simultaneously with the keyboard, a SNES-style controller, or the arcade cabinet, without changing your code. Here is a minimal example of the basics:

```python {linenos=table,hl_lines=[1-2,4,14]}
import controller
import pygame

p0 = controller.Controller(0, keyboard, pygame.joystick)

box = Rect((20, 20), (100, 100))
color = "red"

def draw():
    screen.clear()
    screen.draw.filled_rect(box, color)

def update():
    p0.update()
    global score, color
    if p0.right:
        box.x += 2
    if p0.left:
        box.x -= 2
    if p0.north:
        color = "blue"
    if p0.leftshoulder:
        color = "yellow"
```
