class Player(object):
    racketsizey = 150 
    racketsizex = 41 
    
    def __init__(self, id): 
        self.direction = 0
        self.id = id
        self.y = (height-60*2)/2 
        self.score = 0
        if id == 1:
            self.x = 30 
        else: # PLAYER IS A BOT
            self.x = 840
        
    def move(self):
        self.step = self.direction
        self.counter = 18
        while(self.counter):
            if self.y+self.step > 60 and self.y+self.racketsizey+self.step < height-60: 
                self.y += self.step
            else:
                break
            self.counter-=1
        rect(self.x,self.y,self.racketsizex,self.racketsizey)

    def reset(self):
        self.score = 0
        self.direction = 0
        self.y = (height-60*2)/2
