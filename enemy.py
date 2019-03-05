class Enemy:

    def isOnScreen(self):
        return self.onScreen

    def update(self, boundary = 0):
        self.xpos -= 5
        if self.xpos < boundary:
            self.onScreen = False

    def __init__(self, xpos, ypos):
        super(Enemy, self).__init__()
        self.xpos = xpos
        self.ypos = ypos
        self.onScreen = True