# Example file showing a circle moving on screen
import pygame
import math

from blasterBullet import Bullet

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

TANK_SPEED = 300
ROTATION_SPEED = 200
RADIUS = 40

background = pygame.image.load("assets/flappyBackground.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

tank1_pos = pygame.Vector2(WIDTH / 4, HEIGHT / 4)
tank1_angle = 0

tank2_pos = pygame.Vector2(WIDTH - WIDTH / 4, HEIGHT - HEIGHT / 4)
tank2_angle = 0

bulletList = []

SHOOT_COOLDOWN = 0.5  # seconds between shots
tank1_last_shot = 0
tank2_last_shot = 0

tank1health = 3
tank2health = 3

gameState = "menu"

while running == True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if gameState == "menu":
        pygame.draw.rect(screen, "Red", (WIDTH//2 - 50, HEIGHT//2 - 25, 100, 50))
        screen.fill("black")
            

    if gameState == "playing":
        # fill the screen with a color to wipe away anything from last frame
        screen.blit(background, (0, 0))

        # Draw tank 1 (red) - body circle + barrel line
        pygame.draw.circle(screen, "red", tank1_pos, 40)
        barrel1_end = tank1_pos + pygame.Vector2(60, 0).rotate(-tank1_angle)
        pygame.draw.line(screen, "black", tank1_pos, barrel1_end, 10)
        pygame.draw.rect(screen, "red", (tank1_pos.x-40, tank1_pos.y-55, 80, 10))
        pygame.draw.rect(screen, "green", (tank1_pos.x-40, tank1_pos.y-55, 80/3 * tank1health, 10))

        # Draw tank 2 (blue) - body circle + barrel line
        pygame.draw.circle(screen, "blue", tank2_pos, 40)
        barrel2_end = tank2_pos + pygame.Vector2(60, 0).rotate(-tank2_angle)
        pygame.draw.line(screen, "black", tank2_pos, barrel2_end, 10)
        pygame.draw.rect(screen, "red", (tank2_pos.x-40, tank2_pos.y-55, 80, 10))
        pygame.draw.rect(screen, "green", (tank2_pos.x-40, tank2_pos.y-55, 80/3 * tank2health, 10))
        

        for bullet in bulletList:
            bullet.update(dt)
            bullet.draw(screen)
            

            if bullet.pos.x < 0 or bullet.pos.x > WIDTH:
                if bullet.bounces >= 2:
                    bulletList.remove(bullet)
                    continue
                bullet.direction.x *= -1
                bullet.bounces += 1
            if bullet in bulletList and (bullet.pos.y < 0 or bullet.pos.y > HEIGHT):
                if bullet.bounces >= 2:
                    bulletList.remove(bullet)
                    continue
                bullet.direction.y *= -1
                bullet.bounces += 1

                
            if bullet.collidepoint(tank1_pos) and bullet in bulletList:
                print("Tank 1 hit!")
                bulletList.remove(bullet)
                tank1health -= 1
                
            if bullet.collidepoint(tank2_pos) and bullet in bulletList:
                print("Tank 2 hit!")
                bulletList.remove(bullet)
                tank2health -= 1
                
        if tank1health <= 0:
            screen.fill("Red")
            running = False

            
        if tank2health <= 0:
            screen.fill("Blue")
            running = False

            
            

        keys = pygame.key.get_pressed()
        # Tank 1: A/D rotate, W/S move forward/backward, E shoot
        if keys[pygame.K_a]:
            tank1_angle += ROTATION_SPEED * dt
        if keys[pygame.K_d]:
            tank1_angle -= ROTATION_SPEED * dt
        if keys[pygame.K_w]:
            direction = pygame.Vector2(1, 0).rotate(-tank1_angle)
            tank1_pos += direction * TANK_SPEED * dt
        if keys[pygame.K_s]:
            direction = pygame.Vector2(1, 0).rotate(-tank1_angle)
            tank1_pos -= direction * TANK_SPEED * dt
        tank1_pos.x = pygame.math.clamp(tank1_pos.x, RADIUS, WIDTH - RADIUS)
        tank1_pos.y = pygame.math.clamp(tank1_pos.y, RADIUS, HEIGHT - RADIUS)

        current_time = pygame.time.get_ticks() / 1000
        if keys[pygame.K_e] and current_time - tank1_last_shot >= SHOOT_COOLDOWN:
            barrel1_dir = pygame.Vector2(60, 0).rotate(-tank1_angle)
            newBullet = Bullet(tank1_pos + barrel1_dir, tank1_pos + barrel1_dir * 2)
            bulletList.append(newBullet)
            tank1_last_shot = current_time

        # Tank 2: J/L rotate, I/K move forward/backward, O shoot
        if keys[pygame.K_j]:
            tank2_angle += ROTATION_SPEED * dt
        if keys[pygame.K_l]:
            tank2_angle -= ROTATION_SPEED * dt
        if keys[pygame.K_i]:
            direction = pygame.Vector2(1, 0).rotate(-tank2_angle)
            tank2_pos += direction * TANK_SPEED * dt
        if keys[pygame.K_k]:
            direction = pygame.Vector2(1, 0).rotate(-tank2_angle)
            tank2_pos -= direction * TANK_SPEED * dt
        tank2_pos.x = pygame.math.clamp(tank2_pos.x, RADIUS, WIDTH - RADIUS)
        tank2_pos.y = pygame.math.clamp(tank2_pos.y, RADIUS, HEIGHT - RADIUS)

        if keys[pygame.K_o] and current_time - tank2_last_shot >= SHOOT_COOLDOWN:
            barrel2_dir = pygame.Vector2(60, 0).rotate(-tank2_angle)
            newBullet = Bullet(tank2_pos + barrel2_dir, tank2_pos + barrel2_dir * 2)
            bulletList.append(newBullet)
            tank2_last_shot = current_time
            
        

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

# end loop

pygame.time.delay(2000)  
pygame.quit()