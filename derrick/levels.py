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
        CustomPlatform(820, 220, 200, 20, PLATFORM_COLOR),
        CustomPlatform(820, 480, 200, 20, PLATFORM_COLOR),
        CustomPlatform(1020, 350, 200, 20, PLATFORM_COLOR),
        CustomPlatform(370, 220, 450, 150, PLATFORM_COLOR),
        CustomPlatform(220, 220, 150, 20, PLATFORM_COLOR),
        CustomPlatform(670, 350, 150, 150, PLATFORM_COLOR),
        DeathBlock(670, 630, 100, 20, PLATFORM_RED_COLOR)

    ]

levels = [level1]