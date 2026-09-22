"""PhysicsBody: a box that falls, walks and collides with platforms.

The engine is deliberately boring, which is what makes it reliable:

  * Float geometry.  pygame.Rect stores whole numbers, so a Rect-based player
    throws away the fractional part of every single move.  The body keeps
    floats and only builds an int Rect at the moment it is drawn.
  * One axis at a time.  Horizontal movement is applied and resolved, then
    vertical movement is applied and resolved.  That removes the "which way do
    I push?" guess that minimum-overlap resolution has to make, so landing on
    a thin ledge never shoves you sideways, and running into a tall wall never
    pretends to be a floor.
  * Only surfaces you actually crossed.  A step snaps to the faces the body
    moved through this step, never to a face it is already behind, so nothing
    ever teleports backwards out of a platform.
  * Substepping.  A move is chopped into pieces no bigger than half the body,
    so a fast fall can never skip straight over a thin platform.
  * Ground wins.  A body caught in a gap shorter than it is stays on the floor
    and reports `squeezed` instead of popping up through a ceiling, and a
    platform descending onto it crushes it rather than lifting it up on top.
  * Bumping your head pushes you back down (HEAD_BUMP_SPEED) instead of
    leaving you with upward velocity pressed against the underside.

Typical use:

    from platformTemplate import CustomPlatform
    from physicsBodyTemplate import PhysicsBody

    player = PhysicsBody(620, 320, 40, 40)
    ...
    player.vel_x = -300 if left_held else 300 if right_held else 0
    if jump_pressed and player.on_ground:
        player.jump(600)
    player.move_and_collide(platformList, dt, bounds=screen.get_rect())
    player.draw(screen)
"""

import math

import pygame

from platformTemplate import box_of, int_rect, solid_boxes

__all__ = [
    "PhysicsBody",
    "GRAVITY",
    "TERMINAL_VELOCITY",
    "MAX_DT",
    "HEAD_BUMP_SPEED",
    "CORNER_CORRECTION",
    "GROUND_PROBE",
]

# Downward acceleration, pixels per second per second.
GRAVITY = 1000.0

# Speed cap.  Without one, a long fall eventually covers more ground in a
# single frame than a platform is thick, and substepping has to work far harder
# to keep up.
TERMINAL_VELOCITY = 1600.0

# The longest frame the physics will believe in.  Dragging the window, hitting
# a breakpoint or loading an image can hand you a dt of several seconds;
# without this clamp the player teleports across the level in one step.
MAX_DT = 1.0 / 30.0

# How hard a head bump pushes you back down, pixels per second.
HEAD_BUMP_SPEED = 120.0

# If a jump clips the corner of a platform by this many pixels or fewer, the
# body is nudged sideways around it instead of having its jump killed.  Set it
# to 0 to turn the forgiveness off.
CORNER_CORRECTION = 6.0

# How far below the feet to look when deciding `on_ground`.  Keeps the flag
# steady while resting, and stops a 1-pixel gap from eating a jump.
GROUND_PROBE = 1.0

# Safety valve on the substep loop.  Never reached at sane speeds.
MAX_SUBSTEPS = 256

# Overlaps thinner than this are floating-point noise, not collisions.  Without
# it, `y = platform.top - height` can land a hair inside the platform, and the
# body sticks to the ledge it is standing on.
SKIN = 1e-6


