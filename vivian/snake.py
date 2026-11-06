import random
from pathlib import Path

import pygame


WIDTH = 400
HEIGHT = 400
FPS = 60
TILE = 20
FOOD_COUNT = 10
PLAYER_RADIUS = 24
PLAYER_SPEED = 300
MOVE_EVERY = 0.6


BACKGROUND = (22, 27, 34)
PLAYER_COLOR = (83, 220, 190)
ASSETS = Path(__file__).parent / "assets"
FRUIT_FILES = ("Avocado.png", "Pomegranate .png", "coconut.png", "pineapple.png")


def load_fruit_images():
    images = []
    for name in FRUIT_FILES:
        image = pygame.image.load(ASSETS / name).convert_alpha()
        images.append(pygame.transform.smoothscale(image, (TILE, TILE)))
    return images     
 
 
def spawn_food(board, empty, food, fruit_images):
    empty_cells = [
        (r, c)
        for r in range(len(board))
        for c in range(len(board[0]))
        if board[r][c] == empty
    ]
    if not empty_cells:
        return None
    r, c = random.choice(empty_cells)
    board[r][c] = food
    return (r, c), random.choice(fruit_images)



def rotate_head(image, direction):
    # pygame.transform.rotate turns the picture counterclockwise.
    # Your head image already faces left, so left needs 0 degrees.
    if direction == (-1, 0):  # up
        return pygame.transform.rotate(image, 270)
    if direction == (1, 0):  # down
        return pygame.transform.rotate(image, 90)
    if direction == (0, 1):  # right
        return pygame.transform.rotate(image, 180)
    return image  # left


def rotate_tail(image, tail_direction):
    # Tail sprite points right (tip on the right, body on the left).
    if tail_direction == (-1, 0):  # up
        return pygame.transform.rotate(image, 90)
    if tail_direction == (1, 0):  # down
        return pygame.transform.rotate(image, 270)
    if tail_direction == (0, -1):  # left
        return pygame.transform.rotate(image, 180)
    return image  # right


def rotate_body(image, prev_pos, next_pos):
    # Body sprite is already horizontal. Rotate 90 if this piece is vertical.
    prev_row, prev_col = prev_pos
    next_row, next_col = next_pos
    if prev_col == next_col:
        return pygame.transform.rotate(image, 90)
    return image


def fill_food(board, empty, food, fruit_images, food_sprites, count=FOOD_COUNT):
    while len(food_sprites) < count:
        spawned = spawn_food(board, empty, food, fruit_images)
        if spawned is None:
            break
        pos, image = spawned
        food_sprites[pos] = image


def move_snake(snake_body, direction, board, empty, snake, food, food_sprites, fruit_images):
    global running
    head_row, head_col = snake_body[0]
    d_row, d_col = direction
    new_head_x = head_row + d_row
    new_head_y = head_col + d_col

    for i in range(1, len(snake_body)-1):
        if snake_body[0]== snake_body[i]:
            running = False
            return snake_body
            
    if new_head_x < 0 or new_head_x >= 20:
        running = False
        return snake_body
    if new_head_y < 0 or new_head_y >= 20:
        running = False
        return snake_body

    new_head = (new_head_x, new_head_y)
    ate_food = board[new_head_x][new_head_y] == food

    snake_body.insert(0, new_head)
    board[new_head_x][new_head_y] = snake

    if ate_food:
        food_sprites.pop(new_head, None)
        fill_food(board, empty, food, fruit_images, food_sprites)
    else:
        tail_row, tail_col = snake_body.pop()
        board[tail_row][tail_col] = empty
    return snake_body


