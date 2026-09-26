from ethanPlatform import *


def level2():
    return[
        CustomPlatform(0, 600, 1280, 20, "yellow"), #floor
        CustomPlatform ( 200, 50, 100 ,20, "yellow"), #1 lower left floor
        CustomPlatform ( 200, 180,70,20, "yellow" ),#1 left floor
        CustomPlatform ( 350, 0,20,270, "yellow" ), #1 left smaller wall

        CustomPlatform ( 200, 50,20, 500, "yellow" ),#3 left wall
        CustomPlatform ( 1000, 320,20, 300, "yellow" ),#4 lower right wall
        CustomPlatform ( 1000, 0,20, 250, "yellow" ),#4 upper right wall
        CustomPlatform ( 920, 80,20, 220, "yellow" ),#4 center right wall

        CustomPlatform ( 640, 250, 100 ,20, "yellow"), #6 center floor
        CustomPlatform ( 640, 200,20,60, "yellow" ), #6 centerfloorwall
        CustomPlatform ( 640, 380,100,20, "yellow" ), #6 lower center floor
        CustomPlatform ( 365, 380,70,20, "yellow" ), #7  leftcenter floor

        # Section 1: Far Left Scattered Platforms
        CustomPlatform(50, 500, 40, 10, "yellow"),
        CustomPlatform(150, 430, 20, 10, "yellow"),
        CustomPlatform(60, 350, 25, 10, "yellow"),
        CustomPlatform(130, 320, 20, 10, "yellow"),
        CustomPlatform(200, 270, 20, 10, "yellow"),
        CustomPlatform(95, 240, 25, 10, "yellow"),
        CustomPlatform(160, 160, 20, 10, "yellow"),

        
        # Upper Right Enclosure with Green Door Anchor
        CustomPlatform(1110, 140, 20, 10, "yellow"),        # Left ledge
        CustomPlatform(1130, 115, 10, 35, "yellow"),        # Left wall boundary
        CustomPlatform(1135, 140, 115, 12, "yellow"),       # Slanted/flat platform base
        EscapeDoor(1140, 110, 100, 15, 0, 500),             # Green exit door

         # Section 7: Far-Right Ledges & Escape Feature
        CustomPlatform(1010, 210, 25, 10, "yellow"),
        CustomPlatform(1090, 245, 20, 10, "yellow"),
        CustomPlatform(1160, 280, 20, 10, "yellow"),
        CustomPlatform(1220, 360, 20, 10, "yellow"),
        CustomPlatform(1140, 450, 40, 12, "yellow"),

        #====================================================================#

        # # Main Ground Floor
        # CustomPlatform(0, 580, 1280, 20, "yellow"),

        # # Section 1: Far Left Scattered Platforms
        # CustomPlatform(50, 500, 40, 10, "yellow"),
        # CustomPlatform(150, 430, 20, 10, "yellow"),
        # CustomPlatform(60, 350, 25, 10, "yellow"),
        # CustomPlatform(130, 320, 20, 10, "yellow"),
        # CustomPlatform(200, 270, 20, 10, "yellow"),
        # CustomPlatform(95, 240, 25, 10, "yellow"),
        # CustomPlatform(160, 160, 20, 10, "yellow"),

        # # Section 2: Left Vertical Barrier & Attached Ledges
        # CustomPlatform(280, 100, 20, 470, "yellow"),        # Tall left vertical wall
        # CustomPlatform(300, 100, 65, 15, "yellow"),         # Top right extension
        # CustomPlatform(300, 175, 35, 15, "yellow"),         # Lower right extension

        # # Section 3: Upper-Left Overlapping Vertical Column
        # CustomPlatform(390, 40, 15, 140, "yellow"),          # Vertical pillar
        # CustomPlatform(405, 100, 25, 10, "yellow"),          # Upper ledge right
        # CustomPlatform(405, 145, 25, 10, "yellow"),          # Lower ledge right

        # # Section 4: Center Floating Platforms & Lower Ledge
        # CustomPlatform(340, 410, 45, 12, "yellow"),         # Lower left-center platform
        # CustomPlatform(510, 250, 95, 15, "yellow"),         # Upper central platform
        # CustomPlatform(500, 330, 90, 15, "yellow"),         # Mid central platform

        # # Section 5: Mid-Right Vertical Wall Assembly
        # CustomPlatform(810, 110, 15, 330, "yellow"),        # Upper mid vertical wall
        # CustomPlatform(775, 110, 35, 10, "yellow"),         # Top left cap
        # CustomPlatform(815, 430, 30, 10, "yellow"),         # Bottom right extension

        # # Section 6: Right Inner Wall with Stair-Step Corner
        # CustomPlatform(930, 75, 15, 220, "yellow"),         # Upper right vertical segment
        # CustomPlatform(860, 295, 85, 15, "yellow"),         # Corner horizontal segment
        # CustomPlatform(860, 295, 15, 60, "yellow"),          # Corner vertical step down
        # CustomPlatform(930, 365, 15, 215, "yellow"),        # Lower right vertical segment

        # # Section 7: Far-Right Ledges & Escape Feature
        # CustomPlatform(1010, 210, 25, 10, "yellow"),
        # CustomPlatform(1090, 245, 20, 10, "yellow"),
        # CustomPlatform(1160, 280, 20, 10, "yellow"),
        # CustomPlatform(1220, 360, 20, 10, "yellow"),
        # CustomPlatform(1140, 450, 40, 12, "yellow"),
        
        # # Upper Right Enclosure with Green Door Anchor
        # CustomPlatform(1110, 140, 20, 10, "yellow"),        # Left ledge
        # CustomPlatform(1130, 115, 10, 35, "yellow"),        # Left wall boundary
        # CustomPlatform(1135, 140, 115, 12, "yellow"),       # Slanted/flat platform base
        # EscapeDoor(1140, 110, 100, 15, 0, 500),             # Green exit door
    ]
        # ======================================================================#


