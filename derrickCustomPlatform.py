import pygame
import random

# Types:
    # Normal - Black
    # Phase - Purple

# A platform is just a pygame.Rect that also remembers how to draw itself
# (its color) and what kind of platform it is (its type).
class CustomPlatform(pygame.Rect):
    def __init__(self, posx, posy, width, height, type="normal"):
        super().__init__(posx, posy, width, height)
        self.type = type
        flag = True
        while flag:
            if type == "normal" or type == 0:
                self.color = "#000000"
                type = "normal"
                flag = False
            elif type == "phase" or type == 1:
                self.color = "#AA4FFF"
                self.type = "phase"
                flag = False
            elif type == "climb" or type == 2:
                self.color = "#4FFF4F"
                self.type = "climb"
                flag = False
            elif type == "fall" or type == 3:
                self.color = "#FF4FFF"
                self.type = "fall"
                flag = False
            elif type == "bounce" or type == 4:
                self.color = "#80DFFF"
                self.type = "bounce"
                flag = False
            elif type == "speed" or type == 5:
                self.color = "#FF884F"
                self.type = "speed"
                flag = False
            elif type == "danger" or type == 6:
                self.color = "#F22525"
                self.type = "danger"
                flag = False
            elif type == "random":
                type = random.randint(0, 7)
                self.color = "#FFFFFF"
            # elif type == "crash":
                # self.color = "#F22525"
            else:
                self.color = "#000000" # Black
                flag = False
            # print(type)
