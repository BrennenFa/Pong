import pygame
import random
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()
clock = pygame.time.Clock()
screenWidth = 1250
screenHeight = 750

win = pygame.display.set_mode((screenWidth, screenHeight))

#class player(object):
class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.score = 0


#move is called after each reset
    def move(self, keys):
        if keys[K_UP] and self.y > 10:
            self.y -= 1
  

        if keys[K_DOWN] and self.y < screenHeight - self.height - 10:    
            self.y += 1
           



class Rival(object):
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.score = 0

        def move(self, y):
            if self.y + int(self.height / 2) < y and self.y < screenHeight - self.height - 10:
                self.y += 1
            if self.y + int(self.height / 2) > y and self.y > 10:
                self.y -= 1
            

class Ball(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.left = False
        self.right = False
        self.up = False
        self.down = False
    def move(self):
        
        if self.left == True:
            self.x -= 1
        if self.right == True:
            self.x += 1
        if self.up == True:
            self.y -= 1
        if self.down == True:
            self.y += 1
    def bounce(self, x, y, width, height, wall):
        if self.x - self.radius <= x + width and self.x + self.radius >= x :
            if self.y - self.radius <= y + height and self.y + self.radius >= y - height:
                if wall:
                    self.up = not self.up
                    self.down = not self.down
                if not wall:
                    self.left = not self.left
                    self.right = not self.right



    def start(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        random1 = random.randint(1, 2)
        if random1 == 1:
            self.left = True
        else:
            self.right = True

        random2 = random.randint(1, 2)
        if random2 == 1:
            self.up = True
        else:
            self.down = True


   






loop = False   

#defines p1, p2, ball
p1 = Player(50, int(screenHeight / 2), 25, 75)
p2 = Rival(screenWidth - 50, int(screenHeight / 2), 25, 75)
ball = Ball(int(screenWidth / 2), int(screenHeight / 2), 10)



game = True #keeps track of overal game
while game:


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game = False
        elif event.type == QUIT:
            game = False
        
    font = pygame.font.SysFont('comicsans', 30, True, True)
    font1 = pygame.font.SysFont('comicsans', 10, False, False)
    p1.x = 50 
    p1.y = int(screenHeight / 2)
    p2.x = screenWidth - 50
    p2.y = int(screenHeight / 2)
    ball.x = int(screenWidth / 2)
    ball.y = int(screenHeight / 2)






    ball.start()



    
    round = True
    while round:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game = False
                    running = False
                    loop = True
            elif event.type == QUIT:
                game = False
                running = False
                loop = True
        clock.tick(3000)
        win.fill((0, 0, 0))
        
        if loop == True:
            break
    


        
        keys = pygame.key.get_pressed()
        p1.move(keys)
        p2.move(ball.y)

        
        


        #ball stuff - delete after quotations fixed





        
        ball.bounce(p1.x, p1.y, p1.width, p1.height, False)#player pong
        
        ball.bounce(p2.x, p2.y, p2.width, p2.height, False)#p2 pong
        #bounces off the edges     
        ball.bounce(0, screenHeight, screenWidth, 0, True)#bottom border
        ball.bounce(0, 0, screenWidth, 0, True)#top border

        win.fill((0, 0, 0))
        ball.move()
        p1.move(keys)
        pygame.draw.rect(win, [255, 255, 255], [p1.x, p1.y, p1.width, p1.height])#draw p1
        pygame.draw.rect(win, [255, 255, 255], [p2.x, p2.y, p2.width, p2.height])
        pygame.draw.circle(win, [255, 255, 255], [ball.x, ball.y], ball.radius)#draw ball
            

        if ball.x < 0:
            p2.score += 1
            break
        elif ball.x > screenWidth + 50:
            p1.score +=1
            break

        score1 = font.render("Your score: " + str(p1.score), 1, (255, 255, 255))
        score2 = font.render("Opponent score: " + str(p2.score), 1, (255, 255, 255))
        escape = font.render("Press 'ESC' to quit the program:", 1, (255, 255, 255))
        
        win.blit(score1, (50, 50))
        win.blit(score2, (screenWidth - 50 - score2.get_width(), 50))
        win.blit(escape, (screenWidth / 2 - escape.get_width() / 2, screenHeight - 50))
            
        pygame.display.flip()

    

#

#what happens if you hit the bottom of the paddle
#reset game after score gets to seven, reset board after it reaches 7

#make game harder



    #hits the edges
"""if ball.y + ball.radius == p1.y or ball.y - ball.radius == p1.y + p1.height:
        #if self.y - self.radius < y + height and self.y + self.radius > y - height:
        print("somewhat")
        if ball.x - ball.radius < p1.x + p1.width and ball.x + ball.radius > p1.x :
            print("edge")
            ball.up = not ball.up
            ball.down = not ball.down
            ball.left = not ball.left
            ball.right = not ball.right

    
else:
    ball.bounce(p1.x, p1.y, p1.width, p1.height, False)#player pong

if ball.y + ball.radius == p2.y or ball.y - ball.radius == p2.y + p2.height:
    if ball.x - ball.radius < p1.x + p2.width and ball.x + ball.radius > p2.x :
        ball.up = not ball.up
        ball.down = not ball.down
        ball.left = not ball.left
        ball.right = not ball.right

else:
    ball.bounce(p2.x, p2.y, p2.width, p2.height, False)"""#p2 pong
#quit
#
