class Ball:

    def __init__(self):  # setup
        self.x = width / 2
        self.y = (height - 60 * 2) / 2
        self.direction = PVector(0, 0)

    def move(self):
        self.stepx = self.direction.x  # a single stepx distance
        self.stepy = self.direction.y  # a single stepy distance
        self.counter = 8  # step multiplier
        while self.counter:  # a while cycle for checking each move individually - this makes sure that the ball doesnt glitch out at high speed
            if self.y + self.stepy > 60 and self.y + self.stepy \
                < height - 60:  # if not out of upper and lower boundaries, move
                self.y += self.stepy  # move
                self.x += self.stepx
            else:

                  # if touching the boundary, flip the y direction

                self.direction.y *= -1  # flip y direction (bounce)
                self.stepy *= -1
                self.y += self.stepy
                self.x += self.stepx
                break  # stop the while loop early, in order to not get out of boundaries
            self.counter -= 1
        rect(self.x, self.y, 10, 10)  # visualise it

    def reset(self):  # reset the ball's direction and pos
        if random(0, 100) > 49:  # decide whether the ball will go to the right or left
            self.direction = PVector(random(0.5, 1), random(0.4, 1))  # right
        else:
            self.direction = PVector(random(-1, -0.5), random(0.4, 1))  # left
        self.x = width / 2
        self.y = (height - 60 * 2) / 2
