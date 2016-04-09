'''
Created on Feb 10, 2013

@author: Brandon
'''

import pygame
from pygame.locals import *
from GrassManager import *
from Animal import *
from Food import *
import math
import time


pygame.init()
fpsClock = pygame.time.Clock()

WINDOWWIDTH  = 640
WINDOWHEIGHT = 480
screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('Llama Simulator 3000: Alpha v.004')

lightGreen = pygame.Color(130, 255, 130)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
#mouse
mouseX, mouseY = 0, 0

fontObj = pygame.font.Font('freesansbold.ttf', 18)
msg1 = ''
msg2 = ''

#creating the managers
gm = GrassManager()
#lists of all things on the screen
fruitlist = []
meatlist = []
tigerlist = []

framecount = 1 # frame count for debugging
while True:
    screen.fill(lightGreen)
    
    msgObjFood = fontObj.render(msg1, False, blue)
    msgRectObj = msgObjFood.get_rect()
    msgRectObj.topleft = (0, 0)
    screen.blit(msgObjFood, msgRectObj)
    msgObjEnergy = fontObj.render(msg2, False, red)
    msgfoodRect = msgObjEnergy.get_rect()
    msgfoodRect.topright = (WINDOWWIDTH, 0)
    screen.blit(msgObjEnergy, msgfoodRect)
        

    #Grass
    gl = gm.getGrasslist()
    print(len(gl))
    for each in gl:
        gm.frame(WINDOWWIDTH, WINDOWHEIGHT, each.getX(), each.getY())
        screen.set_at((each.getX(), each.getY()), each.getColor())
    gm.updateGrasslist()
    
    #Fruit
    for each in fruitlist:
        #fruit is 24x24 so half is 12
        screen.blit(each.getImage(), (int(each.x - 12), int(each.y - 12)))
    
    #Meat?
    for each in meatlist:
        #llama is 48x48 so half is 24
        screen.blit(each.getImage(), (int(each.x - 24), int(each.y - 24)))
        each.frame(fruitlist)
        msg1 = 'Unit Food: ' + str(int(each.food))
        msg2 = 'Unit Energy: ' + str(int(each.energy))
        
    #Tiger
    for each in tigerlist:
        #tiger is 48x48 so half is 24
        screen.blit(each.getImage(), (int(each.x - 24), int(each.y - 24)))
        each.frame(meatlist)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos
        elif event.type == MOUSEBUTTONUP:
            gm.createGrass((mouseX, mouseY))
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == K_c:  # clears everything
                i = 0
                length = len(fruitlist)
                while i < length:
                    fruitlist.remove(fruitlist[0])
                    i += 1
                length = len(meatlist)
                while i < length:
                    fruitlist.remove(meatlist[0])
                    i += 1
                length = len(tigerlist)
                while i < length:
                    fruitlist.remove(tigerlist[0])
                    i += 1
            elif event.key == K_l:
                i = Llama((mouseX, mouseY))
                meatlist.append(i)
            elif event.key == K_p:
                i = Pear((mouseX, mouseY))
                fruitlist.append(i)
            elif event.key == K_r:
                i = RottenPear((mouseX, mouseY))
                fruitlist.append(i)
            elif event.key == K_t:
                i = Tiger((mouseX, mouseY))
                tigerlist.append(i)

                
    print("frame: " + str(framecount))
    framecount += 1
    pygame.display.update()
    fpsClock.tick(30)