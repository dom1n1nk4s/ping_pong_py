class Ball:

    def __init__(self):
        self.direction = PVector(0,0)
        self.x = width/2
        self.y = (height-60*2)/2
        
    def move(self):
        self.stepx = self.direction.x 
        self.stepy = self.direction.y 
        self.counter = 8
        while(self.counter):
            if self.y+self.stepy > 60 and self.y+self.stepy < height-60: 
                self.y += self.stepy 
                self.x += self.stepx
            else:
                self.direction.y *= -1
                self.stepy *= -1
                self.y += self.stepy
                self.x += self.stepx
                break        
            self.counter-=1
        rect(self.x,self.y,10,10) 
       
    def reset(self):
        if random(0,100) > 49:
            self.direction = PVector(random(0.4,1),random(0.4,1)) 
        else:
            self.direction = PVector(random(-1,-0.4),random(0.4,1)) 
        self.x = width/2
        self.y =(height-60*2)/2
