import pygame
import random
#want to do so dont get sea of green
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((300,400))
clock = pygame.time.Clock()
running = True

font = pygame.font.SysFont("Verdana", 40)

player = pygame.transform.scale(
        pygame.image.load("assets/jumpboy.png"),
        (60,50)
    )
player_rect = player.get_rect(midbottom=(150, 370))  # start standing on the bottom platform
pygame.display.set_caption("Jump")
pygame.display.set_icon(
    player
)
player_vy = 0

nenemy = pygame.transform.scale(
    pygame.image.load("assets/pacboy.png"), (75, 75)
)
nenemy_rect = nenemy.get_rect()
nenemy_dir = 1

nenemy_rect.y = random.randint(-200, -100)

# bounce = pygame.mixer.Sound("Sonic_boom1.ogg.mp3")
# bounce.set_volume(0.5)
platforms = [
    pygame.Rect(125, 370, 50, 25),  # starting platform under the player
    pygame.Rect(0, 300, 50, 25),
    pygame.Rect(70, 320, 50, 25),
]
 
# all bellow can be gone to fix generation(can do 50/50 per set distance, or 1/3 chance for 3 set distances)
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


while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((60,90,130))
    print(player_vy)

    player_vy += 0.2
    player_rect.y += player_vy

    # if the player goes above the middle, push everything down so they stay in the middle
    if player_rect.centery < 200:
        shift = 200 - player_rect.centery
        player_rect.centery = 200
        for platform in platforms[:]:  # copy so removing doesn't skip platforms
            platform.y += shift
            if platform.top >= 400:
                platforms.remove(platform)
        nenemy_rect.y += shift
        if nenemy_rect.top >= 400:
            nenemy_rect.y = random.randint(-500, -400)

    # only spawn once the highest platform has scrolled into view, so spacing stays even
    highest = min(p.top for p in platforms)
    if highest > 0:
        gap = random.choice([20, 40, 55])  # jump reaches ~62px, keep gaps below that
        platforms.append(pygame.Rect(random.randint(0, 250), highest - gap, 50, 25))
    for platform in platforms:
        pygame.draw.rect(screen, (100, 200, 120), platform)

        # only bounce when falling onto a platform, not when passing up through it
        if player_vy > 0 and player_rect.colliderect(platform):
            player_vy = -5
            print("bottom" + str(player_rect.bottom))
            # bounce.play()     

    if player_vy > -0.1 and player_vy < 0.1:
        print("top" + str(player_rect.bottom))


    nenemy_rect.x += nenemy_dir *5
    if nenemy_rect.right >= 300:
        nenemy_dir = -1
    elif nenemy_rect.left <= 0:
        nenemy_dir = 1

    # if player_rect.colliderect(nenemy_rect) and nenemy_rect.bottom > 40: #careful & =! and
    #     screen.fill((0, 0, 0))
    #     text_surface = font.render("You lose...", True, "white")
    #     text_rect = text_surface.get_rect(center=(150, 200))
    #     screen.blit(text_surface, text_rect)
    #     running = False
    # if player_rect.centery > 500: #makes so if fall off screen, you lose
    #     screen.fill((0, 0, 0))
    #     text_surface = font.render("You lose...", True, "white")
    #     text_rect = text_surface.get_rect(center=(150, 200))
    #     screen.blit(text_surface, text_rect)
    #     running = False

    


    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect.x -= 3
    if keys[pygame.K_d]:
        player_rect.x -= -3
    
    screen.blit(player, player_rect)
    screen.blit(nenemy, nenemy_rect)
    clock.tick(60)
    pygame.display.flip()
    
    
pygame.time.wait(5000)
pygame.quit()
