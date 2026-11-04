import pygame
import random

def choose_random_powerup():
    powerUp_types = ["life", "speed", "jumpboost", "health", "invincibility", "pierce"]
    return random.choice(powerUp_types)




def level1():
    return [
        PowerUp(200,200, "speed"),
        PowerUp(400,200, "health"),
        PowerUp(600,200, "jumpboost"),
        PowerUp(100,500, "invincibility"),
        PowerUp(200,550, "pierce"),
        PowerUp(600,550, "life")
    ]



def level2():
    return []


def level3():
    return []


def level4():
    return []


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

        elif type == "invincibility":
            self.image = pygame.image.load("assets/purple-lightning.png")

        elif type == "pierce":
            self.image = pygame.image.load("assets/blue-lightning.png")
        else:
            print("WRONG TYPE")
            exit()

        self.image = pygame.transform.scale(self.image,(self.width, self.height))


    def draw(self, screen):
        screen.blit(self.image, self.rect)


        
