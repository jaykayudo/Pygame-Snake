import pygame, random,time
from pygame.locals import *

pygame.init()

()
WINDOWWIDTH = 900
WINDOWHEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

pygame.display.set_caption('SNAKY')

#Sound Files
snakechop = pygame.mixer.Sound("snakechop.ogg")

crash = pygame.mixer.Sound("crash.wav")
snakechop.set_volume(1.0)
# pygame.mixer.music.set_volume(0.5)
crash.set_volume(0.5)

logo = pygame.image.load('logomain.png')

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

    
def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

def randcoords():
    xrand = random.randint(0,CELLWIDTH-1)
    yrand = random.randint(0,CELLHEIGHT-1)
    return xrand, yrand
def drawFood(xrand,yrand):
    y = yrand* CELLSIZE
    x = xrand* CELLSIZE
    foodrect = pygame.Rect(x,y,CELLSIZE,CELLSIZE)
    pygame.draw.rect(DISPLAYSURF,RED,foodrect)

def wall_collision(CELLWIDTH,CELLHEIGHT,coords):
    if coords[0]['x'] >= CELLWIDTH or coords[0]['x']< 0:
        return True
    if coords[0]['y'] >= CELLHEIGHT or coords[0]['y'] < 0:
        return True

def Game_over_screen():
    myfont = pygame.font.SysFont("stencil",100)
    gameover = myfont.render("GAME OVER",True,WHITE)
    gameoverrect = gameover.get_rect()
    gameoverrect.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)
    DISPLAYSURF.blit(gameover,gameoverrect)
    pygame.display.update() 



def drawsnakeintro(coords):
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
    text2 = myfont2.render("Press any key to Play or Esc to Quit",True,WHITE)
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

def score_writter(score):
    myfont = pygame.font.SysFont("stencil",40)
    scoretext = myfont.render("Score: "+str(score),True,WHITE)
    scorerect = scoretext.get_rect()
    scorerect.topright = (WINDOWWIDTH-10,10)
    DISPLAYSURF.blit(scoretext,scorerect)
    pygame.display.update() 



    
    




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
    # pygame.mixer.music.play(-1)
    while running:
        width = 200
        height = 100
        snake_body = coords[1:]
        for events in pygame.event.get():
            if events.type == QUIT:
                pygame.quit()
                quit()
            if events.type == KEYDOWN:
                if events.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                    main()
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
        snake = drawsnakeintro(coords)
       # print(snake)

        if snake[0] == 780 and snake[1] <= 90:
            direction = DOWN
        if snake[0] == 90 and snake[1] >= 510:
            direction = UP
        if snake[1] == 510 and snake[0] >= 780 :
            direction = LEFT
        if snake[1] == 90 and snake[0] <=90:
            direction = RIGHT
        DISPLAYSURF.blit(logo,(20,WINDOWHEIGHT-50))

        degrees += 5
       
        
        pygame.display.update()
        clock.tick(10)





def main():
    direction = RIGHT
    score =  0
    clock = pygame.time.Clock()
    startx = random.randint(4,CELLWIDTH-6)
    starty = random.randint(4,CELLHEIGHT -5) 
    coords = [{'x':startx,'y':starty},
            {'x':startx-1,'y':starty},
             {'x':startx-2,'y':starty}
             ]
   
    xrand,yrand = randcoords()
    running = True
    chop = False
    while running:
        snake_body = coords[1:]
        for events in pygame.event.get():
            if events.type == QUIT:
                pygame.quit()
                quit()
            if events.type == KEYDOWN:
                if events.key == K_ESCAPE:
                    running = False
                if events.key == K_DOWN  and direction != UP:
                    direction = DOWN
                if events.key == K_UP  and direction != DOWN:
                    direction = UP
                if events.key == K_LEFT  and direction != RIGHT:
                    direction = LEFT
                if events.key == K_RIGHT  and direction != LEFT:
                    direction = RIGHT
        if chop:

            xrand,yrand = randcoords()
            score+= 1

            chop = False
        else:
            del coords[-1]
        if direction == RIGHT:
            newhead = {'x':coords[0]['x']+1,'y':coords[0]['y']}
        if direction == LEFT:
            newhead = {'x':coords[0]['x']-1,'y':coords[0]['y']}
        if direction == UP:
            newhead = {'x':coords[0]['x'],'y':coords[0]['y']-1}
        if direction == DOWN:
            newhead = {'x':coords[0]['x'],'y':coords[0]['y']+1}

        
        coords.insert(0,newhead)
        for body in snake_body:
            if body['x'] == coords[0]['x'] and body['y'] == coords[0]['y']:
                crash.play()
                Game_over_screen()
                time.sleep(2)
                running = False

        
    
        DISPLAYSURF.fill(BLACK)
        drawsnake(coords)
        #drawGrid()
        drawFood(xrand,yrand)

        if xrand == coords[0]['x'] and yrand == coords[0]['y']:
            snakechop.play() 
            chop = True
        score_writter(score)
        if wall_collision(CELLWIDTH,CELLHEIGHT,coords):
            crash.play()
            Game_over_screen()
            time.sleep(2)
            running = False
        
        
        pygame.display.update()
        clock.tick(10)

game_intro()
