---
title: import
---

Importing is the process of adding functions or other objects from other modules to support your program.

Imagine we wish to use the `randint()` function
to choose a random number between 1 and 6, as
though we were throwing a single six-sided die.
The `randint()` function is part of the `random` module.
There are two ways we can go:
- import the whole module
- import just the objects we need

## Import module
```python
import random

num = random.randint(1,6)
print(num)
```

We can use a different name for the module in our
program, which is useful if the original name is really long, or we happen to have two modules with the same name.

```python
import random as ran

num = ran.randint(1,6)
print(num)
```

## Import just what we need
By importing just the objects we need from a module,
we don't need to use the name of the module anymore.

```python
from random import randint

num = randint(1,6)
print(num)
```

We can rename objects for convenience or to avoid name clashes.

```python
from random import randint as throwDie

num = throwDie(1,6)
print(num)
```