def main():
    global running
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=0)
    pygame.display.set_caption("WASD Circle")
    clock = pygame.time.Clock()

    snake_head_image = pygame.image.load(ASSETS / "head-removebg-preview.png").convert_alpha()
    snake_head_image = pygame.transform.smoothscale(snake_head_image, (TILE, TILE))
    snake_body_image = pygame.image.load(ASSETS / "body-removebg-preview.png").convert_alpha()
    snake_body_image = pygame.transform.smoothscale(snake_body_image, (TILE, TILE))
    snake_tail_image = pygame.image.load(ASSETS / "tail-removebg-preview.png").convert_alpha()
    snake_tail_image = pygame.transform.smoothscale(snake_tail_image, (TILE, TILE))
    corner_top_left = pygame.image.load(ASSETS / "top-left-removebg-preview.png").convert_alpha()
    corner_top_left = pygame.transform.smoothscale(snake_head_image, (TILE, TILE))
    corner_top_right = pygame.image.load(ASSETS / "top-right-removebg-preview.png").convert_alpha()
    corner_top_right = pygame.transform.smoothscale(snake_head_image, (TILE, TILE))
    corner_bottom_left = pygame.image.load(ASSETS / "bottom-left-removebg-preview.png").convert_alpha()
    corner_bottom_left = pygame.transform.smoothscale(snake_head_image, (TILE, TILE))
    corner_bottom_right = pygame.image.load(ASSETS / "bottom-right-removebg-preview.png").convert_alpha()
    corner_bottom_right = pygame.transform.smoothscale(snake_head_image, (TILE, TILE))

    running = True

    empty = 0
    snake = 1
    food = 2
    snake_body = [(9, 9), (10, 9), (11, 9)]  # head, body, tail
    direction = (-1, 0)  # start moving up
    move_timer = 0

    fruit_images = load_fruit_images()
    board = [[0] * 20 for _ in range(20)]
    for row, col in snake_body:
        board[row][col] = snake
    food_sprites = {}
    fill_food(board, empty, food, fruit_images, food_sprites)

    while running:
        delta_time = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and direction != (1, 0):
            direction = (-1, 0)
        elif keys[pygame.K_s] and direction != (-1, 0):
            direction = (1, 0)
        elif keys[pygame.K_a] and direction != (0, 1):
            direction = (0, -1)
        elif keys[pygame.K_d] and direction != (0, -1):
            direction = (0, 1)

        move_timer += delta_time
        if move_timer >= MOVE_EVERY:
            move_timer = 0
            snake_body = move_snake(
                snake_body, direction, board, empty, snake, food, food_sprites, fruit_images
            )

        



        # draw stuff here
        screen.fill(BACKGROUND)

        # columns
        for c in range(20):
            yCoord = c * 20
            # rows
            for r in range(20):
                xCoord = r * 20

                o = r
                if c % 2 == 0:
                    o += 1

                if o % 2 == 0:
                    color = (190, 180, 230)
                else:
                    color = (171, 161, 214)

                pygame.draw.rect(screen, color, (xCoord, yCoord, TILE, TILE))
                fruit = food_sprites.get((c, r))
                if fruit is not None:
                    screen.blit(fruit, (xCoord, yCoord))
                
                if (c, r) in snake_body:
                    if (c, r) == snake_body[0]:
                        head = rotate_head(snake_head_image, direction)
                        screen.blit(head, (xCoord, yCoord))
                    elif (c, r) == snake_body[-1]:
                        prev_row, prev_col = snake_body[-2]
                        tail_row, tail_col = snake_body[-1]
                        tail_direction = (tail_row - prev_row, tail_col - prev_col)
                        tail = rotate_tail(snake_tail_image, tail_direction)
                        screen.blit(tail, (xCoord, yCoord))
                    else:
                        i = snake_body.index((c, r))
                        prev = snake_body[i - 1]
                        curr = snake_body[i]
                        nxt = snake_body[i + 1]
                        to_prev = (prev[0] - curr[0], prev[1] - curr[1])
                        to_next = (nxt[0] - curr[0], nxt[1] - curr[1])
                        sides = {to_prev, to_next}
                        if sides == { (0, -1), (1, 0) }:   # left + down
                            corner_image = corner_top_left
                        elif sides == { (0, 1), (1, 0) }:  # right + down
                            corner_image = corner_top_right
                        elif sides == { (0, -1), (-1, 0) }:  # left + up
                            corner_image = corner_bottom_left
                        elif sides == { (0, 1), (-1, 0) }:   # right + up
                            corner_image = corner_bottom_right

                        if prev[0] == nxt[0] or prev[1] == nxt[1]:
                            piece = rotate_body(snake_body_image, prev, nxt)  # straight
                        else:
                            piece = corner_image(prev, (c, r), nxt)           # turn
                        screen.blit(piece, (xCoord, yCoord))

            


        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()