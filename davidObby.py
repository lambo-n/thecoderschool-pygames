# Example file showing a circle moving on screen
import pygame
from davidPlatform import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
canJump = False

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
playerRect = pygame.Rect(player_pos.x - 32, player_pos.y - 32, 64,64)
playerHitbox = pygame.Rect(player_pos.x - 34, player_pos.y - 34, 67 ,67)


playerImage = pygame.image.load("assets/jumpboy.png").convert_alpha()
playerImage = pygame.transform.scale(playerImage, (64, 64))
gravity = 0

# lvl 1 platforms
platform1lvl1 = ObbyPlatform(0,650,1280,100,"blue")
platform2lvl1 = ObbyPlatform(50,500,300,50,"black")
platform3lvl1 = ObbyPlatform(200,325,300,50,"black")
platform4lvl1 = ObbyPlatform(500,200,300,50,"black")
escapeRect1 = Escape(1200,100,50,50,"gold", 100, 600)

lvl1List = [platform1lvl1,platform2lvl1,platform3lvl1,platform4lvl1,escapeRect1]

# lvl 2 platforms
platform1lvl2 = ObbyPlatform(0,650,1280,100,"blue")
platform2lvl2 = ObbyPlatform(400,400,1,1,"black")
platform3lvl2 = ObbyPlatform(200,600,1,1,"black")
platform4lvl2 = ObbyPlatform(700,200,1,1,"black")
escapeRect2 = Escape(900,100,50,50,"gold", 100, 600)




lvl2List = [platform1lvl2, platform2lvl2, platform3lvl2, platform4lvl2,escapeRect2]

# lvl 3 platforms
platform1Lvl3 = ObbyPlatform(40,670,100,230,"blue")
platform2Lvl3 = ObbyPlatform(500,700,30,20,"black")
platform3Lvl3 = ObbyPlatform(700,500,20,20,"black")
platform4Lvl3 = ObbyPlatform(400,300,1,1,"light grey")
platform5Lvl3 = ObbyPlatform(800,200,1,1,"light grey")
escapeRect3 = Escape(900,100,50,50,"gold", 500, 600)
killblock = Killblock(0,900,1280,100,"red")


lvl3List = [platform1Lvl3,platform2Lvl3,platform3Lvl3,platform4Lvl3,platform5Lvl3,escapeRect3,killblock]

#lvl 4 platforms

platform1lvl4 = ObbyPlatform(450,600,300,200,"blue")
platform2lvl4 = ObbyPlatform(450,100,10,900,"black")
platform3lvl4 = ObbyPlatform(900,100,10,900,"black")
teleportplatform1 = Teleporter(800,400,50,50,"red",1000,100)
escapeRect4 = Escape(1100,100,50,50,"gold", 500, 600)
killblock = Killblock(0,900,1280,100,"red")



lvl4List = [platform1lvl4,platform2lvl4,platform3lvl4,teleportplatform1,escapeRect4,killblock]


#lvl 5 platforms

platform1lvl5 = ObbyPlatform(0,650,1280,100,"blue")
platform2lvl5 = ObbyPlatform(850,170,10,10,"black")
killblock = Killblock(600,450,100,50,"red")
teleportplatform2 = Teleporter(150,600,20,20,"white",900,100)
escapeRect5 = Escape(1100,100,50,50,"gold", 700, 600)


lvl5List = [platform1lvl5,teleportplatform2,killblock,platform2lvl5,escapeRect5]


# lvl 6 platforms
platform1lvl6  = Killblock(0,900,1280,100,"red")
platform2lvl6  = ObbyPlatform(214, 91, 1, 2, "black")
platform3lvl6  = ObbyPlatform(347, 38, 1, 2, "black")
platform4lvl6  = ObbyPlatform(486, 112, 1, 2, "black")
platform5lvl6  = ObbyPlatform(619, 67, 1, 2, "black")
platform6lvl6  = ObbyPlatform(748, 129, 1, 2, "black")
platform7lvl6  = ObbyPlatform(886, 54, 1, 2, "black")
platform8lvl6  = ObbyPlatform(1017, 96, 1, 2, "black")
platform9lvl6  = ObbyPlatform(1164, 42, 1, 2, "black")

