import pygame
import random

def choose_random_powerup():
    powerUp_types = ["life", "speed", "jumpboost", "health", "immunity", "pierce"]
    return random.choice(powerUp_types)




def level1():
    [
        PowerUp(200,200, choose_random_powerup())
    ]


def level2():
    []


def level3():
    []


def level4():
    []


powers = [level1,level2,level3,level4]

class PowerUp:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type
        self.width = self.width = 50
        self.height = self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if type == "life":
            self.image = pygame.image.load("assets/orange-lightning.png")

        elif type == "speed":
            self.image = pygame.image.load("assets/yellow-lightning.png")

        elif type == "jumpboost":
            self.image = pygame.image.load("assets/cyan-lightning.png")

        elif type == "health":
            self.image = pygame.image.load("assets/pink-lightning.png")

        elif type == "immunity":
            self.image = pygame.image.load("assets/purple-lightning.png")

        elif type == "pierce":
            self.image = pygame.image.load("assets/blue-lightning.png")
        else:
            print("WRONG TYPE")
            exit()

        self.image = pygame.transform.scale(self.image,(self.width, self.height))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


        
