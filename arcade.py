import pygame
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

CELL = 20  # grid cell size in pixels
COLS = screen.get_width() // CELL
ROWS = screen.get_height() // CELL

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
enemy_pos = pygame.Vector2(100, 100)
ENEMY_SPEED = 150

def world_to_grid(pos):
    return int(pos.x // CELL), int(pos.y // CELL)

def grid_to_world_center(gx, gy):
    return pygame.Vector2(gx * CELL + CELL / 2, gy * CELL + CELL / 2)

def find_next_waypoint(enemy, player):
    # Build a fresh walkable grid each frame (all open — no obstacles)
    matrix = [[1] * COLS for _ in range(ROWS)]
    grid = Grid(matrix=matrix)

    ex, ey = world_to_grid(enemy)
    px, py = world_to_grid(player)

    # Clamp to grid bounds
    ex = max(0, min(ex, COLS - 1))
    ey = max(0, min(ey, ROWS - 1))
    px = max(0, min(px, COLS - 1))
    py = max(0, min(py, ROWS - 1))

    if (ex, ey) == (px, py):
        return None  # already on same cell

    start = grid.node(ex, ey)
    end = grid.node(px, py)
    finder = AStarFinder()
    path, _ = finder.find_path(start, end, grid)

    if len(path) >= 2:
        next_node = path[1]
        return grid_to_world_center(next_node.x, next_node.y)
    return None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # --- Player movement ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # --- Enemy pathfinding ---
    waypoint = find_next_waypoint(enemy_pos, player_pos)
    if waypoint is not None:
        direction = waypoint - enemy_pos
        if direction.length() > 1:
            enemy_pos += direction.normalize() * ENEMY_SPEED * dt

    # --- Draw ---
    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.circle(screen, "blue", enemy_pos, 30)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
