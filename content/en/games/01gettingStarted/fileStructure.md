---
title: Structuring your files
weight: 20
---

Each of your projects should live in its own folder somewhere sensible (like in a Digital Tech folder in your OneDrive!).

```
Digital Tech/
│
├── firstGame/
│   └── game.py
│
├── secondGame/
│   └── game.py
│
├── thirdGame/
│   └── game.py
│
└── fourthGame/
    └── game.py
```

Within each of those folders, there will be the python file with your game code in it,
along with some other files and folders. Here is an example of a more
complex project:

```
myGame/
├── game.py
│
├── images/
│   ├── someImage.png
│   ├── anotherImage.jpg
│   └── ... # sprites, tiles and other image files
│
├── fonts/
│   └── ... # any font files
│
├── sounds/
│   └── ... # any sound files
│
└── music/
    └── ... # any music files
```

You don't need to have those folders unless you have something to put in them.

{{< alert color="warning" title="Check your version of Mu">}}
If you are using a version of Mu older than `1.1.0-alpha.2`, the shortcut buttons in Pygame Zero mode (Images, Sounds, Fonts and Music) will open folders in Mu's *default* save location. If you have saved your project in a different location (like your OneDrive) you won't be able to use these shortcut buttons, as they won't open the right folders.

From `1.1.0-alpha.2` onwards, the buttons will open folders relative to the file you have open, so they will always work, regardless of where you save your game file.
{{< /alert >}}
