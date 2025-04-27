class Controller:
    def __init__(self, pId, kb, js):
        self.kb = kb
        self.pId = pId
        self.js = False
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.east = False
        self.south = False
        self.west = False
        self.north = False
        self.select = False
        self.start = False
        self.leftshoulder = False
        self.rightshoulder = False
        if js.get_count() > pId:
            self.js = js.Joystick(pId)
            print(f"Player {pId} has a joystick.")
        if pId == 0:
            self.kbmap = {
                'up': 'w',
                'down': 's',
                'left': 'a',
                'right': 'd',
                'north': 'g',
                'south': 'b',
                'west': 'v',
                'east': 'n',
                'leftshoulder': 'q',
                'rightshoulder': 'e',
                'select': 'f',
                'start': 'h'
            }
        elif pId == 1:
            self.kbmap = {
                'up': 'p',
                'down': 'semicolon',
                'left': 'l',
                'right': 'quote',
                'north': 'up',
                'south': 'down',
                'west': 'left',
                'east': 'right',
                'leftshoulder': 'o',
                'rightshoulder': 'leftbracket',
                'select': 'rightbracket',
                'start': 'backslash'
            }
        if self.js != False:
            self.jsmap = {
                'north': 0,
                'east': 1,
                'south': 2,
                'west': 3,
                'leftshoulder': 4,
                'rightshoulder': 5,
                'select': 8,
                'start': 9
            }

    def update(self):
        self.up = getattr(self.kb,self.kbmap['up'])
        self.down = getattr(self.kb,self.kbmap['down'])
        self.left = getattr(self.kb,self.kbmap['left'])
        self.right = getattr(self.kb,self.kbmap['right'])
        self.north = getattr(self.kb,self.kbmap['north'])
        self.south = getattr(self.kb,self.kbmap['south'])
        self.west = getattr(self.kb,self.kbmap['west'])
        self.east = getattr(self.kb,self.kbmap['east'])
        self.start = getattr(self.kb,self.kbmap['start'])
        self.select = getattr(self.kb,self.kbmap['select'])
        self.leftshoulder = getattr(self.kb,self.kbmap['leftshoulder'])
        self.rightshoulder = getattr(self.kb,self.kbmap['rightshoulder'])
        if self.js != False:
            self.up = self.up or (self.js.get_axis(1) < -0.1)
            self.down = self.down or (self.js.get_axis(1) > 0.1)
            self.left = self.left or (self.js.get_axis(0) < -0.1)
            self.right = self.right or (self.js.get_axis(0) > 0.1)
            self.north = self.north or self.js.get_button(self.jsmap['north'])
            self.south = self.south or self.js.get_button(self.jsmap['south'])
            self.east = self.east or self.js.get_button(self.jsmap['east'])
            self.west = self.west or self.js.get_button(self.jsmap['west'])
            self.start = self.start or self.js.get_button(self.jsmap['start'])
            self.select = self.select or self.js.get_button(self.jsmap['select'])
            self.leftshoulder = self.leftshoulder or self.js.get_button(self.jsmap['leftshoulder'])
            self.rightshoulder = self.rightshoulder or self.js.get_button(self.jsmap['rightshoulder'])