platform10lvl6 = ObbyPlatform(42, 184, 1, 2, "black")
platform11lvl6 = ObbyPlatform(171, 231, 1, 2, "black")
platform12lvl6 = ObbyPlatform(308, 167, 1, 2, "black")
platform13lvl6 = ObbyPlatform(449, 212, 1, 2, "black")
platform14lvl6 = ObbyPlatform(574, 181, 1, 2, "black")
platform15lvl6 = ObbyPlatform(693, 244, 1, 2, "black")
platform16lvl6 = ObbyPlatform(821, 193, 1, 2, "black")
platform17lvl6 = ObbyPlatform(954, 226, 1, 2, "black")
platform18lvl6 = ObbyPlatform(1093, 174, 1, 2, "black")
platform19lvl6 = ObbyPlatform(1237, 216, 1, 2, "black")

platform20lvl6 = ObbyPlatform(96, 322, 1, 2, "black")
platform21lvl6 = ObbyPlatform(238, 278, 1, 2, "black")
platform22lvl6 = ObbyPlatform(372, 341, 1, 2, "black")
platform23lvl6 = ObbyPlatform(513, 296, 1, 2, "black")
platform24lvl6 = ObbyPlatform(647, 354, 1, 2, "black")
platform25lvl6 = ObbyPlatform(771, 305, 1, 2, "black")
platform26lvl6 = ObbyPlatform(914, 349, 1, 2, "black")
platform27lvl6 = ObbyPlatform(1048, 289, 1, 2, "black")
platform28lvl6 = ObbyPlatform(1181, 337, 1, 2, "black")

platform29lvl6 = ObbyPlatform(28, 421, 1, 2, "black")
platform30lvl6 = ObbyPlatform(157, 389, 1, 2, "black")
platform31lvl6 = ObbyPlatform(291, 452, 1, 2, "black")
platform32lvl6 = ObbyPlatform(427, 405, 1, 2, "black")
platform33lvl6 = ObbyPlatform(558, 467, 1, 2, "black")
platform34lvl6 = ObbyPlatform(704, 416, 1, 2, "black")
platform35lvl6 = ObbyPlatform(843, 453, 1, 2, "black")
platform36lvl6 = ObbyPlatform(981, 397, 1, 2, "black")
platform37lvl6 = ObbyPlatform(1122, 465, 1, 2, "black")

platform38lvl6 = ObbyPlatform(74, 548, 1, 2, "black")
platform39lvl6 = ObbyPlatform(203, 503, 1, 2, "black")
platform40lvl6 = ObbyPlatform(336, 576, 1, 2, "black")
platform41lvl6 = ObbyPlatform(473, 524, 1, 2, "black")
platform42lvl6 = ObbyPlatform(604, 593, 1, 2, "black")
platform43lvl6 = ObbyPlatform(736, 541, 1, 2, "black")
platform44lvl6 = ObbyPlatform(875, 582, 1, 2, "black")
platform45lvl6 = ObbyPlatform(1012, 526, 1, 2, "black")
platform46lvl6 = ObbyPlatform(1157, 591, 1, 2, "black")

platform47lvl6 = ObbyPlatform(21, 665, 1, 2, "black")
platform48lvl6 = ObbyPlatform(145, 626, 1, 2, "black")
platform49lvl6 = ObbyPlatform(274, 687, 1, 2, "black")
platform50lvl6 = ObbyPlatform(411, 642, 1, 2, "black")
platform51lvl6 = ObbyPlatform(539, 701, 1, 2, "black")
platform52lvl6 = ObbyPlatform(676, 654, 1, 2, "black")
platform53lvl6 = ObbyPlatform(813, 688, 1, 2, "black")
platform54lvl6 = ObbyPlatform(947, 637, 1, 2, "black")
platform55lvl6 = ObbyPlatform(1086, 696, 1, 2, "black")
platform56lvl6 = ObbyPlatform(1224, 648, 1, 2, "black")

