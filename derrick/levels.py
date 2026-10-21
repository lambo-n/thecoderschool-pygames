from customPlatform import CustomPlatform, DeathBlock
import pygame

PLATFORM_COLOR = pygame.Color("#101010")
PLATFORM_RED_COLOR = pygame.Color("#FF2B1B")

def level1():
    return [
        CustomPlatform(0, 650, 1280, 70, PLATFORM_COLOR),
        CustomPlatform(0, 0, 70, 720, PLATFORM_COLOR),
        CustomPlatform(1210, 0, 70, 720, PLATFORM_COLOR),
        CustomPlatform(0, 0, 1280, 70, PLATFORM_COLOR),
        CustomPlatform(220, 500, 300, 150, PLATFORM_COLOR),
        CustomPlatform(70, 220, 150, 150, PLATFORM_COLOR),
        CustomPlatform(820, 220, 200, 40, PLATFORM_COLOR),
        CustomPlatform(820, 460, 200, 40, PLATFORM_COLOR),
        CustomPlatform(1020, 340, 200, 40, PLATFORM_COLOR),
        CustomPlatform(370, 220, 450, 150, PLATFORM_COLOR),
        CustomPlatform(220, 220, 150, 40, PLATFORM_COLOR),
        CustomPlatform(670, 350, 150, 150, PLATFORM_COLOR),
        DeathBlock(775, 650, 125, 20, PLATFORM_RED_COLOR),
        DeathBlock(370, 220, 450, 20, PLATFORM_RED_COLOR),
        CustomPlatform(500, 170, 200, 20, PLATFORM_COLOR)

    ]

levels = [level1]