class Enemy:

    def destroy(self):
        self.onScreen = False
    
    def isOnScreen(self):
        return self.onScreen

    def update(self, boundary = 0):
        self.xpos -= self.speed
        if self.xpos < boundary:
            self.onScreen = False

    def __init__(self, xpos, ypos, speed):
        super(Enemy, self).__init__()
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed
        self.onScreen = True