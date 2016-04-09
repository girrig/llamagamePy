'''
Created on Feb 10, 2013

@author: Brandon
'''

import pygame
from pygame.locals import *
from Player import Player
from Animal import Llama, Tiger
from Food import Apple, Pear
import math
import time


class World():
    def __init__(self, width=1280, height=720):
        pygame.init()
        self.width = width
        self.height = height
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Llama Simulator 3000: Alpha v0.006')

        self.lightgreen = pygame.Color(130, 255, 130)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)
        self.white = pygame.Color(255, 255, 255)
        self.black = pygame.Color(0, 0, 0)

        #mouse
        self.mouseX, self.mouseY = 0, 0

        self.font = pygame.font.Font('freesansbold.ttf', 18)

        # lists of all things on the screen
        self.fruitlist = []
        self.llamalist = []
        self.tigerlist = []

        # Player
        self.player = Player((self.width/2, self.height/2))
        self.direction = 'down'
        self.moveUp = self.moveDown = self.moveLeft = self.moveRight = False

        # Loop
        self.done = False


    #### MAIN LOOP FUCTIONS ####
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEMOTION:
                self.mouseX, self.mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
                continue  # maybe a movement action?
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == K_UP:
                    self.moveUp = True
                    self.moveDown = False
                    if not self.moveLeft and not self.moveRight:
                        # only change the direction to up if the player wasn't moving left/right
                        self.direction = 'up'
                elif event.key == K_DOWN:
                    self.moveDown = True
                    self.moveUp = False
                    if not self.moveLeft and not self.moveRight:
                        self.direction = 'down'
                elif event.key == K_LEFT:
                    self.moveLeft = True
                    self.moveRight = False
                    if not self.moveUp and not self.moveDown:
                        self.direction = 'left'
                elif event.key == K_RIGHT:
                    self.moveRight = True
                    self.moveLeft = False
                    if not self.moveUp and not self.moveDown:
                        self.direction = 'right'
                elif event.key == K_c:  # clears everything
                    del self.fruitlist[:]
                    del self.llamalist[:]
                    del self.tigerlist[:]
                elif event.key == K_l:
                    self.llamalist.append(Llama((self.mouseX, self.mouseY)))
                elif event.key == K_p:
                    self.fruitlist.append(Pear((self.mouseX, self.mouseY)))
                elif event.key == K_a:
                    self.fruitlist.append(Apple((self.mouseX, self.mouseY)))
                elif event.key == K_t:
                    self.tigerlist.append(Tiger((self.mouseX, self. mouseY)))
            elif event.type == KEYUP:
                if event.key == K_UP:
                    self.moveUp = False
                    # if the player was moving in a sideways direction before, change the self.direction the player is facing.
                    if self.moveLeft:
                        self.direction = 'left'
                    if self.moveRight:
                        self.direction = 'right'
                elif event.key == K_DOWN:
                    self.moveDown = False
                    if self.moveLeft:
                        self.direction = 'left'
                    if self.moveRight:
                        self.direction = 'right'
                elif event.key == K_LEFT:
                    self.moveLeft = False
                    if self.moveUp:
                        self.direction = 'up'
                    if self.moveDown:
                        self.direction = 'down'
                elif event.key == K_RIGHT:
                    self.moveRight = False
                    if self.moveUp:
                        self.direction = 'up'
                    if self.moveDown:
                        self.direction = 'down'

    def update(self):
        self.updateMap()
        self.updateLists()
        self.updatePlayer()

    def draw(self):
        # order matters here
        self.drawMap()
        self.drawPlayer()
        self.drawLists()

    #### SUB FUNCTIONS ####
    def updateMap(self):
        pass

    def updateLists(self):
        # Llama
        for each in self.llamalist:
            each.update(self.fruitlist)

        # Tiger
        for each in self.tigerlist:
            each.update(self.llamalist)

    def updatePlayer(self):
        # actually move the position of the player
        if self.moveUp:
            self.player.y -= self.player.speed
        if self.moveDown:
            self.player.y += self.player.speed
        if self.moveLeft:
            self.player.x -= self.player.speed
        if self.moveRight:
            self.player.x += self.player.speed

    def drawMap(self):
        self.screen.fill(self.lightgreen)

    def drawPlayer(self):
        if self.moveUp or self.moveDown or self.moveLeft or self.moveRight:  # moving
            # draw the correct walking/running sprite from the animation object
            if self.direction == 'up':
                self.screen.blit(self.player.getAnimation('back_walk.00' + str(self.player.anim_frame)), (self.player.x, self.player.y))
            elif self.direction == 'down':
                self.screen.blit(self.player.getAnimation('front_walk.00' + str(self.player.anim_frame)), (self.player.x, self.player.y))
            elif self.direction == 'left':
                self.screen.blit(self.player.getAnimation('left_walk.00' + str(self.player.anim_frame)), (self.player.x, self.player.y))
            elif self.direction == 'right':
                self.screen.blit(self.player.getAnimation('right_walk.00' + str(self.player.anim_frame)), (self.player.x, self.player.y))
            self.player.update_anim()
        else:  # standing still
            self.player.anim_frame = 0
            if self.direction == 'up':
                self.screen.blit(self.player.getAnimation('_back_stand'), (self.player.x, self.player.y))
            elif self.direction == 'down':
                self.screen.blit(self.player.getAnimation('_front_stand'), (self.player.x, self.player.y))
            elif self.direction == "left":
                self.screen.blit(self.player.getAnimation('_left_stand'), (self.player.x, self.player.y))
            elif self.direction == "right":
                self.screen.blit(self.player.getAnimation('_right_stand'), (self.player.x, self.player.y))

    def drawLists(self):
        # Fruit
        for each in self.fruitlist:
            # fruit is 24x24 so half is 12
            self.screen.blit(each.getImage(), (int(each.x - 12), int(each.y - 12)))

        # Llama
        for each in self.llamalist:
            each.paint(self.screen)

        # Tiger
        for each in self.tigerlist:
            each.paint(self.screen)

    def mainLoop(self):
        framecount = 0  # frame count for debugging
        while not self.done:
            self.handleEvents()
            self.update()
            self.draw()

            # updates certain sections of the screen based on parameters (No parameters = full screen refresh)
            pygame.display.update()
            #print("frame: " + str(framecount))
            framecount += 1
            self.fpsClock.tick(30)
