from py5 import *

def settings():
    size(500, 500)

def setup():
    global playerX, playerY, keys, turtleImage, jiillyFissh
    playerX = 50
    playerY = 250
    keys = set()
    frame_rate(60)
    turtleImage = load_image('assets/turtle.png')
    jiillyFissh = load_image('assets/jellyfish.png')

def draw():
    global playerX, playerY, turtleImage, jiillyFissh

    # player movement
    if 'w' in keys and playerY >= 0:
        playerY -= 10
    if 's' in keys and playerY <= 500:
        playerY += 10
    if 'a' in keys and playerX >= 0:
        playerX -= 10   
    if 'd' in keys and playerX <= 500:
        playerX += 10
        
    # draw stuff here under background
    background(255, 255, 255)
    image(turtleImage, playerX, playerY, 75, 75)
    image(jiillyFissh, 100, 0, 400, 300)
    
    
    
def key_pressed(e):
    keys.add(e.get_key())

def key_released(e):
    keys.discard(e.get_key())

run_sketch()