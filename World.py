'''
Created on Feb 10, 2013

@author: Brandon
'''

import pygame
from pygame.locals import *
import sys
from Unit import *
import math


pygame.init()
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Game Thingy')

background = pygame.image.load('640x480bg.png').convert()
fruit = pygame.image.load('24fruit.png')
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

#unit
unitObj = Unit()


foodlist = []

while True:
    screen.blit(background, (0, 0))
    #screen.fill(white)
    
    msgObjFood = fontObj.render(msg1, False, blue)
    msgRectObj = msgObjFood.get_rect()
    msgRectObj.topleft = (0, 0)
    screen.blit(msgObjFood, msgRectObj)
    
    msgObjEnergy = fontObj.render(msg2, False, red)
    msgfoodRect = msgObjEnergy.get_rect()
    msgfoodRect.topright = (640, 0)
    screen.blit(msgObjEnergy, msgfoodRect)
    
    #unit
    screen.blit(pygame.image.load(unitObj.currentImage), (int(unitObj.x - 24), int(unitObj.y - 24)))
    #pygame.draw.circle(screen, blue, (int(unit.x), int(unit.y)), 20, 0)
    

    for each in foodlist:
        #fruit is 24x24 so half is 12
        screen.blit(fruit, (each.pos[0] - 12, each.pos[1] - 12))
        #pygame.draw.circle(screen, green, (each.pos), 5, 0)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos
        elif event.type == MOUSEBUTTONUP:
            i = Food(event.pos)
            foodlist.append(i)
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    unitObj.frame(foodlist)
    msg1 = 'Unit Food: ' + str(int(unitObj.food))
    msg2 = 'Unit Energy: ' + str(int(unitObj.energy))
        
    pygame.display.update()
    fpsClock.tick(30)