class PhysicsBody:
    """A box that falls, walks and collides with platforms.

    x, y is the top-left corner, matching pygame.Rect and CustomPlatform.  Use
    PhysicsBody.from_center(...) if you would rather give the middle.

    Read these after each move_and_collide():
        on_ground       standing on a platform, on the bounds floor, or within
                        GROUND_PROBE pixels above one
        hit_head        bumped a ceiling this frame (and got pushed back down)
        hit_wall_left   blocked moving left
        hit_wall_right  blocked moving right
        squeezed        the gap is shorter or narrower than the body; the body
                        was kept in place rather than pushed through anything
    """

    def __init__(self, x, y, width, height, color="gold"):
        self.x = float(x)
        self.y = float(y)
        self.w = abs(float(width))
        self.h = abs(float(height))
        self.color = color

        self.vel_x = 0.0
        self.vel_y = 0.0

        # Per-body tuning, so one body can be floatier than another.
        self.gravity = GRAVITY
        self.terminal_velocity = TERMINAL_VELOCITY
        self.head_bump_speed = HEAD_BUMP_SPEED
        self.corner_correction = CORNER_CORRECTION
        self.max_dt = MAX_DT

        self.on_ground = False
        self.hit_head = False
        self.hit_wall_left = False
        self.hit_wall_right = False
        self.squeezed = False

    @classmethod
    def from_center(cls, centerx, centery, width, height, color="gold"):
        return cls(centerx - width / 2.0, centery - height / 2.0, width, height, color)

    # -- geometry ----------------------------------------------------------
    @property
    def width(self):
        return self.w

    @property
    def height(self):
        return self.h

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

    @centerx.setter
    def centerx(self, value):
        self.x = float(value) - self.w / 2.0

    @property
    def centery(self):
        return self.y + self.h / 2.0

    @centery.setter
    def centery(self, value):
        self.y = float(value) - self.h / 2.0

    @property
    def center(self):
        return pygame.Vector2(self.centerx, self.centery)

    @center.setter
    def center(self, value):
        self.centerx, self.centery = float(value[0]), float(value[1])

    @property
    def rect(self):
        return int_rect(self.x, self.y, self.w, self.h)

    def resize(self, width, height):
        """Change the body's size without dropping it through the floor.

        Keeps the feet and the horizontal centre put, which is what crouching,
        growing, or swapping to a differently sized sprite wants.  If the new
        size overlaps something, the next move_and_collide() pushes it out.
        """
        centerx, bottom = self.centerx, self.bottom
        self.w = abs(float(width))
        self.h = abs(float(height))
        self.centerx = centerx
        self.bottom = bottom

    # -- movement ----------------------------------------------------------
    def jump(self, speed=600.0):
        """Launch upward.  Check `on_ground` yourself before calling."""
        self.vel_y = -abs(float(speed))
        self.on_ground = False

    def move_and_collide(self, platforms, dt, bounds=None, gravity=None):
        """Apply gravity, move, and resolve every collision.

        platforms -- list of CustomPlatforms / Rects / (x, y, w, h) tuples
        dt        -- seconds since the last frame (clamped to self.max_dt)
        bounds    -- optional rect the body is kept inside; its floor grounds
                     the body and its ceiling triggers a head bump
        gravity   -- overrides self.gravity for this frame (0 to hover)
        """
        self.on_ground = False
        self.hit_head = False
        self.hit_wall_left = False
        self.hit_wall_right = False
        self.squeezed = False

        boxes = solid_boxes(platforms)
        limits = box_of(bounds) if bounds is not None else None

        try:
            dt = float(dt)
        except (TypeError, ValueError):
            dt = 0.0
        if not math.isfinite(dt) or dt <= 0.0:
            dt = 0.0
        dt = min(dt, self.max_dt)

        # Something may have moved into the body since last frame: a moving
        # platform, a resize, a teleport, a body spawned inside the level.  Get
        # out first, or the axis passes below have no clean answer.
        self._depenetrate(boxes, limits)

        accel = self.gravity if gravity is None else float(gravity)
        self.vel_y += accel * dt
        if self.vel_y > self.terminal_velocity:
            self.vel_y = self.terminal_velocity
        elif self.vel_y < -self.terminal_velocity:
            self.vel_y = -self.terminal_velocity

        dx = self.vel_x * dt
        dy = self.vel_y * dt

        # Never travel more than half the body in one step, so nothing thin
        # enough to fit between two samples can be missed.
        step_limit = max(1.0, min(self.w, self.h) * 0.5)
        steps = min(int(max(abs(dx), abs(dy)) / step_limit) + 1, MAX_SUBSTEPS)
        step_x = dx / steps
        step_y = dy / steps

        for _ in range(steps):
            prev_x = self.x
            self.x += step_x
            self._resolve_x(boxes, step_x, limits, prev_x)
            prev_y = self.y
            self.y += step_y
            self._resolve_y(boxes, step_y, limits, prev_y)

        # A resting body barely moves, and a body with gravity switched off
        # does not move at all, so confirm `on_ground` by looking under the feet.
        if not self.on_ground and self.vel_y >= 0.0 and self._has_support(boxes, limits):
            self.on_ground = True

        return self

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    # -- collision internals ----------------------------------------------
    def _overlaps(self, box):
        left, top, right, bottom = box
        return (
            self.x < right - SKIN
            and self.x + self.w > left + SKIN
            and self.y < bottom - SKIN
            and self.y + self.h > top + SKIN
        )

    def _blockers(self, boxes):
        return [box for box in boxes if self._overlaps(box)]

    def _has_support(self, boxes, limits, ignore=None):
        """Is there a surface directly under the feet?

        Only counts tops that are level with the feet (within GROUND_PROBE), so
        a ceiling the body happens to be overlapping is never mistaken for a
        floor.  `ignore` skips one box, to ask "is anything *else* holding me
        up?".
        """
        feet = self.y + self.h
        if limits is not None and feet >= limits[3] - GROUND_PROBE:
            return True
        for box in boxes:
            if box is ignore:
                continue
            left, top, right, bottom = box
            if top < feet - SKIN or top > feet + GROUND_PROBE:
                continue
            if self.x < right - SKIN and self.x + self.w > left + SKIN:
                return True
        return False

    def _resolve_x(self, boxes, direction, limits, prev_x):
        """Undo horizontal penetration only -- never touches y.

        Only faces the body actually crossed this step count.  Snapping to a
        face it is already behind would teleport it backwards, so a body that
        somehow ends up inside a platform is left to _depenetrate.

        Taking the extreme edge over every overlapping platform at once makes
        the result independent of list order, so a wall built from a stack of
        platforms behaves exactly like one tall platform.
        """
        if direction > 0.0:
            prev_right = prev_x + self.w
            faces = [box[0] for box in self._blockers(boxes) if box[0] >= prev_right - SKIN]
            if faces:
                self.x = min(faces) - self.w
                self.vel_x = 0.0
                self.hit_wall_right = True
        elif direction < 0.0:
            faces = [box[2] for box in self._blockers(boxes) if box[2] <= prev_x + SKIN]
            if faces:
                self.x = max(faces)
                self.vel_x = 0.0
                self.hit_wall_left = True

        if limits is not None:
            if self.x < limits[0]:
                self.x = limits[0]
                self.vel_x = max(self.vel_x, 0.0)
                self.hit_wall_left = True
            elif self.x + self.w > limits[2]:
                self.x = limits[2] - self.w
                self.vel_x = min(self.vel_x, 0.0)
                self.hit_wall_right = True

    def _resolve_y(self, boxes, direction, limits, prev_y):
        """Undo vertical penetration only -- never touches x.

        As with _resolve_x, only surfaces the body crossed this step count.
        Landing on the nearest top of *every* overlapping box would snap a
        crushed body up onto the very ceiling that is crushing it.
        """
        if direction > 0.0:
            prev_bottom = prev_y + self.h
            overlapping = self._blockers(boxes)
            tops = [box[1] for box in overlapping if box[1] >= prev_bottom - SKIN]
            if tops:
                self._land(min(tops))
            elif overlapping:
                # Already buried in something and still heading into it, which
                # only happens to a squeezed body.  Stay put rather than sink.
                self.y = prev_y
                self.vel_y = 0.0
            if self._blockers(boxes):
                # A ceiling is closer than the body is tall.  The feet stay on
                # the floor; the caller decides what a squeeze means.
                self.squeezed = True

        elif direction < 0.0:
            overlapping = self._blockers(boxes)
            hits = [box for box in overlapping if box[3] <= prev_y + SKIN]
            if not hits and overlapping:
                # Same story upward: a squeezed body must not climb further
                # into the ceiling it is already inside.
                self.y = prev_y
                self.vel_y = self.head_bump_speed
                self.hit_head = True
                self.squeezed = True
            elif hits and not self._corner_correct(boxes, hits, limits):
                self.y = max(box[3] for box in hits)
                self.vel_y = self.head_bump_speed
                self.hit_head = True
                # Bumped into a gap shorter than the body: the floor wins.
                remaining = self._blockers(boxes)
                floors = [box[1] for box in remaining if box[1] >= self.centery]
                if floors:
                    self._land(min(floors))
                if remaining:
                    self.squeezed = True

        if limits is not None:
            if self.y + self.h > limits[3]:
                self._land(limits[3])
            elif self.y < limits[1]:
                self.y = limits[1]
                if self.vel_y < 0.0:
                    self.vel_y = self.head_bump_speed
                    self.hit_head = True

    def _land(self, surface_top):
        self.y = surface_top - self.h
        if self.vel_y > 0.0:
            self.vel_y = 0.0
        self.on_ground = True

    def _corner_correct(self, boxes, hits, limits):
        """Slip a rising body around a platform corner it barely clipped.

        Returns True if the body was moved aside and the jump may continue.
        """
        if self.corner_correction <= 0.0:
            return False

        start_x = self.x
        to_the_right = max(box[2] for box in hits) - self.x
        to_the_left = (self.x + self.w) - min(box[0] for box in hits)

        for shift in sorted((to_the_right, -to_the_left), key=abs):
            if not 0.0 < abs(shift) <= self.corner_correction:
                continue
            self.x = start_x + shift
            blocked = bool(self._blockers(boxes))
            if limits is not None:
                blocked = blocked or self.x < limits[0] or self.x + self.w > limits[2]
            if not blocked:
                return True
            self.x = start_x
        return False

    def _push_out(self, way, box):
        left, top, right, bottom = box
        if way == "up":
            self._land(top)
        elif way == "down":
            self.y = bottom
            if self.vel_y < 0.0:
                self.vel_y = self.head_bump_speed
                self.hit_head = True
        elif way == "left":
            self.x = left - self.w
            self.vel_x = min(self.vel_x, 0.0)
        else:
            self.x = right
            self.vel_x = max(self.vel_x, 0.0)

    def _depenetrate(self, boxes, limits):
        """Push an already-overlapping body back out.

        A body should never be overlapping at the start of a frame, but it
        happens: a moving platform slid into it, it was resized, it was
        teleported, or it was placed inside the level to begin with.  Clearing
        it here means the axis passes always start from a clean state.
        """
        for _ in range(4):
            hits = self._blockers(boxes)
            if not hits:
                break

            box = min(hits, key=lambda b: min(
                (self.x + self.w) - b[0], b[2] - self.x,
                (self.y + self.h) - b[1], b[3] - self.y,
            ))
            left, top, right, bottom = box

            # Already standing on something else means this box is pressing
            # into the body rather than being something to stand on, so riding
            # up on top of it -- surfing a descending crusher -- is not offered.
            may_stand = not self._has_support(boxes, limits, ignore=box)

            # A push longer than the body's own size along that axis is a
            # teleport, not a fix -- it would fling the body clean out of the
            # side of a full-width floor -- so each option is capped.
            options = [
                (bottom - self.y, "down", self.h),
                ((self.x + self.w) - left, "left", self.w),
                (right - self.x, "right", self.w),
            ]
            if may_stand:
                options.append(((self.y + self.h) - top, "up", self.h))
            pushes = sorted((o for o in options if o[0] <= o[2]), key=lambda o: o[0])

            before = (self.x, self.y, self.vel_x, self.vel_y,
                      self.on_ground, self.hit_head)
            for _, way, _cap in pushes:
                self._push_out(way, box)
                if not self._blockers(boxes):
                    break
                (self.x, self.y, self.vel_x, self.vel_y,
                 self.on_ground, self.hit_head) = before
            else:
                # Nothing frees the body, so it is genuinely wedged.  Put its
                # feet on the platform if that is allowed -- ground beats
                # ceiling -- and otherwise leave it exactly where it is rather
                # than let it jitter between two platforms every frame.
                self.squeezed = True
                if may_stand:
                    self._land(top)
                break
        else:
            if self._blockers(boxes):
                self.squeezed = True

        if limits is not None:
            self.x = min(max(self.x, limits[0]), max(limits[0], limits[2] - self.w))
            self.y = min(max(self.y, limits[1]), max(limits[1], limits[3] - self.h))
