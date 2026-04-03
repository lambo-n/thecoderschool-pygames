# Example file showing a circle moving on screen
import pygame
import random
from bullet import *
from blasterEnemy import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
money = 0
wave = 1
# 1, 2, 4, 7, 11, 16
waveAmount = 0
enemiesLeft = waveAmount

             
             


WIDTH = screen.get_width()
HEIGHT = screen.get_height()

player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)

playerImage = pygame.image.load("assets/cowboyReady.png").convert_alpha()
playerImage = pygame.transform.scale(playerImage, (80, 80))

bulletList = []
enemyList = []


health = 100

canJump = False
gameState = "playing"

font = pygame.font.SysFont(None, 40)
font_small = pygame.font.SysFont(None, 28)
font_large = pygame.font.SysFont(None, 64)

# Shop card layout
CARD_W, CARD_H = 240, 320
CARD_Y = HEIGHT // 2 - CARD_H // 2
card_gap = 60
total_w = 3 * CARD_W + 2 * card_gap
card_start_x = WIDTH // 2 - total_w // 2

upgrade_rects = [
    pygame.Rect(card_start_x + i * (CARD_W + card_gap), CARD_Y, CARD_W, CARD_H)
    for i in range(3)
]

start_btn = pygame.Rect(WIDTH // 2 - 110, CARD_Y + CARD_H + 40, 220, 52)

while running == True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gameState == "shop":
                mx, my = pygame.mouse.get_pos()
                for i, rect in enumerate(upgrade_rects):
                    if rect.collidepoint(mx, my):
                        print(f"Upgrade {i + 1} clicked")
                if start_btn.collidepoint(mx, my):
                    gameState = "playing"
            elif gameState == "playing":
                mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
                copyPos = player_pos.copy()
                bulletList.append(Bullet((copyPos.x + 40, copyPos.y + 40), mouse_pos))

    if gameState == "shop":
        screen.fill((20, 20, 35))

        # Title
        title_surf = font_large.render("S H O P", True, (220, 200, 120))
        screen.blit(title_surf, (WIDTH // 2 - title_surf.get_width() // 2, 60))

        # Money display
        money_surf = font.render(f"$ {money}", True, (100, 220, 100))
        screen.blit(money_surf, (WIDTH // 2 - money_surf.get_width() // 2, 130))

        mx, my = pygame.mouse.get_pos()

        for i, rect in enumerate(upgrade_rects):
            hovered = rect.collidepoint(mx, my)
            card_color   = (50, 50, 80) if not hovered else (70, 70, 110)
            border_color = (120, 100, 200) if not hovered else (200, 170, 255)
            icon_color   = (180, 150, 255)

            # Card shadow
            shadow = pygame.Rect(rect.x + 6, rect.y + 6, rect.w, rect.h)
            pygame.draw.rect(screen, (10, 10, 20), shadow, border_radius=14)

            # Card body
            pygame.draw.rect(screen, card_color, rect, border_radius=14)
            pygame.draw.rect(screen, border_color, rect, width=2, border_radius=14)

            # Icon placeholder
            icon_rect = pygame.Rect(rect.x + CARD_W // 2 - 40, rect.y + 30, 80, 80)
            pygame.draw.rect(screen, (30, 30, 50), icon_rect, border_radius=10)
            pygame.draw.rect(screen, icon_color, icon_rect, width=2, border_radius=10)
            q_surf = font_large.render("?", True, icon_color)
            screen.blit(q_surf, (icon_rect.centerx - q_surf.get_width() // 2,
                                  icon_rect.centery - q_surf.get_height() // 2))

            # Upgrade name
            name_surf = font.render(f"Upgrade {i + 1}", True, (230, 230, 230))
            screen.blit(name_surf, (rect.centerx - name_surf.get_width() // 2, rect.y + 130))

            # Description placeholder
            for j, line in enumerate(["???", "???", "???"]):
                line_surf = font_small.render(line, True, (140, 140, 170))
                screen.blit(line_surf, (rect.centerx - line_surf.get_width() // 2,
                                        rect.y + 178 + j * 24))

            # Buy button at bottom of card
            buy_rect = pygame.Rect(rect.x + 30, rect.y + CARD_H - 60, CARD_W - 60, 40)
            buy_color = (80, 170, 80) if hovered else (50, 120, 50)
            pygame.draw.rect(screen, buy_color, buy_rect, border_radius=8)
            buy_surf = font_small.render("BUY", True, (220, 255, 220))
            screen.blit(buy_surf, (buy_rect.centerx - buy_surf.get_width() // 2,
                                    buy_rect.centery - buy_surf.get_height() // 2))

        # Start Wave button
        sw_color = (180, 130, 40) if not start_btn.collidepoint(mx, my) else (220, 170, 60)
        pygame.draw.rect(screen, sw_color, start_btn, border_radius=10)
        pygame.draw.rect(screen, (255, 210, 80), start_btn, width=2, border_radius=10)
        sw_surf = font.render("Start Wave", True, (255, 245, 200))
        screen.blit(sw_surf, (start_btn.centerx - sw_surf.get_width() // 2,
                               start_btn.centery - sw_surf.get_height() // 2))
        
        
        
    elif gameState == "playing":
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")  
        

        textHealth = font.render(str(health), True, (0, 0, 255))
        screen.blit(textHealth, (50, 600))
            

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and canJump:
            gravity = -600
            canJump = False
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
            
        screen.blit(playerImage, player_pos)
            
        
        if len(enemyList) == 0:
            waveAmount = 1 + (wave - 1) * wave // 2
            wave += 1
            enemiesLeft = waveAmount

            enemyTypes = {"normal": 2, "speed": 1}
            budget = waveAmount
            while budget > 0:
                affordable = [t for t, v in enemyTypes.items() if v <= budget]
                enemyType = random.choice(affordable)
                newEnemy = Enemy(pygame.Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)), enemyType)
                enemyList.append(newEnemy)
                budget -= enemyTypes[enemyType]
            
            gameState = "shop"
            
            
            
        for bullet in bulletList[:]:
            bullet.update(dt)
            bullet.draw(screen)
            if not (0 <= bullet.pos.x <= WIDTH and 0 <= bullet.pos.y <= HEIGHT):
                bulletList.remove(bullet)
                
            for enemy in enemyList[:]:
                enemyRect = enemy.get_rect()
                
                if enemyRect.collidepoint(bullet.pos) and bullet in bulletList:
                    enemy.health -= 5
                    bulletList.remove(bullet)
                    
                if enemy.health <= 0 and enemy:
                    money += enemy.value
                    enemiesLeft -= enemy.value
                    print(money)
                    print(enemiesLeft)
                    enemyList.remove(enemy)
                    
                
                
        for enemy in enemyList[:]:
            enemyRect = enemy.get_rect()
            
            if enemyRect.collidepoint(player_pos):
                health -= enemy.strength
                
            enemy.update(player_pos, dt)
            enemy.draw(screen)
            
            
        if health <= 0:
            running = False
        
  
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()