def level1():
    return[
        CustomPlatform(0, 600, 1280, 20, "red"), 
        CustomPlatform ( 800, 400, 200 ,20, "red"),
        CustomPlatform ( 785, 303,200,20, "red" ),
        CustomPlatform(785, 203, 10, 100, "red" ),
        CustomPlatform(785, 33, 10, 100, "red" ),
        CustomPlatform(50, 530, 150, 20, "red" ),
        CustomPlatform(195, 400, 10, 150, "red" ),
        CustomPlatform(50, 400, 150, 20, "red" ),
        CustomPlatform(300, 400, 35, 20, "red" ),
        CustomPlatform(530, 400, 35, 20, "red" ),
        EscapeDoor(300, 150, 100, 20, 0,500 ),
        CustomPlatform(300, 170, 100, 20, "red" ),

    ]


# Levels 3-7: World 1-1 from the original Super Mario Bros, split into 5 screens.
# 1 Mario tile = 32px, ground surface at y=600.
def level3():
    return[
        CustomPlatform(0, 600, 1280, 120, "red"), # ground
        CustomPlatform(192, 472, 32, 32, "red"), # ? block
        CustomPlatform(320, 472, 160, 32, "red"), # brick ? brick ? brick
        CustomPlatform(384, 344, 32, 32, "red"), # upper ? block
        CustomPlatform(576, 536, 64, 64, "red"), # small pipe
        CustomPlatform(896, 504, 64, 96, "red"), # medium pipe
        CustomPlatform(1152, 472, 64, 128, "red"), # tall pipe
        EscapeDoor(1270, 0, 10, 600, 40, 540), # walk off the right edge
    ]


def level4():
    return[
        CustomPlatform(0, 600, 608, 120, "red"), # ground
        CustomPlatform(672, 600, 480, 120, "red"), # ground
        CustomPlatform(1248, 600, 32, 120, "red"), # ground
        CustomPlatform(224, 472, 64, 128, "red"), # tall pipe
        CustomPlatform(864, 472, 96, 32, "red"), # brick ? brick
        CustomPlatform(960, 344, 256, 32, "red"), # long upper brick row
        EscapeDoor(1270, 0, 10, 600, 40, 540), # walk off the right edge
    ]


