import pygame
import time
import random

pygame.init()

##
#crash_sound = pygame.mixer.Sound("car_brake_crash.wav")
##

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
bright_red = (255,0,0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
lime = (0,200,0)
bright_lime = (0, 255, 0)

def random_color():
    first = random.randrange(0,255)
    secund = random.randrange(0,255)
    tred = random.randrange(0,255)
    my_color = (first,secund,tred)
    return my_color

my_color = random_color()

car_width = 130

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Car game')
clock = pygame.time.Clock()

carImg = pygame.image.load('my_car.png')
gameIcon = pygame.image.load('my_car.png')

pause = False


def things_dodged(count):
    font = pygame.font.SysFont("courier New", 25)
    text = font.render('Dodged: '+str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def crash():
    #pygame.mixer.Sound.play(crash_sound)
    #pybame.mixer.music.stop()
    
    largeText = pygame.font.SysFont("courier New", 75)
    TextSurf, TextRect = text_objects("NO!!! You Crashed", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button('Try Again',150,450,100,50,bright_lime,lime, game_loop)
        button('QUIT',550,450,100,50,bright_red,red, game_quit)

        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac, action = None): #ic = inactive color, ac = active color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()             
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    
    smallText = pygame.font.SysFont("courier New", 17)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def game_quit():
    pygame.quit()
    quit()

def unpaused():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    pygame.mixer.music.pause()
    
    largeText = pygame.font.SysFont("courier New", 100)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button('Continue',150,450,100,50,bright_lime,lime, unpaused)
        button('QUIT',550,450,100,50,bright_red,red, game_quit)

        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("courier New", 100)
        TextSurf, TextRect = text_objects("A Car Game", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button('GO!',150,450,100,50,bright_lime,lime, game_loop)
        button('QUIT',550,450,100,50,bright_red,red, game_quit)

        pygame.display.update()
        clock.tick(15)

def message_display(text):
    largeText = pygame.font.SysFont("courier New", 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop() 

def game_loop():
    global pause

    pygame.mixer.music.load("Periscope.mp3")
    pygame.mixer.music.play(-1)
    
    x = (display_width * 0.45)
    y = (display_height * 0.66)
    x_change = 0
##    car_speed = 0
##    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0
    
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_p:
                    pause = True
                    paused()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)
 
        things(thing_startx, thing_starty, thing_width, thing_height, my_color)
       
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
 
        if x > display_width - car_width or x < 0:
            crash()
 
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
 
        if y < thing_starty+thing_height:
            print('y crossover')
 
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash() 

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
game_quit()
quit()
