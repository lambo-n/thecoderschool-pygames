"""Platforms: the solid boxes a PhysicsBody stands on, and how to read them.

CustomPlatform keeps its position and size as floats.  pygame.Rect stores whole
numbers, so a Rect-based platform silently rounds any fractional coordinate --
which matters as soon as a level is laid out with expressions like
SCREEN_WIDTH / (1280 / 400).  The int Rect is built only when it is drawn.

The physics engine lives in physicsBodyTemplate.py and reads platforms through
solid_boxes() below, so it works with CustomPlatforms, plain pygame.Rects,
(x, y, w, h) tuples, or anything carrying a .rect.
"""

import pygame

__all__ = ["CustomPlatform", "int_rect", "box_of", "solid_boxes"]


def int_rect(x, y, w, h):
    """Whole-pixel Rect for drawing, rounded so the size never wobbles.

    Rounding the two edges rather than the position and the size independently
    keeps a moving box from flickering a pixel wider and narrower as it goes.
    """
    left = int(round(x))
    top = int(round(y))
    return pygame.Rect(left, top, int(round(x + w)) - left, int(round(y + h)) - top)


def box_of(obj):
    """(left, top, right, bottom) as floats, from anything rect-shaped."""
    if hasattr(obj, "left") and hasattr(obj, "bottom"):
        return float(obj.left), float(obj.top), float(obj.right), float(obj.bottom)
    if hasattr(obj, "rect"):
        r = obj.rect
        return float(r.left), float(r.top), float(r.right), float(r.bottom)
    left, top, width, height = obj
    return float(left), float(top), float(left) + float(width), float(top) + float(height)


def solid_boxes(platforms):
    """Normalised, non-empty collision boxes for a list of platforms.

    Accepts a list, or a single platform on its own.  Platforms with
    `solid = False` are skipped, and so are platforms with no area: a
    zero-width or zero-height platform cannot be stood on, which is also how
    pygame treats an empty Rect.
    """
    if platforms is None:
        return []
    if isinstance(platforms, (CustomPlatform, pygame.Rect)) or hasattr(platforms, "rect"):
        platforms = [platforms]

    boxes = []
    for platform in platforms:
        if platform is None or not getattr(platform, "solid", True):
            continue
        left, top, right, bottom = box_of(platform)
        if left > right:
            left, right = right, left
        if top > bottom:
            top, bottom = bottom, top
        if right - left <= 0.0 or bottom - top <= 0.0:
            continue
        boxes.append((left, top, right, bottom))
    return boxes


class CustomPlatform:
    """A solid box.  Position and size are kept as floats.

    Negative widths and heights are normalised, so CustomPlatform(300, 400,
    -100, 20) is the same platform as CustomPlatform(200, 400, 100, 20) rather
    than an invisible box that collides with nothing.

    Set `solid = False` to turn a platform into decoration the physics ignores.
    """

    def __init__(self, posx, posy, width, height, color="white"):
        posx, posy = float(posx), float(posy)
        width, height = float(width), float(height)
        if width < 0.0:
            posx, width = posx + width, -width
        if height < 0.0:
            posy, height = posy + height, -height

        self.x = posx
        self.y = posy
        self.w = width
        self.h = height
        self.color = color
        self.solid = True

    # -- the names the old template used -----------------------------------
    @property
    def posx(self):
        return self.x

    @posx.setter
    def posx(self, value):
        self.x = float(value)

    @property
    def posy(self):
        return self.y

    @posy.setter
    def posy(self, value):
        self.y = float(value)

    @property
    def width(self):
        return self.w

    @width.setter
    def width(self, value):
        self.w = abs(float(value))

    @property
    def height(self):
        return self.h

    @height.setter
    def height(self, value):
        self.h = abs(float(value))

    # -- edges -------------------------------------------------------------
    @property
    def left(self):
        return self.x

    @left.setter
    def left(self, value):
        self.x = float(value)

    @property
    def right(self):
        return self.x + self.w

    @right.setter
    def right(self, value):
        self.x = float(value) - self.w

    @property
    def top(self):
        return self.y

    @top.setter
    def top(self, value):
        self.y = float(value)

    @property
    def bottom(self):
        return self.y + self.h

    @bottom.setter
    def bottom(self, value):
        self.y = float(value) - self.h

    @property
    def centerx(self):
        return self.x + self.w / 2.0

    @property
    def centery(self):
        return self.y + self.h / 2.0

    @property
    def rect(self):
        """Whole-pixel Rect, rebuilt on demand.  For drawing, not for physics."""
        return int_rect(self.x, self.y, self.w, self.h)

    def move(self, dx, dy):
        """Shift the platform.  The starting point for a moving platform.

        A body already resting on it is pushed back out on its next
        move_and_collide(), so a platform can be moved without checking who is
        standing on it.
        """
        self.x += float(dx)
        self.y += float(dy)

    def update(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def draw(self, screen):
        self.update(screen)
