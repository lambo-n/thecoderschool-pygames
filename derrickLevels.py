from derrickPlatform import *
import pygame

PLATFORM_COLOR = pygame.Color("#101010")

def level1():
    return [
        CustomPlatform(0, 670, 1280, 50, PLATFORM_COLOR),
        CustomPlatform(0, 0, 50, 720, PLATFORM_COLOR),
        CustomPlatform(1230, 0, 50, 720, PLATFORM_COLOR),
        CustomPlatform(0, 0, 1280, 50, PLATFORM_COLOR),
        CustomPlatform(200, 520, 250, 150, PLATFORM_COLOR),
        CustomPlatform(50, 200, 150, 150, PLATFORM_COLOR),
        CustomPlatform(700, 220, 150, 20, PLATFORM_COLOR),
        CustomPlatform(350, 200, 150, 150, PLATFORM_COLOR)

    ]

levels = [level1]