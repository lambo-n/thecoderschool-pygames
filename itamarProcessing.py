from py5 import *

SPEED = 5
SIZE = 50

def settings():
    size(500, 500)

def setup():
    global playerX, playerY, keys
    playerX = 50
    playerY = 250
    keys = set()
    frame_rate(60)

def draw():
    global playerX, playerY

    background(255, 255, 255)

    # Continuous movement: apply held keys every frame for smooth motion
    if 'w' in keys:
        playerY -= SPEED
    if 's' in keys:
        playerY += SPEED
    if 'a' in keys:
        playerX -= SPEED
    if 'd' in keys:
        playerX += SPEED

    # Keep the player inside the window
    playerX = constrain(playerX, 0, 500 - SIZE)
    playerY = constrain(playerY, 0, 500 - SIZE)

    fill(255, 100, 155)
    rect(playerX, playerY, SIZE, SIZE)

def key_pressed(e):
    keys.add(e.get_key())

def key_released(e):
    keys.discard(e.get_key())

run_sketch()