def level5():
    return[
        CustomPlatform(0, 600, 1280, 120, "red"), # ground
        CustomPlatform(32, 344, 128, 32, "red"), # upper bricks + ? block
        CustomPlatform(128, 472, 32, 32, "red"), # coin brick
        CustomPlatform(320, 472, 64, 32, "red"), # two bricks (star)
        CustomPlatform(512, 472, 32, 32, "red"), # ? block
        CustomPlatform(608, 472, 32, 32, "red"), # ? block
        CustomPlatform(608, 344, 32, 32, "red"), # upper ? block
        CustomPlatform(704, 472, 32, 32, "red"), # ? block
        CustomPlatform(896, 472, 32, 32, "red"), # single brick
        CustomPlatform(992, 344, 96, 32, "red"), # upper bricks
        EscapeDoor(1270, 0, 10, 600, 40, 540), # walk off the right edge
    ]


def level6():
    return[
        CustomPlatform(0, 600, 1280, 120, "red"), # ground
        CustomPlatform(32, 344, 128, 32, "red"), # brick ? ? brick
        CustomPlatform(64, 472, 64, 32, "red"), # bricks under the ? blocks
        CustomPlatform(224, 568, 32, 32, "red"), # stairs up
        CustomPlatform(256, 536, 32, 64, "red"), # stairs up
        CustomPlatform(288, 504, 32, 96, "red"), # stairs up
        CustomPlatform(320, 472, 32, 128, "red"), # stairs up
        CustomPlatform(416, 472, 32, 128, "red"), # stairs down
        CustomPlatform(448, 504, 32, 96, "red"), # stairs down
        CustomPlatform(480, 536, 32, 64, "red"), # stairs down
        CustomPlatform(512, 568, 32, 32, "red"), # stairs down
        CustomPlatform(672, 568, 32, 32, "red"), # stairs up to the gap
        CustomPlatform(704, 536, 32, 64, "red"), # stairs up to the gap
        CustomPlatform(736, 504, 32, 96, "red"), # stairs up to the gap
        CustomPlatform(768, 472, 32, 128, "red"), # stairs up to the gap
        CustomPlatform(800, 472, 32, 128, "red"), # stairs up to the gap
        # (the pit between these stairs is left filled in, otherwise you'd be stuck forever)
        CustomPlatform(896, 472, 32, 128, "red"), # stairs down from the gap
        CustomPlatform(928, 504, 32, 96, "red"), # stairs down from the gap
        CustomPlatform(960, 536, 32, 64, "red"), # stairs down from the gap
        CustomPlatform(992, 568, 32, 32, "red"), # stairs down from the gap
        CustomPlatform(1152, 536, 64, 64, "red"), # small pipe
        EscapeDoor(1270, 0, 10, 600, 40, 540), # walk off the right edge
    ]


def level7():
    return[
        CustomPlatform(0, 600, 1280, 120, "red"), # ground
        CustomPlatform(32, 472, 128, 32, "red"), # brick brick ? brick
        CustomPlatform(384, 536, 64, 64, "red"), # small pipe
        CustomPlatform(448, 568, 32, 32, "red"), # final staircase
        CustomPlatform(480, 536, 32, 64, "red"), # final staircase
        CustomPlatform(512, 504, 32, 96, "red"), # final staircase
        CustomPlatform(544, 472, 32, 128, "red"), # final staircase
        CustomPlatform(576, 440, 32, 160, "red"), # final staircase
        CustomPlatform(608, 408, 32, 192, "red"), # final staircase
        CustomPlatform(640, 376, 32, 224, "red"), # final staircase
        CustomPlatform(672, 344, 32, 256, "red"), # final staircase
        CustomPlatform(704, 344, 32, 256, "red"), # final staircase
        CustomPlatform(992, 568, 32, 32, "red"), # flagpole base
        CustomPlatform(1120, 536, 160, 64, "red"), # castle base
        CustomPlatform(1152, 472, 96, 64, "red"), # castle tower
        EscapeDoor(1004, 248, 8, 320, 0, 500), # flagpole (touch it to finish)
    ]


levels = [level1, level2, level3, level4, level5, level6, level7]
