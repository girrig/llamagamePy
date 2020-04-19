import pygame
from pygame.locals import *

anim_dict = {}

# 'images/OBJECTNAME/_DIRECTION_ACTION'
# images example:     'images/llama/_left_llama'
# 'images/OBJECTNAME/DIRECTION_SPEEDTYPE.FRAMENUMBER'
# animations example: 'images/llama/up_walking.002'

# BASICALLY build a string like the example


# Needs an input of 'type'  ex: llama, human, tiger, sheep
def loadAnimations(oType):
    # Setting up string to get animations
    string = "images/"
    # Adding the type onto the string
    string = string + oType + "/"
    # Adding on the random shit that this loop needs to work
    imgLoopString = string + "_%s_%s.png"
    animLoopString = string + "%s_%s.%s.png"

    directionTypes = 'left front back'.split()

    imgTypes = 'dead stand sit'.split()
    for direction in directionTypes:
        for img in imgTypes:
            if "left" in direction:  # for left/right images
                # Temp string for right
                rightDirection = direction.replace("left", "right")
                # Left/right facing images
                temp = anim_dict["_%s_%s" % (direction, img)] = pygame.image.load(imgLoopString % (direction, img))
                anim_dict["_%s_%s" % (rightDirection, img)] = pygame.transform.flip(temp, True, False)
            else:  # Front; Back
                anim_dict["_%s_%s" % (direction, img)] = pygame.image.load(imgLoopString % (direction, img))

    # NOTE: Left animations must be loaded before right animations
    animTypes = 'walk run sleep'.split()  # llama_special, llama_idle
    for direction in directionTypes:
        for anim in animTypes:
            if "left" in direction:  # for left/right images
                # Temp string for right
                rightDirection = direction.replace("left", "right")
                # Left/right facing images
                for num in range(6):  # 0-5
                    temp = anim_dict["%s_%s.%s" % (direction, anim, str(num).rjust(3, '0'))] = pygame.image.load(animLoopString % (direction, anim, str(num).rjust(3, '0')))
                    anim_dict["%s_%s.%s" % (rightDirection, anim, str(num).rjust(3, '0'))] = pygame.transform.flip(temp, True, False)
            else:  # Anything else
                for num in range(6):  # 0-5
                    anim_dict["%s_%s.%s" % (direction, anim, str(num).rjust(3, '0'))] = pygame.image.load(animLoopString % (direction, anim, str(num).rjust(3, '0')))

    return anim_dict
