import pygame, random
from pygame.locals import *

pygame.init()

()
WINDOWWIDTH = 900
WINDOWHEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

pygame.display.set_caption('Testing out snake movement and snake drawing')


CELLSIZE = 30
CELLHEIGHT = WINDOWHEIGHT/CELLSIZE
CELLWIDTH = WINDOWWIDTH/CELLSIZE
DARKGRAY = (192,192,192)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
RIGHT = "right"
UP = "up"
DOWN = "down"
LEFT = "left"




def drawsnake(coords):
    for coord in coords:
        x = coord['x']*CELLSIZE
        y = coord['y']*CELLSIZE
        snake = pygame.Rect(x,y,CELLSIZE,CELLSIZE)
        pygame.draw.rect(DISPLAYSURF,GREEN,snake)
        innersnake = pygame.Rect(x+5,y+5,CELLSIZE-10,CELLSIZE-10)
        pygame.draw.rect(DISPLAYSURF,BLUE,innersnake)
    return snake

def intro_screen(degrees,width,height):
    myfont = pygame.font.SysFont("Castellar",100)
    myfont2 = pygame.font.SysFont("sitka banner",30)
    myfont.set_bold(True)
    text = myfont.render("Snaky",True,BLUE,WHITE)
    myfont2.set_bold(True)
    text2 = myfont2.render("Press any key to Play",True,WHITE)
    text2rect = text2.get_rect()
    text2rect.bottomright = (WINDOWWIDTH-50,WINDOWHEIGHT-50)
    rotatetext = pygame.transform.rotate(text,degrees)
    scaletext = pygame.transform.scale(text,(width,height))
    rotaterect = rotatetext.get_rect()
    rotaterect.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)
    scalerect = scaletext.get_rect()
    scalerect.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)
    DISPLAYSURF.blit(rotatetext,rotaterect)
    DISPLAYSURF.blit(text2,text2rect)
    #print(scalerect)




    
    




def game_intro():
    direction = RIGHT
    clock = pygame.time.Clock()
    startx = 4
    starty = 2
    width = 200
    height = 100
    degrees = 1
    coords = [{'x':startx,'y':starty},
            {'x':startx-1,'y':starty},
             {'x':startx-2,'y':starty}
             ]
   
    
    running = True
    
    while running:
        width = 200
        height = 100
        snake_body = coords[1:]
        for events in pygame.event.get():
            if events.type == QUIT:
                pygame.quit()
                quit()
        if direction == RIGHT:
            newhead = {'x':coords[0]['x']+1,'y':coords[0]['y']}
        if direction == LEFT:
            newhead = {'x':coords[0]['x']-1,'y':coords[0]['y']}
        if direction == UP:
            newhead = {'x':coords[0]['x'],'y':coords[0]['y']-1}
        if direction == DOWN:
            newhead = {'x':coords[0]['x'],'y':coords[0]['y']+1}

        
        
        coords.insert(0,newhead)
        del coords[-1]
        DISPLAYSURF.fill(BLACK)
        width = 400
        height = 200
        intro_screen(degrees,width,height)
        snake = drawsnake(coords)
       # print(snake)

        if snake[0] == 780 and snake[1] <= 90:
            direction = DOWN
        if snake[0] == 90 and snake[1] >= 510:
            direction = UP
        if snake[1] == 510 and snake[0] >= 780 :
            direction = LEFT
        if snake[1] == 90 and snake[0] <=90:
            direction = RIGHT


        degrees += 5
       
        
        pygame.display.update()
        clock.tick(10)

game_intro()