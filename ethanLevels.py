from ethanPlatform import *


def level1():
    return [
        CustomPlatform(0, 600, 1280, 20, "red"), 
        CustomPlatform(800, 400, 200, 20, "red"),
        CustomPlatform(785, 303, 200, 20, "red"),
        CustomPlatform(785, 203, 10, 100, "red"),
        CustomPlatform(785, 33, 10, 100, "red"),
        CustomPlatform(50, 530, 150, 20, "red"),
        CustomPlatform(195, 400, 10, 150, "red"),
        CustomPlatform(50, 400, 150, 20, "red"),
        CustomPlatform(300, 400, 35, 20, "red"),
        CustomPlatform(530, 400, 35, 20, "red"),
        EscapeDoor(300, 150, 120, 20, 0, 500),
        CustomPlatform(300, 170, 120, 20, "red"),
    ]


def level2():
    return [
        CustomPlatform(0, 600, 1280, 20, "yellow"),  # floor
        CustomPlatform(200, 50, 100, 20, "yellow"),  # 1 lower left floor
        CustomPlatform(200, 180, 70, 20, "yellow"),  # 1 left floor
        CustomPlatform(350, 0, 20, 270, "yellow"),   # 1 left smaller wall

        CustomPlatform(200, 50, 20, 500, "yellow"),  # 3 left wall
        CustomPlatform(1000, 320, 20, 300, "yellow"),# 4 lower right wall
        CustomPlatform(1000, 0, 20, 250, "yellow"),  # 4 upper right wall
        CustomPlatform(920, 100, 20, 200, "yellow"), # 4 center right wall

        CustomPlatform(640, 250, 100, 20, "yellow"), # 6 center floor
        CustomPlatform(640, 200, 20, 60, "yellow"),  # 6 centerfloorwall
        CustomPlatform(640, 380, 100, 20, "yellow"), # 6 lower center floor
        CustomPlatform(365, 380, 70, 20, "yellow"),  # 7 leftcenter floor

        # Section 1: Far Left Scattered Platforms
        CustomPlatform(50, 500, 40, 10, "yellow"),
        CustomPlatform(150, 430, 20, 10, "yellow"),
        CustomPlatform(60, 350, 25, 10, "yellow"),
        CustomPlatform(130, 320, 20, 10, "yellow"),
        CustomPlatform(200, 270, 20, 10, "yellow"),
        CustomPlatform(95, 240, 25, 10, "yellow"),
        CustomPlatform(160, 160, 20, 10, "yellow"),

        # Upper Right Enclosure with Green Door Anchor
        CustomPlatform(1110, 140, 20, 10, "yellow"),   # Left ledge
        CustomPlatform(1130, 115, 10, 35, "yellow"),   # Left wall boundary
        CustomPlatform(1135, 140, 115, 12, "yellow"),  # Slanted/flat platform base
        EscapeDoor(1140, 110, 100, 15, 0, 500),        # Green exit door

        # Section 7: Far-Right Ledges & Escape Feature
        CustomPlatform(1010, 210, 25, 10, "yellow"),
        CustomPlatform(1090, 245, 20, 10, "yellow"),
        CustomPlatform(1160, 280, 20, 10, "yellow"),
        CustomPlatform(1220, 360, 20, 10, "yellow"),
        CustomPlatform(1140, 450, 40, 12, "yellow"),
    ]