platform57lvl6 = ObbyPlatform(112, 145, 1, 2, "red")
platform58lvl6 = ObbyPlatform(256, 157, 1, 2, "red")
platform59lvl6 = ObbyPlatform(392, 135, 1, 2, "black")
platform60lvl6 = ObbyPlatform(531, 155, 1, 2, "black")
platform61lvl6 = ObbyPlatform(662, 143, 1, 2, "black")
platform62lvl6 = ObbyPlatform(799, 158, 1, 2, "red")
platform63lvl6 = ObbyPlatform(931, 139, 1, 2, "red")
platform64lvl6 = ObbyPlatform(1072, 151, 1, 2, "red")
platform65lvl6 = ObbyPlatform(1209, 127, 1, 2, "red")

platform66lvl6 = ObbyPlatform(132, 260, 1, 2, "black")
platform67lvl6 = ObbyPlatform(323, 245, 1, 2, "black")
platform68lvl6 = ObbyPlatform(584, 271, 1, 2, "black")
platform69lvl6 = ObbyPlatform(867, 258, 1, 2, "black")
platform70lvl6 = ObbyPlatform(1055, 312, 1, 2, "black")
platform71lvl6 = ObbyPlatform(1198, 406, 1, 2, "black")

platform72lvl6  = ObbyPlatform(31, 18, 1, 2, "black")
platform73lvl6  = ObbyPlatform(96, 76, 1, 2, "red")
platform74lvl6  = ObbyPlatform(164, 34, 1, 2, "black")
platform75lvl6  = ObbyPlatform(231, 118, 1, 2, "black")
platform76lvl6  = ObbyPlatform(299, 73, 1, 2, "black")
platform77lvl6  = ObbyPlatform(365, 19, 1, 2, "black")
platform78lvl6  = ObbyPlatform(438, 86, 1, 2, "black")
platform79lvl6  = ObbyPlatform(507, 43, 1, 2, "black")
platform80lvl6  = ObbyPlatform(574, 104, 1, 2, "black")
platform81lvl6  = ObbyPlatform(645, 27, 1, 2, "black")
platform82lvl6  = ObbyPlatform(714, 82, 1, 2, "black")
platform83lvl6  = ObbyPlatform(782, 49, 1, 2, "black")
platform84lvl6  = ObbyPlatform(849, 117, 1, 2, "black")
platform85lvl6  = ObbyPlatform(921, 31, 1, 2, "black")
platform86lvl6  = ObbyPlatform(988, 74, 1, 2, "black")
platform87lvl6  = ObbyPlatform(1059, 21, 1, 2, "black")
platform88lvl6  = ObbyPlatform(1127, 111, 1, 2, "black")
platform89lvl6  = ObbyPlatform(1194, 59, 1, 2, "black")
platform90lvl6  = ObbyPlatform(1261, 98, 1, 2, "black")

platform91lvl6  = ObbyPlatform(18, 151, 1, 2, "black")
platform92lvl6  = ObbyPlatform(67, 218, 1, 2, "black")
platform93lvl6  = ObbyPlatform(137, 192, 1, 2, "black")
platform94lvl6  = ObbyPlatform(194, 139, 1, 2, "black")
platform95lvl6  = ObbyPlatform(267, 203, 1, 2, "black")
platform96lvl6  = ObbyPlatform(328, 158, 1, 2, "black")
platform97lvl6  = ObbyPlatform(401, 224, 1, 2, "black")
platform98lvl6  = ObbyPlatform(462, 176, 1, 2, "black")
platform99lvl6  = ObbyPlatform(537, 239, 1, 2, "black")
platform100lvl6 = ObbyPlatform(596, 154, 1, 2, "black")
platform101lvl6 = ObbyPlatform(671, 211, 1, 2, "black")
platform102lvl6 = ObbyPlatform(729, 165, 1, 2, "black")
platform103lvl6 = ObbyPlatform(806, 229, 1, 2, "black")
platform104lvl6 = ObbyPlatform(864, 187, 1, 2, "black")
platform105lvl6 = ObbyPlatform(939, 243, 1, 2, "black")
platform106lvl6 = ObbyPlatform(1003, 169, 1, 2, "black")
platform107lvl6 = ObbyPlatform(1077, 207, 1, 2, "black")
platform108lvl6 = ObbyPlatform(1143, 153, 1, 2, "black")
platform109lvl6 = ObbyPlatform(1218, 235, 1, 2, "black")

