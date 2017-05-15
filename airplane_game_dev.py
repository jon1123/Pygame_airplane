import pygame
import time
import random
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

pygame.init()

display_width = 800
display_height = 600

def random_color():
    first = random.randrange(0,255)
    secund = random.randrange(0,255)
    tred = random.randrange(0,255)
    my_color = (first,secund,tred)
    return my_color

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
orange = (255,128,0)
brown = (200,80,10)
green = (0,255,0)
blue = (0,0,255)
sky_gray = (200, 200, 200)
gray = (128, 128, 128)
bg = (186,213,48)
my_color = random_color()
my_other = random_color()
missl_color = random_color()

plane_width = 80
plane_height = 120

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('airplain game')
clock = pygame.time.Clock()

#pixAr = pygame.PixelArray(gameDisplay)

#pixAr[400][300] = black
#pixAr[400][500] = black
#pygame.draw.line(gameDisplay, blue, (100,200), (300,450), 5)
air_size = 20
air_width = 15
airx = int(display_width- (display_width/2))
airy = display_height-(5*air_size)

x_change = 0
y_change = 0

##def missal(air_size,air_width, airx,airy):
##    pixAr = pygame.PixelArray(gameDisplay)
##    flam4 = pygame.draw.line(gameDisplay, orange, (airx+4,airy+4*air_size), (airx+4,airy+4.7*air_size), 2)
##    flam5 = pygame.draw.line(gameDisplay, orange, (airx-4,airy+4*air_size), (airx-4,airy+4.7*air_size), 2)
##    flam6 = pygame.draw.line(gameDisplay, yellow, (airx,airy+4*air_size), (airx,airy+4.7*air_size), 2)
##    flam1 = pygame.draw.line(gameDisplay, red, (airx+4,airy+4*air_size), (airx+4,airy+4.5*air_size), 3)
##    flam2 = pygame.draw.line(gameDisplay, red, (airx-4,airy+4*air_size), (airx-4,airy+4.5*air_size), 3)
##    flam3 = pygame.draw.line(gameDisplay, red, (airx,airy+4*air_size), (airx,airy+4.5*air_size), 3)    frunt_cone = pygame.draw.polygon(gameDisplay, my_color,((airx-4,airy-air_size),(airx+3,airy-air_size),(airx+air_width,airy),(airx-air_width-1,airy)))
##    frunt = pygame.draw.circle(gameDisplay, my_color, (airx,airy), 0.5*air_width)
##    body = pygame.draw.rect(gameDisplay, my_color, (airx - air_width,airy, air_width, 1.5 * air_size))
##    wingfr = pygame.draw.polygon(gameDisplay, my_color,((airx,airy),(airx+1.5*air_size,airy+air_size),(airx,airy+air_size)))
##    wingfl = pygame.draw.polygon(gameDisplay, my_color,((airx,airy),(airx-1.5*air_size,airy+air_size),(airx,airy+air_size)))
##    wingbr = pygame.draw.polygon(gameDisplay, my_color,((airx,airy+air_size),(airx+0.5*air_size,airy+2*air_size),(airx,airy+2*air_size)))
##    wingbl = pygame.draw.polygon(gameDisplay, my_color,((airx,airy+air_size),(airx-0.5*air_size,airy+2*air_size),(airx,airy+2*air_size)))
##    detel1 = pygame.draw.line(gameDisplay, my_other, (airx-1,airy), (airx-1,airy+air_size), 15)
##    detel2 = pygame.draw.line(gameDisplay, my_other, (airx-4,airy+2.5*air_size), (airx-4,airy+3.5*air_size), 2)
##    detel3 = pygame.draw.line(gameDisplay, my_other, (airx+3,airy+2.5*air_size), (airx+3,airy+3.5*air_size), 2)
##    return frunt,body,wingfr,wingfl,wingbr,wingbl,frunt_cone,detel1,detel2,detel3,flam1,flam2,flam3,flam4,flam5,flam6

