#### 4th The House#############
import os,pygame
from pygame.locals import *; pygame.init()
clock = pygame.time.Clock()
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
d = pygame.draw
pygame.display.set_caption("The House")
#Define some colors
white = (255,255,255); black = (0,0,0)
bg= (186,213,48); walls = (157,109,9)
door = (151,36,9); door_light = (181,132,14)
# coordinates of glass panes
windows = [(82,125),(82,215),(262,125),(262,215)]
#inti screen
screen = pygame.display.set_mode([423,347],0,32)
#the walls
screen.fill(bg) # fill the backgrond screen colour
d.rect(screen,black,(60,102,305,225))
d.rect(screen,walls,(73,114,280,200))
#the roof
d.polygon(screen,black,((35,112),(121,12),(296,12),(321,36),(321,12),(361,12),(361,86),(384,112)))
d.polygon(screen,black,((62,101),(128,23),(289,23),(334,69),(334,25),(348,25),(348,88),(361,101)))
# the door
d.rect(screen,black,(167,198,84,125))
d.rect(screen,door,(179,210,60,101))
d.rect(screen,black,(185,216,50,54))
d.rect(screen,door_light,(191,222,38,41))
d.circle(screen,black,(209,277),5)
# the window
for window in windows:
    d.rect(screen,black,(window[0],window[1], 76,76))
    d.rect(screen,white,(window[0]+12,window[1]+12, 22,22))#tl
    d.rect(screen,white,(window[0]+42,window[1]+12, 22,22))#tr
    d.rect(screen,white,(window[0]+12,window[1]+42, 22,22))#bl
    d.rect(screen,white,(window[0]+42,window[1]+42, 22,22))#rl
 
# to display
pygame.display.update()
pygame.time.wait(10000)
pygame.quit()                    
#####################

######### 3rd #########
##import os,pygame
##from pygame.locals import *; pygame.init()
##clock = pygame.time.Clock()
##os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
##pygame.display.set_caption("Geometric Shapes")
##screen = pygame.display.set_mode([800,600],0,32)
### Draw a Circle on screen in (red) at (x,y) coords (60,70) of diameter 40
##pygame.draw.circle(screen,(255,0,0),(60,70),40)
##pygame.display.update();pygame.time.wait(2000)
###Draw a Rectangle in yellow at (x,y,width,height)
##pygame.draw.rect(screen,(255,255,0),(70,70,120,60))
##pygame.display.update();pygame.time.wait(2000)
###Draw a polygon in green at ((x,y),(x,y),(x,y))
##pygame.draw.polygon(screen,(0,255,0),((120,100),(240,40),(220,130)))
##pygame.display.update();pygame.time.wait(2000)
###Draw Line in blue from (x,y) ,(xy), width
##pygame.draw.line(screen,(0,0,255),(10,150),(370,30),10)
##pygame.display.update();pygame.time.wait(2000)
###############################

######## 2nd ##############
###Disco Screen
##import os,pygame
##from pygame.locals import *; pygame.init()
##clock = pygame.time.Clock()
##os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
##pygame.display.set_caption("Disco Screen")
##screen = pygame.display.set_mode([400,200],0,32)
##screen.fill((255,0,0));pygame.display.update();pygame.time.wait(2000)
##screen.fill((255,255,0));pygame.display.update();pygame.time.wait(2000)
##screen.fill((0,255,0));pygame.display.update();pygame.time.wait(2000)
##screen.fill((0,0,255));pygame.display.update();pygame.time.wait(2000)
##screen.fill((255,0,255));pygame.display.update();pygame.time.wait(2000)
##screen.fill((255,255,255));pygame.display.update();pygame.time.wait(2000)
##screen.fill((0,0,0));pygame.display.update();pygame.time.wait(2000)
#########################

#############first 
###open a pygame graphics windo
##import os, pygame
##from pygame.locals import *
##pygame.init()
##clock = pygame.time.Clock()
##os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
###This title appers alsong the top of the praphics window
##pygame.display.set_caption("The Title of My Program")
###opens a window called 'screen' with width 400 height 200
##screen = pygame.display.set_mode([400,200],0,32)
##pygame.time.wait(5000) # A 5 secund pause before ending the program 
###############