platform110lvl6 = ObbyPlatform(45, 287, 1, 2, "black")
platform111lvl6 = ObbyPlatform(108, 347, 1, 2, "black")
platform112lvl6 = ObbyPlatform(179, 302, 1, 2, "black")
platform113lvl6 = ObbyPlatform(247, 369, 1, 2, "black")
platform114lvl6 = ObbyPlatform(316, 319, 1, 2, "black")
platform115lvl6 = ObbyPlatform(381, 376, 1, 2, "black")
platform116lvl6 = ObbyPlatform(455, 288, 1, 2, "black")
platform117lvl6 = ObbyPlatform(521, 337, 1, 2, "black")
platform118lvl6 = ObbyPlatform(591, 391, 1, 2, "black")
platform119lvl6 = ObbyPlatform(654, 314, 1, 2, "black")
platform120lvl6 = ObbyPlatform(719, 372, 1, 2, "black")
platform121lvl6 = ObbyPlatform(787, 327, 1, 2, "black")
platform122lvl6 = ObbyPlatform(856, 385, 1, 2, "black")
platform123lvl6 = ObbyPlatform(927, 301, 1, 2, "black")
platform124lvl6 = ObbyPlatform(994, 361, 1, 2, "black")
platform125lvl6 = ObbyPlatform(1068, 326, 1, 2, "black")
platform126lvl6 = ObbyPlatform(1136, 379, 1, 2, "black")
platform127lvl6 = ObbyPlatform(1203, 294, 1, 2, "black")
platform128lvl6 = ObbyPlatform(1250, 351, 1, 2, "black")

platform129lvl6 = ObbyPlatform(12, 404, 1, 2, "black")
platform130lvl6 = ObbyPlatform(81, 471, 1, 2, "black")
platform131lvl6 = ObbyPlatform(149, 431, 1, 2, "black")
platform132lvl6 = ObbyPlatform(218, 492, 1, 2, "black")
platform133lvl6 = ObbyPlatform(282, 417, 1, 2, "black")
platform134lvl6 = ObbyPlatform(351, 481, 1, 2, "black")
platform135lvl6 = ObbyPlatform(418, 438, 1, 2, "black")
platform136lvl6 = ObbyPlatform(487, 501, 1, 2, "black")
platform137lvl6 = ObbyPlatform(553, 427, 1, 2, "black")
platform138lvl6 = ObbyPlatform(623, 475, 1, 2, "black")
platform139lvl6 = ObbyPlatform(689, 446, 1, 2, "black")
platform140lvl6 = ObbyPlatform(756, 508, 1, 2, "black")
platform141lvl6 = ObbyPlatform(827, 434, 1, 2, "black")
platform142lvl6 = ObbyPlatform(892, 493, 1, 2, "black")
platform143lvl6 = ObbyPlatform(963, 448, 1, 2, "black")
platform144lvl6 = ObbyPlatform(1027, 512, 1, 2, "black")
platform145lvl6 = ObbyPlatform(1099, 423, 1, 2, "black")
platform146lvl6 = ObbyPlatform(1169, 478, 1, 2, "black")
platform147lvl6 = Killblock(1231, 443, 1, 2, "black")

platform148lvl6 = ObbyPlatform(36, 523, 1, 2, "black")
platform149lvl6 = ObbyPlatform(113, 588, 1, 2, "black")
platform150lvl6 = ObbyPlatform(177, 546, 1, 2, "black")

