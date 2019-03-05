class Shot:
    """docstring for Shot"""

    def isOnScreen(self):
        return self.onScreen

    def update(self, boundary):
        self.xpos += 10
        if self.xpos > boundary:
            self.onScreen = False

    def __init__(self, xpos, ypos):
        super(Shot, self).__init__()
        self.xpos = xpos
        self.ypos = ypos
        self.onScreen = True
