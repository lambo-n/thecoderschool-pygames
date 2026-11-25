import pygame
import math

class Projectile:

    def __init__(self, posx, posy, width, height, direction, speed, color="white"):

        self.x = posx
        self.y = posy
        self.w = width
        self.h = height
        self.d = direction
        self.s = speed
        self.color = color

        self.image = None

        angle_rad = math.radians(direction)

        self.vx = math.cos(angle_rad) * speed
        self.vy = math.sin(angle_rad) * speed


        # Direction is measued in Degrees with 0 Degrees being straight to the right
        # Goes counterclockwise

    def update(self, dt):

        self.x += self.vx * dt
        self.y -= self.vy * dt

    def draw(self, screen):
        #screen.blit(self.image, (self.x, self.y))
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.w)
        

class StandardBullet(Projectile):

    def __init__(self, posx, posy, width, height, direction, speed, color="white"):
        super().__init__(posx, posy, width, height, direction, speed, color)

        #self.image = pygame.image.load()

# class Bomb(Projectile):

#     def __init__(self, posx, posy, width, height, direction, speed, radius, color="white"):
#         super().__init__(posx, posy, width, height, direction, speed, color)

#         self.image = pygame.image.load()

#         self.r = radius