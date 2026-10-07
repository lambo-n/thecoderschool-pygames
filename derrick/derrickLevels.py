from derrick.derrickPlatform import *
import pygame

PLATFORM_COLOR = pygame.Color("#101010")

def level1():
    return [
        CustomPlatform(0, 650, 1280, 70, PLATFORM_COLOR),
        CustomPlatform(0, 0, 70, 720, PLATFORM_COLOR),
        CustomPlatform(1210, 0, 70, 720, PLATFORM_COLOR),
        CustomPlatform(0, 0, 1280, 70, PLATFORM_COLOR),
        CustomPlatform(220, 500, 300, 150, PLATFORM_COLOR),
        CustomPlatform(70, 220, 150, 150, PLATFORM_COLOR),
        CustomPlatform(700, 220, 150, 20, PLATFORM_COLOR),
        CustomPlatform(370, 220, 150, 150, PLATFORM_COLOR),
        CustomPlatform(220, 220, 150, 20, PLATFORM_COLOR)

    ]

levels = [level1]