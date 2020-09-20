import os

import pygame

animation_list = {}

# 'images/OBJECTNAME/ACTION/DIRECTION/FRAMENUMBER'
# animations example: 'images/llama/walking/up/02'


def loadAnimations(object_name):
    for actions in os.scandir("images\\" + object_name):
        for directions in os.scandir(actions.path):
            for animations in os.scandir(directions.path):
                # Isolates the action, direction, and frame number from the file path to be used as the dictionary key
                formatted_key = animations.path[7:-4].replace("\\", "_").split("_", 1)[-1]
                animation_list[formatted_key] = pygame.image.load(animations.path)

    return animation_list
