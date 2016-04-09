'''
Created on Oct 12, 2013

@author: Brandon
'''

# import the relevant libraries
import pygame
import pygame.camera
from pygame.locals import *
#  initialise the display window
screen = pygame.display.set_mode([800,420])

# intialise pyGame
pygame.init()
# initialise the camera
pygame.camera.init()

camlist = pygame.camera.list_cameras()
print(camlist)

#  set up a camera object
cam = pygame.camera.Camera("/dev/video0",(640,480))
#  start the camera
cam.start()
#  fetch the camera image
image = cam.get_image()
#  blank out the screen - if you feel like it
screen.fill([0,0,0])
#  copy the camera image to the screen
screen.blit( image, ( 100, 0 ) )
#  update the screen to show the latest screen image
pygame.display.update()
pygame.display.flip()