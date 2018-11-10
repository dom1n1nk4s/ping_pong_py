from Player import Player
from Ball import Ball

def setup():
    size(900,700)
    frameRate(60)
    global p1, p2, ball # needed for other functions
    p1 = Player(1) # W AND S
    p2 = Player(2) # ARROW KEYS
    ball = Ball()

def draw(): # called every frame
    background(0)
    scoreboard()
    checkCollision()
    ball.move()
    p1.move()
    p2.move()    
    getScore()
    
def keyPressed(): # keyboard input to movement
    if key == CODED:
        if keyCode == UP:
            p2.direction = -1 
        elif keyCode == DOWN:
            p2.direction = 1
    else:
        if key.upper() == 'W':
            p1.direction = -1
        elif key.upper() == 'S':
            p1.direction = 1
        elif key.upper() == 'R':
            reset()
        elif key.upper()=='G': # debug
            ball.direction.limit(6)  
            ball.direction = PVector(20,0)
            ball.direction.limit(6)     
                 
def keyReleased(): # resets direction when nothing is pressed
    if key == CODED: # if arrow keys are released
        p2.direction = 0
    else: # if W S are released
        p1.direction = 0

def reset():
    p1.reset()
    p2.reset()
    ball.reset()
        
def scoreboard(): # draws the gui
    stroke(255)
    line(0,60,width,60) # upper boundary
    stroke(255)
    line(0,height-60,width,height-60) # lower boundary
    stroke(255)
    line(width/2,0,width/2,height) # center boundary
    text("PLAYER 1: "+str(p1.score),30,30) # player scores
    text("PLAYER 2: "+str(p2.score),width/2 + 30,30)
    
def getScore(): # checks whether the ball is out of boundaries and adds score
    if ball.x > width:
        p1.score+=1
        ball.reset()
    elif ball.x < 0:
        p2.score+=1
        ball.reset()

def checkCollision(): 
    if p1.x < ball.x and p1.y < ball.y and p1.x+p1.racketsizex > ball.x and p1.y+p1.racketsizey > ball.y: # if hit racket
        ball.direction.x *= -1*(1+random(0.5))#flip x direction and boost it 
        ball.stepx *= -1
        ball.y += ball.stepy #move in y axis
        ball.x = p1.x+p1.racketsizex+1 # teleports the ball to the front of the racket (it sometimes gets stuck inside), **
    if p2.x < ball.x and p2.y < ball.y and p2.x+p2.racketsizex > ball.x and p2.y+p2.racketsizey > ball.y: # same stuff, but for p2's racket
        ball.direction.x *= -1*(1+random(0.5))
        ball.stepx *= -1
        ball.y += ball.stepy  
        ball.x = p2.x-1 # **
    ball.direction.x=constrain(ball.direction.x,-5,5) # limits ball speed