def air_plane(air_size,air_width, airx,airy):
    pixAr = pygame.PixelArray(gameDisplay)
    flam4 = pygame.draw.line(gameDisplay, orange, (airx+4,airy+4*air_size), (airx+4,airy+4.7*air_size), 2)
    flam5 = pygame.draw.line(gameDisplay, orange, (airx-4,airy+4*air_size), (airx-4,airy+4.7*air_size), 2)
    flam6 = pygame.draw.line(gameDisplay, yellow, (airx,airy+4*air_size), (airx,airy+4.7*air_size), 2)
    flam1 = pygame.draw.line(gameDisplay, red, (airx+4,airy+4*air_size), (airx+4,airy+4.5*air_size), 3)
    flam2 = pygame.draw.line(gameDisplay, red, (airx-4,airy+4*air_size), (airx-4,airy+4.5*air_size), 3)
    flam3 = pygame.draw.line(gameDisplay, red, (airx,airy+4*air_size), (airx,airy+4.5*air_size), 3)
    frunt_cone = pygame.draw.polygon(gameDisplay, my_color,((airx-4,airy-air_size),(airx+3,airy-air_size),(airx+air_width,airy),(airx-air_width-1,airy)))
    frunt = pygame.draw.circle(gameDisplay, my_color, (airx,airy), air_width)
    body = pygame.draw.rect(gameDisplay, my_color, (airx - air_width,airy, 2 * air_width, 3.5 * air_size))
    wingfr = pygame.draw.polygon(gameDisplay, my_color,((airx,airy),(airx+2.5*air_size,airy+2*air_size),(airx,airy+2*air_size)))
    wingfl = pygame.draw.polygon(gameDisplay, my_color,((airx,airy),(airx-2.5*air_size,airy+2*air_size),(airx,airy+2*air_size)))
    wingbr = pygame.draw.polygon(gameDisplay, my_color,((airx,airy+2*air_size),(airx+1.5*air_size,airy+4*air_size),(airx,airy+4*air_size)))
    wingbl = pygame.draw.polygon(gameDisplay, my_color,((airx,airy+2*air_size),(airx-1.5*air_size,airy+4*air_size),(airx,airy+4*air_size)))
    detel1 = pygame.draw.line(gameDisplay, my_other, (airx-1,airy), (airx-1,airy+air_size), 15)
    detel2 = pygame.draw.line(gameDisplay, my_other, (airx-4,airy+2.5*air_size), (airx-4,airy+3.5*air_size), 2)
    detel3 = pygame.draw.line(gameDisplay, my_other, (airx+3,airy+2.5*air_size), (airx+3,airy+3.5*air_size), 2)
    return frunt,body,wingfr,wingfl,wingbr,wingbl,frunt_cone,detel1,detel2,detel3,flam1,flam2,flam3,flam4,flam5,flam6

planeImg = air_plane(air_size,air_width, airx, airy)

#pygame.display.set_icon(planeImg)

pause = False

def things_dodged(dodged):
    font = pygame.font.SysFont("courier Regular", 25)
    text = font.render("Dodged: " + str(dodged),True, black)
    gameDisplay.blit(text,(1,1))

def things(thing_startx, thing_starty, thing_width, thing_height, color):
    body = pygame.draw.rect(gameDisplay,color,[thing_startx, thing_starty, thing_width, thing_height])
    frunt = pygame.draw.circle(gameDisplay, color, (thing_startx+int(0.5*thing_width),thing_starty+thing_height),int(0.5*thing_width))
    wingfr = pygame.draw.polygon(gameDisplay, color,((thing_startx+int(0.5*thing_width), thing_starty+thing_height),(thing_startx+1.5*thing_width,thing_starty+thing_width),(thing_startx,thing_starty+thing_width)))
    wingfl = pygame.draw.polygon(gameDisplay, color,((thing_startx+int(0.5*thing_width), thing_starty+thing_height),(thing_startx-0.5*thing_width,thing_starty+thing_width),(thing_startx,thing_starty+thing_width)))
    return body#thethings that will be avoided
  
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def crash():
    ####################################
    #pygame.mixer.Sound.play(crash_sound)
    #pygame.mixer.music.stop()
    ####################################
    largeText = pygame.font.SysFont("courier New",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        button("Play Again",150,450,100,50,green,blue,game_loop)
        button("Quit",550,450,100,50,red,blue,quitgame)

        pygame.display.update()
        clock.tick(15) 


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("courier Regular",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    ############
    pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("courier New",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("Continue",150,450,100,50,green,blue,unpause)
        button("Quit",550,450,100,50,red,blue,quitgame)

        pygame.display.update()
        clock.tick(15) 

def game_intro():
    intro = True
    pygame.mixer.music.load("AllaWhatParody.mp3")
    pygame.mixer.music.play(-1)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(sky_gray)
        largeText = pygame.font.SysFont("courier New", 115)
        TextSurf, TextRect = text_objects("Fly A Plane", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        

        button("GO!",150,450,100,50,green,blue,game_loop)
        button("Quit",550,450,100,50,red,blue,quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    pygame.mixer.music.load("AdagioInC.mp3")
    pygame.mixer.music.play(-1)
    air_size = 20
    air_width = 15
    airx = int(display_width- (display_width/2))
    airy = display_height-(5*air_size)

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_startx2 = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 25
    thing_height = 50
 
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
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        thing_starty += thing_speed            
        airx += x_change
        airy += y_change

        gameDisplay.fill(bg)

        things(thing_startx, thing_starty, thing_width, thing_height, black)

        air_plane(air_size,air_width, airx, airy)

        things_dodged(dodged)

        if dodged > 10:
            things(thing_startx2, thing_starty-70, thing_width, thing_height, black)
        if dodged > 20:
            things(int((thing_startx-thing_startx2)/2), thing_starty+70, thing_width, thing_height, missl_color)
            

        if airx > display_width - air_width or airx < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            #thing_width += (dodged * 1.2)
 
        if airy < thing_starty+thing_height:
            print('y crossover')
 
            if airx > thing_startx and airx < thing_startx + thing_width or airx+air_width > thing_startx and airx + air_width < thing_startx+thing_width:
                print('x crossover')
                crash()


        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
quit()



