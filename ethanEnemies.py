import pygame


def level1():
    return[
        Enemy((400,500), pygame.image.load("assets/Skeleton.png"), 30, (400,300)),
    ]

def level2():
    return[
        Enemy((450,480), pygame.image.load("assets/Skeleton.png"), 30, (500,300)),
        Enemy((650,480), pygame.image.load("assets/Skeleton.png"), 30, (700, 300)),
    ]

def level3():
    return[
        Enemy((400,500), pygame.image.load("assets/Skeleton.png"), 30, (400, 300)),
        Enemy((500,600), pygame.image.load("assets/Skeleton.png"), 30, (500, 400)),
        Enemy((100,300), pygame.image.load("assets/Skeleton.png"), 30, (100,100)),
    ]

enemies = [level1, level2, level3]

class Enemy:
    def __init__(self, pos, image, health, target):
        self.current_pos = pygame.Vector2(pos)
        self.start_pos =  pygame.Vector2(pos)
        self.image = pygame.transform.scale(image, (80,80))
        self.health = health
        self.target =  pygame.Vector2(target)
        self. rect = self.image.get_rect(center=self.current_pos)

        self.speed = 200
        self.moving_to_target = True

    


    def update(self, dt):
        destination = self.target if self.moving_to_target else self.start_pos

        direction = destination - self.current_pos
        distance = direction.length()

        step = self.speed *dt

        if distance <= step:
            self.current_pos = pygame.Vector2(destination)
            self.moving_to_target = not self.moving_to_target

        else:
            self.current_pos += direction.normalize() * step


        self.rect.center = (round(self.current_pos.x), round(self.current_pos.y))
        
    def draw(self, screen):
        screen.blit( self.image, self.rect)
