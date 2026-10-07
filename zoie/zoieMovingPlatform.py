import pygame


class MovingPlatform:
    def __init__(self, x, y, width, height, moving_dir=1, bound_min=50, bound_max=600, axis='y'):
        self.rect = pygame.Rect(x, y, width, height)
        self.moving_dir = moving_dir
        self.bound_min = bound_min
        self.bound_max = bound_max
        self.axis = axis
        self.prev_x = x
        self.prev_y = y

    def update(self, dt):
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        if self.axis == 'y':
            self.rect.y += self.moving_dir * 150 * dt
            if self.rect.top >= self.bound_max:
                self.rect.y = self.bound_max - 1
                self.moving_dir *= -1
            elif  self.rect.bottom <= self.bound_min:
                self.rect.y = self.bound_min
                self.moving_dir *= -1
        else:
            self.rect.x += self.moving_dir * 150 * dt
            if self.rect.right >= self.bound_max:
                self.rect.x = self.bound_max - self.rect.width
                self.moving_dir *= -1
            elif self.rect.left <= self.bound_min:
                self.rect.x = self.bound_min
                self.moving_dir *= -1