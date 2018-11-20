from Player import Player
from Ball import Ball

def setup():
    size(900,700)
    frameRate(60)
    global p1, p2, ball
    ball = Ball()
    p1 = Player(1) # W AND S
    p2 = Player(2) # PLAYER IS A BOT
   
def draw():
    background(0)
    scoreboard()
    checkCollision()
    ball.move()
    botdirection() # bot ai
    p1.move()
    p2.move()
    getScore()
    
def keyPressed():
    if key != CODED:
        if key.upper() == 'W':
            p1.direction = -1
        elif key.upper() == 'S':
            p1.direction = 1
        elif key.upper() == 'R':
            reset()
         
def keyReleased(): # resets direction when nothing is pressed
    if key != CODED: # if W or S are released
        p1.direction = 0
        
def botdirection(): # artificial superhuman intelligence
    if p2.y+p2.racketsizey/2 <= ball.y: # if center of racket is higher or equal to ball's pos, move downward
        p2.direction = 0.7
    elif p2.y+p2.racketsizey/2 >= ball.y: # else if it's lower, move upward
        p2.direction = -0.7

def reset():
    p1.reset()
    p2.reset()
    ball.reset()
        
def scoreboard():
    stroke(255)
    line(0,60,width,60) 
    stroke(255)
    line(0,height-60,width,height-60) 
    stroke(255)
    line(width/2,0,width/2,height) 
    text("PLAYER 1: "+str(p1.score),30,30) 
    text("BOT: "+str(p2.score),width/2 + 30,30)
    
def getScore():
    if ball.x > width:
        p1.score+=1
        ball.reset()
    elif ball.x < 0:
        p2.score+=1
        ball.reset()

def checkCollision():
    if p1.x < ball.x and p1.y < ball.y and p1.x+p1.racketsizex > ball.x and p1.y+p1.racketsizey > ball.y: 
        ball.direction.x *= -1*(1+random(0.5))
        ball.stepx *= -1
        ball.y += ball.stepy  
        ball.x = p1.x+p1.racketsizex+1 
    if p2.x < ball.x and p2.y < ball.y and p2.x+p2.racketsizex > ball.x and p2.y+p2.racketsizey > ball.y:
        ball.direction.x *= -1*(1+random(0.5))
        ball.stepx *= -1
        ball.y += ball.stepy 
        ball.x = p2.x-1
    ball.direction.x=constrain(ball.direction.x,-5,5)
