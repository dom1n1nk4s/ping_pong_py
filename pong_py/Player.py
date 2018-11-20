class Player(object):

    racketsizey = 150  # height of the 'pingpong square'
    racketsizex = 41  # width of the 'pingpong square', it has to be larger than 40, otherwise, the ball will teleport through the ball at max speed (max speed=5,multiplier=8,8*5=40)

    # the keyword self is beyond me to understand

    def __init__(self, id):  # called everytime a object is initialised
        self.direction = 0  # direction in the y axis only
        self.id = id
        self.y = (height - 60 * 2) / 2  # center
        self.score = 0
        if id == 1:  # player 1 position
            self.x = 30
        else:

              # id == 2, player 2 position

            self.x = 840

    def move(self):  # movement, duh
        step = self.direction  # a single step distance
        self.counter = 18
        while self.counter:  # while cycle, for accurate movement checking
            if self.y + step > 60 and self.y + self.racketsizey + step \
                < height - 60:  # if not out of boundaries, move
                self.y += step  # move
            else:
                break
            self.counter -= 1
        rect(self.x, self.y, self.racketsizex, self.racketsizey)  # visualise it

    def reset(self):
        self.score = 0
        self.direction = 0
        self.y = (height - 60 * 2) / 2  # center
