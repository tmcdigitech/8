---
title: Comments
weight: 50
---
Comments are a way of leaving messages for other humans (or
you in the future) in your program. They are a vital part
of programming, and critical to writing good code that works.

Comments are indicated using some combination of symbols,
and the computer is programmed to ignore them, so you can
write anything you like, and not have to worry about the
computer trying to make sense of it.
Because the computer ignores any text that is a comment,
we can also use comments to “turn off” some lines
of our program temporarily by “commenting them out”.

In Python, any time the computer comes across
a `#` (hash) symbol, it will ignore the rest of the line.
Most text editors have a way to automatically add and
remove comments from a selection of code.
In Visual Studio Code, the shortcut for toggling comment
markers is <kbd>Ctrl</kbd>+<kbd>/</kbd>
(<kbd>Cmd</kbd>+<kbd>/</kbd> on a Mac).

```python
# This is a comment
```

## Why do we need comments?
Because computers are brainless machines with no clue
about anything, computer programs are extremely thorough, step-by-step sequences of instructions that tell the computer exactly what to do. They don't, however, provide any clue
about what the program is for, why you might want to use it,
or why certain bits of code are included.

Comments allow a human reader to get a "big picture" sense
of what chunks of the program, and the program as a whole,
are about, and why certain decisions have been made.
They are also used to leave reminders about things that
still need to be fixed, things which might cause trouble
later, and places where a problem has been found but a
solution hasn't been worked out yet.