escapeRect6 = Escape(600, 50, 1, 1, "gold", 200, 100)


lvl6List = [
    platform1lvl6, platform2lvl6, platform3lvl6, platform4lvl6,
    platform5lvl6, platform6lvl6, escapeRect6, platform7lvl6,
    platform8lvl6, platform9lvl6, platform10lvl6, platform11lvl6,
    platform12lvl6, platform13lvl6, platform14lvl6, platform15lvl6,
    platform16lvl6, platform17lvl6, platform18lvl6, platform19lvl6,
    platform20lvl6, platform21lvl6, platform22lvl6, platform23lvl6,
    platform24lvl6, platform25lvl6, platform26lvl6, platform27lvl6,
    platform28lvl6, platform29lvl6, platform30lvl6, platform31lvl6,
    platform32lvl6, platform33lvl6, platform34lvl6, platform35lvl6,
    platform36lvl6, platform37lvl6, platform38lvl6, platform39lvl6,
    platform40lvl6, platform41lvl6, platform42lvl6, platform43lvl6,
    platform44lvl6, platform45lvl6, platform46lvl6, platform47lvl6,
    platform48lvl6, platform49lvl6, platform50lvl6, platform51lvl6,
    platform52lvl6, platform53lvl6, platform54lvl6, platform55lvl6,
    platform56lvl6, platform57lvl6, platform58lvl6, platform59lvl6,
    platform60lvl6, platform61lvl6, platform62lvl6, platform63lvl6,
    platform64lvl6, platform65lvl6, platform66lvl6, platform67lvl6,
    platform68lvl6, platform69lvl6, platform70lvl6, platform71lvl6,platform72lvl6, platform73lvl6, platform74lvl6, platform75lvl6,
    platform76lvl6, platform77lvl6, platform78lvl6, platform79lvl6,
    platform80lvl6, platform81lvl6, platform82lvl6, platform83lvl6,
    platform84lvl6, platform85lvl6, platform86lvl6, platform87lvl6,
    platform88lvl6, platform89lvl6, platform90lvl6, platform91lvl6,
    platform92lvl6, platform93lvl6, platform94lvl6, platform95lvl6,
    platform96lvl6, platform97lvl6, platform98lvl6, platform99lvl6,
    platform100lvl6, platform101lvl6, platform102lvl6, platform103lvl6,
    platform104lvl6, platform105lvl6, platform106lvl6, platform107lvl6,
    platform108lvl6, platform109lvl6, platform110lvl6, platform111lvl6,
    platform112lvl6, platform113lvl6, platform114lvl6, platform115lvl6,
    platform116lvl6, platform117lvl6, platform118lvl6, platform119lvl6,
    platform120lvl6, platform121lvl6, platform122lvl6, platform123lvl6,
    platform124lvl6, platform125lvl6, platform126lvl6, platform127lvl6,
    platform128lvl6, platform129lvl6, platform130lvl6, platform131lvl6,
    platform132lvl6, platform133lvl6, platform134lvl6, platform135lvl6,
    platform136lvl6, platform137lvl6, platform138lvl6, platform139lvl6,
    platform140lvl6, platform141lvl6, platform142lvl6, platform143lvl6,
    platform144lvl6, platform145lvl6, platform146lvl6, platform147lvl6,
    platform148lvl6, platform149lvl6, platform150lvl6
]

#7 platforms

platform1lvl7 = ObbyPlatform(100,600,100,300,"red")
platform2lvl7 = ObbyPlatform(700,600,100,300,"red")
platform3lvl7 = Killblock(400,430,20,470,"red")
platform4lvl7 = Killblock(400,50,20,270,"red")
platform5lvl7 = ObbyPlatform(520,700,20,1,"red")
platform6lvl7 = ObbyPlatform(900,220,100,500,"red")
platform7lvl7 = ObbyPlatform(900,200,100,20,"red")
platform8lvl7 = Killblock(750,500,150,10,"red")
platform9lvl7 = ObbyPlatform(850,400,50,10,"red")
platform10lvl7 = ObbyPlatform(850,250,50,10,"red")
escapeRect7 = Escape(1200,300,50,50,"red",1,1)


