# Example file showing a circle moving on screen
import random
import math 

import pygame
from ethanBullet import *
from enemy import Enemy

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720), )
clock = pygame.time.Clock()
running = True
dt = 0
money = 99999999999999999
wave = 1
waveAmount = 0
enemiesLeft = waveAmount

damage = 5
health = 100
speed = 300

speedUpgradecost = 100
damageUpgradecost = 200
healthUpgradecost = 500

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


blasterBoyImage = pygame.image.load("assets/blasterboy.png").convert_alpha()


bulletlist = []
enemylist = []








gameState = "shop"
waveOver = True




font = pygame.font.SysFont(None,40)

damageButtonRect = pygame.Rect(WIDTH/2-75, HEIGHT/2 - 150,150,150)
healthButtonRect = pygame.Rect(WIDTH/2+150, HEIGHT/2 - 150,150,150)
speedButtonRect = pygame.Rect(WIDTH/2-300, HEIGHT/2 - 150,150,150)
startWaveButton = pygame.Rect(WIDTH/2-150, 600,150,75)

# draw game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gameState == "playing":
                mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
                bulletlist.append(Bullet(player_pos.copy(), mouse_pos))
            elif gameState == "shop":
                mx, my = pygame.mouse.get_pos()
                if startWaveButton.collidepoint(mx,my):
                    gameState = "playing"
                if healthButtonRect.collidepoint(mx,my):
                    if money >= healthUpgradecost:
                        health = math.ceil(health * 1.5)
                        money -= healthUpgradecost
                        healthUpgradecost = math.ceil(healthUpgradecost * 1.5)
                if speedButtonRect.collidepoint(mx,my):
                    if money >= speedUpgradecost:
                        speed = math.ceil(speed * 1.2)
                        money -= speedUpgradecost
                        speedUpgradecost = math.ceil(speedUpgradecost * 1.5)
                if damageButtonRect.collidepoint(mx,my):
                    if money >= damageUpgradecost:
                        damage = math.ceil(damage * 1.5)
                        money -= damageUpgradecost
                        damageUpgradecost = math.ceil(damageUpgradecost * 1.5)

            



    if gameState == "shop":
        screen.fill("black")

        # (xPos, yPos, xWidth, yHeight)
        pygame.draw.rect(screen,"white", damageButtonRect)#damage
        #bottemleft(x = width/2-150,y = height/2-225)
        #topright(x=width/2-0, y = height/2-75)
        pygame.draw.rect(screen,"white",speedButtonRect)#speed
        #bottomleft(x = width/2+150-75,y = height/2 - 150 - 75)
        #topright(x = width/2+150+75,y = height/2 -150 +75)
        pygame.draw.rect(screen,"white",healthButtonRect)#health
        #bottomleft(x = width/2 - 300 - 75, y= height/2 - 150 - 75)
        #topright(x = width/2 - 300 + 75,y = height/ - 150 + 75)
        pygame.draw.rect(screen,"white",startWaveButton)#start
        #bottomleft(x = width/2 - 150 + 75 )
        #topright


        startwavetext1 = font.render("start",True,"green")
        startwavetext2 = font.render("wave",True,"green")
        startwavetext1_rect = startwavetext1.get_rect(center = (560,625))
        startwavetext2_rect = startwavetext2.get_rect(center = (560,650))
        screen.blit(startwavetext1,startwavetext1_rect)
        screen.blit(startwavetext2,startwavetext2_rect)
        




        formattedMoney = "$" + str(money)
        Moneytext = font.render(formattedMoney,True,"green")
        Moneytext_rect = Moneytext.get_rect(center = (100,640))
        screen.blit(Moneytext,Moneytext_rect)







        damageUpgradeText1 = font.render("damage", True, "black")
        damageUpgradeText2 = font.render("upgrade", True, "black")
        damageUpgradeText3 = font.render(str(damageUpgradecost), True, "black")
        damageUpgadetext1_rect = damageUpgradeText1.get_rect(center=(WIDTH/2, HEIGHT/2 - 125))
        damageUpgradetext2_rect = damageUpgradeText2.get_rect(center=(WIDTH/2, HEIGHT/2 - 100))
        damageUpgradetext3_rect = damageUpgradeText3.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
        screen.blit(damageUpgradeText1,damageUpgadetext1_rect)
        screen.blit(damageUpgradeText2,damageUpgradetext2_rect)
        screen.blit(damageUpgradeText3,damageUpgradetext3_rect)



        speedUpgradeText1 = font.render("speed", True, "black")
        speedUpgradeText2 = font.render("upgrade", True, "black")
        speedUpgradeText3 = font.render(str(speedUpgradecost), True, "black")
        speedUpgradetext1_rect = speedUpgradeText1.get_rect(center=(WIDTH/3-10, HEIGHT/2 - 125))
        speedUpgradetext2_rect = speedUpgradeText2.get_rect(center=(WIDTH/3-10, HEIGHT/2 - 100))
        speedUpgradetext3_rect = speedUpgradeText3.get_rect(center=(WIDTH/3-10, HEIGHT/2 - 50))
        screen.blit(speedUpgradeText1,speedUpgradetext1_rect)
        screen.blit(speedUpgradeText2,speedUpgradetext2_rect)
        screen.blit(speedUpgradeText3,speedUpgradetext3_rect)




        healthUpgradeText1 = font.render("health", True, "black")
        healthUpgradeText2 = font.render("upgrade", True, "black")
        healthUpgradeText3 = font.render(str(healthUpgradecost), True, "black")
        healthUpgradetext1_rect = healthUpgradeText1.get_rect(center=(WIDTH/1.5+10, HEIGHT/2 - 125))
        healthUpgradetext2_rect = healthUpgradeText2.get_rect(center=(WIDTH/1.5+10, HEIGHT/2 - 100))
        healthUpgradetext3_rect = healthUpgradeText2.get_rect(center=(WIDTH/1.5+50, HEIGHT/2 - 50))
        screen.blit(healthUpgradeText1,healthUpgradetext1_rect)
        screen.blit(healthUpgradeText2,healthUpgradetext2_rect)
        screen.blit(healthUpgradeText3,healthUpgradetext3_rect)

    elif gameState == "playing":
       # fill the screen width a color to wipe away anything from last frame
        screen.fill("purple")

    
        
        pygame.draw.rect(screen,"white",(WIDTH/2-150, HEIGHT/2 - 100,300,200))
        blasterBoyRect = blasterBoyImage.get_rect(center = player_pos)
        screen.blit(blasterBoyImage, blasterBoyRect)

        textHealth = font.render(str(health), True, (255,255,255))
        screen.blit(textHealth,(50,600))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= speed * dt
        if keys[pygame.K_s]:
            player_pos.y += speed * dt
        if keys[pygame.K_a]:
            player_pos.x -= speed * dt
        if keys[pygame.K_d]:
            player_pos.x += speed * dt



        if len(enemylist) == 0:
            if waveOver == False:
                gameState = "shop"
                waveOver = True

            elif waveOver == True:
                waveOver = False
                waveAmount += 1 + (wave - 1)*wave//2
                wave += 1
                enemiesLeft = waveAmount

                enemyTypes = {"normal":2, "speed":1, "strong":1}
                budget = waveAmount
                
                while budget > 0:
                    affordable = [t for t ,v in enemyTypes.items() if v <= budget]
                    enemyType = random.choice(affordable)
                    newEnemy = Enemy(pygame.Vector2(random.randint(0,WIDTH), random.randint(0,HEIGHT)), enemyType)
                    enemylist.append(newEnemy)
                    budget -= enemyTypes[enemyType]


        for bullet in bulletlist[:]:
            bullet.update(dt)
            bullet.draw(screen)
            if not (0 <= bullet.pos.x <= WIDTH and 0 <= bullet.pos.y <= HEIGHT):
                bulletlist.remove(bullet) 

            for enemy in enemylist[:]:
                enemyRect = enemy.get_rect()

                if enemyRect.collidepoint(bullet.pos) and bullet in bulletlist:
                    enemy.health -= damage
                    bulletlist.remove(bullet)


                if enemy.health <= 0 and enemy:
                    money += enemy.value
                    enemiesLeft -= enemy.value
                    print(money)
                    enemylist.remove(enemy)    


        for enemy in enemylist[:]:
            enemyRect = enemy.get_rect()
            if enemyRect.collidepoint(player_pos):
                health -= enemy.strength
            enemy.update(player_pos, dt)
            enemy.draw(screen)   



        if health <= 0:
            running = False            

    player_rect = blasterBoyImage.get_rect()
    player_rect.clamp_ip(screen.get_rect())

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
