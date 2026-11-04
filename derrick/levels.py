from customPlatform import CustomPlatform, DeathBlock, EndPortal
import pygame

PLATFORM_COLOR = pygame.Color("#101010")
PLATFORM_RED_COLOR = pygame.Color("#FF2B1B")

BOTTOM_LEFT_CORNER_START = (135, 615)

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
        DeathBlock(775, 650, 125, 20),
        DeathBlock(370, 220, 450, 20),
        CustomPlatform(500, 170, 200, 20, PLATFORM_COLOR),
        EndPortal(170, 170, 25, 25, 500, 500),

    ]

def level2():
    return [
        CustomPlatform(0, 650, 1280, 70, PLATFORM_COLOR),
        CustomPlatform(0, 0, 70, 720, PLATFORM_COLOR),
        CustomPlatform(1210, 0, 70, 720, PLATFORM_COLOR),
        CustomPlatform(0, 0, 1280, 70, PLATFORM_COLOR),
    ]

levels = [level1, level2]

startPositions = [(135, 615), (500, 500)]