lvl7List = [platform1lvl7,platform2lvl7,platform3lvl7,platform4lvl7,platform5lvl7,platform6lvl7,
            platform7lvl7,platform8lvl7,platform9lvl7,escapeRect7,platform10lvl7]



#8 platforms

platform1lvl8 = ObbyPlatform(0,650,1280,100,"blue")
escapeRect8 = Killblock(900,500,50,50,"gold")
escape2Rect8 = Escape(600,500,50,50,"gold",1,1)
escape3Rect8 = Killblock(300,500,50,50,"gold")
escape4Rect8 = Killblock(200,500,50,50,"gold")
escape5Rect8 = Killblock(400,500,50,50,"gold")
escape6Rect8 = Killblock(800,500,50,50,"gold")
escape7Rect8 = Killblock(700,500,50,50,"gold")
escape8Rect8 = Killblock(500,500,50,50,"gold")



lvl8List = [platform1lvl8, escapeRect8,escape2Rect8,escape3Rect8,escape4Rect8,escape5Rect8,escape6Rect8
            ,escape7Rect8,escape8Rect8]


#9 platforms




levels = [lvl1List,lvl2List,lvl3List,lvl4List,lvl5List,lvl6List,lvl7List,lvl8List]

currentLvl = 7
currentPlatformList = lvl1List




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # MOVEMENT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and canJump == True:
        player_pos.y -= 20
        gravity = -525 * dt
        canJump = False
    if keys[pygame.K_s]:
        pass
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt


    # GRAVITY
    gravity += 12 * dt
    player_pos.y += gravity
    
    
    # update player hitbox
    playerRect = pygame.Rect(player_pos.x - 32, player_pos.y - 32, 64,64)
    playerHitbox = pygame.Rect(player_pos.x - 34, player_pos.y - 34, 67 ,67)
    
    
    # COLLISION CHECKS
    # platform physics
    canJump = False
    for platform in currentPlatformList:
        if playerRect.colliderect(platform):
            overlap_top = playerRect.bottom - platform.top
            overlap_bottom = platform.bottom - playerRect.top
            overlap_left = playerRect.right - platform.left
            overlap_right = platform.right - playerRect.left
            overlap_y = min(overlap_top, overlap_bottom)
            overlap_x = min(overlap_left, overlap_right)

            if overlap_y <= overlap_x:
                if gravity >= 0 and overlap_top <= overlap_bottom:
                    playerRect.bottom = platform.top
                    gravity = 0
                    canJump = True
                else:
                    playerRect.top = platform.bottom
                    gravity = 0 
            else:
                if overlap_left <= overlap_right:
                    playerRect.right = platform.left
                else:
                    playerRect.left = platform.right
            player_pos.x = playerRect.centerx
            player_pos.y = playerRect.centery



    



        
    # if playerHitbox.colliderect(killblock.rect) and (currentLvl == 5):
    #     running = False

        


    # PRINT STUFF ON SCREEN
    screen.fill("white")


    # print/move platforms
    currentPlatformList = levels[currentLvl - 1]
    for platform in currentPlatformList:
        pygame.draw.rect(screen, platform.color, platform.rect)
        outcome = platform.update(screen,player_pos,playerHitbox)
        
        if outcome == "kill":
            running = False
            print("You Died")
        elif outcome == "teleport":
            player_pos.x = platform.teleportX
            player_pos.y = platform.teleportY
        elif outcome == "escape":
            currentLvl += 1
            if currentLvl > len(levels):
                running = False
                print("you win")
            player_pos.x = platform.escapeX
            player_pos.y = platform.escapeY

        elif outcome == "bounce":
            gravity = -700 * dt


    screen.blit(playerImage, playerRect)
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
