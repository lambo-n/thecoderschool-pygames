import pygame
import random
#want to do so dont get sea of green
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((300,400))
clock = pygame.time.Clock()

player = pygame.transform.scale(
        pygame.image.load("seal2.jpg"),
        (60,50)
    )
player_rect = player.get_rect()
pygame.display.set_caption("Jump")
pygame.display.set_icon(
    player
)
player_vy = 0

nenemy = pygame.transform.scale(
    pygame.image.load("TetoPlush.png"), (75, 75)
)
nenemy_rect = nenemy.get_rect()
nenemy_dir = 1

nenemy_rect.y = random.randint(-200, -100)

bounce = pygame.mixer.Sound("Sonic_boom1.ogg.mp3")
bounce.set_volume(0.5)
platforms = [
    pygame.Rect(0, 200, 50, 25),
    pygame.Rect(70, 300, 50, 25),
]

platforms += [
    pygame.rect.Rect(
        random.randint(0, 300),
        random.randint(0,450),
        50, 25
    )
    for _ in range(10)
]

platforms += [
    pygame.rect.Rect(
        random.randint(0, 300),
        random.randint(0,450),
        50, 25
    )
    for _ in range(5)
]

def spawn_platforms():
    n = 1
    for i in range(n):
        platforms.append(
            pygame.Rect(
                random.randint(0, 300),
                -300 + i * 100,
                50, 25,
            )
            
        )


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((60,90,130))

    for platform in platforms:
        pygame.draw.rect(screen, (100, 200, 120), platform)

        if player_vy < 0 and player_rect.centery < 150:
            platform.y += -player_vy
            # if player_rect.colliderect(platform):
            #     platforms.remove(platform)
            # else:
            # if clock.tick > 60: #yeah not work=\\\\woudl this method work, cna I change clock.tick, but do I want to use framerate
            if platform.top >= 400:
                # spawn_platforms()
                r= random.randint(0,4)
                if r == 0:
                    platforms.remove(platform)
                else:
                    platform.top = 0 # maybe change.top to another part
                
                # platforms.remove(platform)
            if player_rect.colliderect(platform):
                break
                
                





        if player_rect.colliderect(platform):
            player_vy = -5
            bounce.play()     


    screen.blit(player, player_rect)
    screen.blit(nenemy, nenemy_rect)

    if player_vy < 0 and player_rect.centery <150:
        nenemy_rect.y += -player_vy
        if nenemy_rect.top >= 400:
            nenemy_rect.y = random.randint(-500, -400)


    nenemy_rect.x += nenemy_dir *5
    if nenemy_rect.right >= 300:
        nenemy_dir = -1
    elif nenemy_rect.left <= 0:
        nenemy_dir = 1

    player_vy += 0.2
    player_rect.y += player_vy

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect.x -= 3
    if keys[pygame.K_d]:
        player_rect.x -= -3
    clock.tick(60)
    pygame.display.flip()