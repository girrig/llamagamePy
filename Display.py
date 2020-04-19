import pygame
from pygame.locals import (K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, KEYDOWN,
                           KEYUP, MOUSEBUTTONUP, MOUSEMOTION, QUIT, K_a, K_c,
                           K_l, K_p, K_t)

from Animal import Llama, Tiger
from Fruit import Apple, Pear
from Player import Player


class Display():
    def __init__(self, width=1280, height=720):
        pygame.init()
        self.width = width
        self.height = height
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('LlamaGame: Alpha v0.007')

        # Colors
        self.lightgreen = pygame.Color(130, 255, 130)
        self.black = pygame.Color(0, 0, 0)

        # Font for text display
        self.font = pygame.font.SysFont('Calibri', 18)

        # Lists of all things on the screen
        self.fruitlist = []
        self.llamalist = []
        self.tigerlist = []

        # Player
        self.player = Player((self.width / 2, self.height / 2))

        # Loop variables
        self.framecount = 0  # Frame count for debugging
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
                pass  # Maybe a movement action?
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == K_UP:
                    self.player.moveUp = True
                    self.player.moveDown = False
                    if not self.player.moveLeft and not self.player.moveRight:
                        # Only change the direction to up if the player wasn't moving left/right
                        self.player.direction = 'up'
                elif event.key == K_DOWN:
                    self.player.moveDown = True
                    self.player.moveUp = False
                    if not self.player.moveLeft and not self.player.moveRight:
                        self.player.direction = 'down'
                elif event.key == K_LEFT:
                    self.player.moveLeft = True
                    self.player.moveRight = False
                    if not self.player.moveUp and not self.player.moveDown:
                        self.player.direction = 'left'
                elif event.key == K_RIGHT:
                    self.player.moveRight = True
                    self.player.moveLeft = False
                    if not self.player.moveUp and not self.player.moveDown:
                        self.player.direction = 'right'
                elif event.key == K_c:  # Clears everything
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
                    self.player.moveUp = False
                    # If the player was moving in a sideways direction before, change the self.direction the player is facing
                    if self.player.moveLeft:
                        self.player.direction = 'left'
                    if self.player.moveRight:
                        self.player.direction = 'right'
                elif event.key == K_DOWN:
                    self.player.moveDown = False
                    if self.player.moveLeft:
                        self.player.direction = 'left'
                    if self.player.moveRight:
                        self.player.direction = 'right'
                elif event.key == K_LEFT:
                    self.player.moveLeft = False
                    if self.player.moveUp:
                        self.player.direction = 'up'
                    if self.player.moveDown:
                        self.player.direction = 'down'
                elif event.key == K_RIGHT:
                    self.player.moveRight = False
                    if self.player.moveUp:
                        self.player.direction = 'up'
                    if self.player.moveDown:
                        self.player.direction = 'down'

    def update(self, deltaT):
        # Not using deltaT yet
        self.updateMap()
        self.updateLists()
        self.updatePlayer()

    def draw(self):
        # Order matters here
        self.drawMap()
        self.drawLists()
        self.drawPlayer()

    #### SUB FUNCTIONS ####
    def updateMap(self):
        pass

    def updateLists(self):
        # Fruit
        for each in self.fruitlist:
            each.update()

        # Llama
        for each in self.llamalist:
            each.update(self.fruitlist)

        # Tiger
        for each in self.tigerlist:
            each.update(self.llamalist)

    def updatePlayer(self):
        self.player.update()

    def drawMap(self):
        self.screen.fill(self.lightgreen)

        # Frame counter
        frames_text = 'frame#:' + str(self.framecount)
        frames_text_font = self.font.render(frames_text, False, self.black)
        frames_text_rect = frames_text_font.get_rect()
        frames_text_rect.topleft = (10, 10)
        self.screen.blit(frames_text_font, frames_text_rect)

        # FPS counter
        fps_text = 'fps:' + str(int(self.fpsClock.get_fps()))
        fps_text_font = self.font.render(fps_text, False, self.black)
        fps_text_rect = fps_text_font.get_rect()
        fps_text_rect.topleft = (10, 30)
        self.screen.blit(fps_text_font, fps_text_rect)

    def drawLists(self):
        # Fruit
        for each in self.fruitlist:
            # fruit is 24x24 so half is 12
            self.screen.blit(each.getImage(), (int(each.pos_x - 12), int(each.pos_y - 12)))

        # Llama
        for each in self.llamalist:
            each.paint(self.screen)

        # Tiger
        for each in self.tigerlist:
            each.paint(self.screen)

    def drawPlayer(self):
        self.player.paint(self.screen)

    def mainLoop(self):
        lag = 0.0
        MS_PER_UPDATE = 15

        while not self.done:
            # Time keeping
            currentTime = self.fpsClock.get_time()
            lag = lag + currentTime

            self.handleEvents()

            while (lag >= MS_PER_UPDATE):
                self.update(lag / MS_PER_UPDATE)
                pygame.display.update()  # Updates certain sections of the screen based on parameters (No parameters = full screen refresh)
                lag = lag - MS_PER_UPDATE

            self.draw()

            self.framecount += 1
            self.fpsClock.tick(120)