def level3():
    return [
        # Outer Frame / Boundaries (1280x720 Screen)
        CustomPlatform(0, 700, 1280, 20, "blue"),       # Main Ground Floor (y=700)
        CustomPlatform(0, 0, 1280, 20, "blue"),         # Top Ceiling Floor (y=0)
        
        # Bottom Left Vertical Pillars
        CustomPlatform(75, 560, 15, 140, "blue"),
        CustomPlatform(220, 580, 15, 120, "blue"),
        CustomPlatform(180, 640, 50, 12, "blue"),       # Crossbar

        # Lower-Mid Horizontal Platform
        CustomPlatform(350, 620, 165, 15, "blue"),

        # Mid-Left S-Shape / Vertical Assembly
        CustomPlatform(260, 510, 185, 15, "blue"),
        CustomPlatform(525, 350, 15, 180, "blue"),
        CustomPlatform(420, 390, 70, 15, "blue"),
        CustomPlatform(370, 390, 15, 110, "blue"),
        CustomPlatform(390, 430, 40, 15, "blue"),

        # Center Floating & Stair Feature
        CustomPlatform(550, 260, 210, 15, "blue"),
        CustomPlatform(590, 360, 50, 15, "blue"),
        CustomPlatform(640, 500, 150, 15, "blue"),
        CustomPlatform(640, 500, 15, 120, "blue"),      # L-stem down

        # Mid-Right Cross & Pillar Complex
        CustomPlatform(800, 195, 200, 15, "blue"),
        CustomPlatform(800, 265, 15, 260, "blue"),
        CustomPlatform(700, 365, 180, 15, "blue"),
        CustomPlatform(705, 410, 70, 15, "blue"),

        # Far Right Ladder Steps & Boundary Wall
        CustomPlatform(1130, 20, 15, 680, "blue"),      # Right vertical boundary
        CustomPlatform(1030, 150, 100, 12, "blue"),
        CustomPlatform(1060, 240, 70, 12, "blue"),
        CustomPlatform(1060, 360, 70, 12, "blue"),
        CustomPlatform(1060, 470, 70, 12, "blue"),
        CustomPlatform(1060, 590, 70, 12, "blue"),

        # Upper Right Goal Enclosure
        CustomPlatform(880, 395, 60, 12, "blue"),
        EscapeDoor(1040, 115, 80, 15, 0, 500),
    ]


def level4():
    return [
    # Left Elevated Enclosure & Hanging Walls
    CustomPlatform(0, 440, 450, 15, "blue"),         # Main left base platform
    CustomPlatform(210, 120, 250, 15, "blue"),        # Upper left horizontal roof
    CustomPlatform(210, 120, 15, 250, "blue"),        # Far-left vertical drop wall
    CustomPlatform(290, 260, 15, 180, "blue"),        # Center-left vertical divider
    CustomPlatform(365, 160, 15, 230, "blue"),        # Right inner vertical wall
    CustomPlatform(465, 120, 15, 230, "blue"),        # Outer left boundary vertical wall

    # Mid-Section Pit & Stepped Bridges
    CustomPlatform(465, 200, 190, 15, "blue"),        # Mid upper bridge platform
    CustomPlatform(545, 200, 15, 340, "blue"),        # Deep center vertical drop pillar
    CustomPlatform(655, 200, 15, 240, "blue"),        # Mid right vertical wall
    CustomPlatform(660, 300, 40, 10, "blue"),         # Small right-pointing ledge

    # Upper Vertical Obstacle Bars (Top Section)
    CustomPlatform(735, 0, 15, 360, "blue"),          # Vertical bar 1
    CustomPlatform(815, 0, 15, 120, "blue"),          # Upper vertical stub bar 2
    CustomPlatform(815, 240, 15, 200, "blue"),         # Lower vertical bar 2
    CustomPlatform(905, 0, 15, 370, "blue"),          # Vertical bar 3
    CustomPlatform(980, 100, 15, 340, "blue"),         # Vertical bar 4
    CustomPlatform(1085, 0, 15, 370, "blue"),         # Vertical bar 5
    CustomPlatform(1030, 270, 60, 12, "blue"),        # Small horizontal crossbar

    # Mid Horizontal Corridor
    CustomPlatform(660, 440, 620, 15, "blue"),        # Main right horizontal deck

    # Lower Pit & Lower Right Corridor Path
    CustomPlatform(470, 440, 15, 210, "blue"),        # Drop-down left pit wall
    CustomPlatform(470, 650, 690, 15, "blue"),        # Lowest pit floor run
    CustomPlatform(720, 440, 15, 110, "blue"),        # Inner hanging pit wall
    CustomPlatform(720, 550, 400, 15, "blue"),        # Middle horizontal runner

    # Escape Door (Green door at the end of the bottom right tunnel)
    EscapeDoor(1150, 520, 15, 130, 0, 500),
    ]
    


levels = [level1, level2, level3, level4]
