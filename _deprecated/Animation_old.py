'''
Created on Feb 16, 2014

@author: Brandon
'''

import pygame
from pygame.locals import *
import sys
import time
import pyganim


animImgs = {}
animObjs = {}

# 'images/OBJECTNAME/_OBJECTNAME_ACTION_DIRECTION'
# images example:     'images/llama/_llama_left'
# 'images/OBJECTNAME/DIRECTION_SPEEDTYPE.FRAMENUMBER'
# animations example: 'images/llama/up_walking.002'

# BASICALLY build a string like the example for each object that has animations


# needs an input of 'type'  ex: llama, human, tiger, sheep
def loadAnimations(oType):
    # setting up string to get animations
    string = "images/"
    # adding the type onto the string
    string = string + oType + "/"
    # adding on the random shit that this loop needs to work
    loopString = string + "%s.%s.png"
    # creating strings for the initial 3 .png's
    frontString = string + "_" + oType + "_front.png"
    backString = string + "_" + oType + "_back.png"
    leftString = string + "_" + oType + "_left.png"
    
    # load the "standing" sprites (these are single images, not animations)
    animImgs['front_standing'] = pygame.image.load(frontString)
    animImgs['back_standing'] = pygame.image.load(backString)
    animImgs['left_standing'] = pygame.image.load(leftString)
    animImgs['right_standing'] = pygame.transform.flip(animImgs['left_standing'], True, False)
    
    
    # creating the PygAnimation objects for walking/running in all directions except right direction
    animTypes = 'back_run back_walk front_run front_walk left_run left_walk left_sleep'.split() # llama_special, llama_idle, llama_sit
    for animType in animTypes:
        imagesAndDurations = [(loopString % (animType, str(num).rjust(3, '0')), 0.1) for num in range(6)]
        animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)
    
    # create the right-facing sprites by copying and flipping the left-facing sprites
    # right_walk
    animObjs['right_walk'] = animObjs['left_walk'].getCopy()
    animObjs['right_walk'].flip(True, False)
    animObjs['right_walk'].makeTransformsPermanent()
    # right_run
    animObjs['right_run'] = animObjs['left_run'].getCopy()
    animObjs['right_run'].flip(True, False)
    animObjs['right_run'].makeTransformsPermanent()
    # right_sleep
    animObjs['right_sleep'] = animObjs['left_sleep'].getCopy()
    animObjs['right_sleep'].flip(True, False)
    animObjs['right_sleep'].makeTransformsPermanent()
    # right_special
    '''
    animObjs['right_special'] = animObjs['left_special'].getCopy()
    animObjs['right_special'].flip(True, False)
    animObjs['right_special'].makeTransformsPermanent()
    '''
    
    return animImgs, animObjs