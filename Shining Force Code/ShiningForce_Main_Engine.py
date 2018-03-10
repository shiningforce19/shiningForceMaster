#########################################################################
#
# TO DO:
# -----------------------------------------------------------------------
#
# 1. Make selector movement animation work well with with the camera
# 2. Holding down a key will move pointer as long as it's held down
#
# CHECKPOINT
#
# 1. Be able to select Max
#
#

#
# CRITICAL FLAW (MAYBE?)
#
# Sprites/Characters locations are currently grid-locked, where updating is based on looping through the grid and
# animating every object it finds in a cell. This makes animation a lot more difficult, as we will have to keep track
# of two locations, one grid-locked one, and the other the location to put the sprite, which could be in-between
# grid spaces when animating.
# To fix this, remove the requirement for a cell to contain a character and have characters be free-form. But does this
# make choosing spell targets more difficult???
#
#
#

# FOR SMOOTH SPRITE MOVEMENT:
# CHANGE TO AN "ANIMATING" STATE WHEN key is pressed. While in this state, move a set increment
# for each run of a loop. Within this loop, check for a new key press and queue only the most
# recent key press up to be done at the end of the animation
#
#########################################################################

import sys
import pygame
from pygame.locals import *

from Class_Definition_GridSpace import GridSpace
import Asset_Instantiation_Images as m
from Maps_Instantiation import test_battle
from Population_Instantiation import test_battle_population
from Object_Instantiation_Character import Max
from Object_Instantiation_Character import Bat_1
from Object_Instantiation_Character import Bat_2

########################################################################################################################
#  Main Game Engine and Main Game Loop                                                                                 #
########################################################################################################################

SCALE_CONST = 1.75

# Define Display variables:
TILESIZE = int(32 * SCALE_CONST)
SPRITESIZE = int(24 * SCALE_CONST)
MAPWIDTH = 21
MAPHEIGHT = 21
PADDING = ((TILESIZE - SPRITESIZE) / 2)

CAMERASIZE = 9
CAMERABUFFER = 4                           
WIN_WIDTH = CAMERASIZE*TILESIZE
WIN_HEIGHT = CAMERASIZE*TILESIZE + (2*TILESIZE)
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
cameraX = 0*TILESIZE
cameraY = 12*TILESIZE

# Define Game Variables:
selected = None
ploc_i = 4
ploc_j = 16
state = ""
bufferedCommand = ""

# Set Up the Display:
pygame.init()
DISPLAYSURF = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Shining Force")
icon = pygame.image.load('../Assets/icon.png').convert_alpha()
pygame.display.set_icon(icon)

menu_image_1 = pygame.transform.scale(pygame.image.load('../Assets/Menu_Box_1.png').convert_alpha(), (int(96 * SCALE_CONST), int(64 * SCALE_CONST))) 
menu_image_2 = pygame.transform.scale(pygame.image.load('../Assets/Menu_Box_2.png').convert_alpha(), (int(192 * SCALE_CONST), int(64 * SCALE_CONST))) 

# MENU FOR SAVE/LOAD HERE:

#### Enter a Battle or Exploration:
current_map = test_battle
current_population = test_battle_population

# Create the grid:
grid = []
for i in range (0, MAPWIDTH):
    grid.append([])
    for j in range (0, MAPHEIGHT):
        grid[i].append(0)
for i in range (0, MAPWIDTH):
    for j in range (0, MAPHEIGHT):
        x = GridSpace(None, 0, 0, 0, 0, 0, 0)
        grid[i][j] = x
state = "selecting"
animation_stage_horizontal = 0
animation_stage_vertical = 0

# Fill the grid from the selected population:
for populant in current_population:
    grid[populant[1]][populant[2]].setOccupant(populant[0])

# Initialize selector graphic:
selector_image = pygame.transform.scale(pygame.image.load('../Assets/selector.png').convert(), (int(32 * SCALE_CONST), int(32 * SCALE_CONST)))
selector_image.set_colorkey((248,0,248),0)

#### Main Game Loop:
while True:
    #get all user events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:            
            if event.key == K_RIGHT and ploc_i < MAPWIDTH - 1:
                if state == "selecting":
                    
                    if (ploc_i + 1 > CAMERABUFFER and ploc_i + 1 < MAPWIDTH - CAMERABUFFER):
                        cameraX += (1*TILESIZE)

                    state = "animating"
                    animation_stage_horizontal = 1
            elif event.key == K_LEFT and ploc_i > 0:
                if state == "selecting":

                    if (ploc_i - 1 >= CAMERABUFFER and ploc_i - 1 < MAPWIDTH - CAMERABUFFER - 1):
                        cameraX -= (1*TILESIZE)

                    state = "animating"
                    animation_stage_horizontal = -1
            elif event.key == K_UP and ploc_j > 0:
                if state == "selecting":

                    if (ploc_j - 1 >= CAMERABUFFER and ploc_j - 1 < MAPWIDTH - CAMERABUFFER - 1):
                        cameraY -= (1*TILESIZE)

                    state = "animating"
                    animation_stage_vertical = -1
            elif event.key == K_DOWN and ploc_j < MAPHEIGHT - 1:
                if state == "selecting":

                    if (ploc_j + 1 > CAMERABUFFER and ploc_j + 1 < MAPWIDTH - CAMERABUFFER):
                        cameraY += (1*TILESIZE)

                    state = "animating"
                    animation_stage_vertical = 1
    # Display the map:
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            # Display the map tiles:            
            DISPLAYSURF.blit(m.textures[current_map[row][column]], (column*TILESIZE - cameraX, row*TILESIZE - cameraY, TILESIZE, TILESIZE))
            # Display the sprites:
            if (grid[row][column].isOccupied() == 1):
                grid[row][column].getOccupant().getSprite().update()
                DISPLAYSURF.blit(grid[row][column].getOccupant().getSprite().image, (column*TILESIZE + PADDING - cameraX, row*TILESIZE + PADDING - cameraY, 24, 24))
    # Display the selector if appropriate:
    if state == "selecting":
        DISPLAYSURF.blit(selector_image, (ploc_i*TILESIZE - cameraX, ploc_j*TILESIZE - cameraY, TILESIZE, TILESIZE))
    elif state == "animating":
        if animation_stage_horizontal >= 1:
            animation_stage_horizontal += 1
        elif animation_stage_horizontal <= -1:
            animation_stage_horizontal -= 1
        elif animation_stage_vertical >= 1:
            animation_stage_vertical += 1
        elif animation_stage_vertical <= -1:
            animation_stage_vertical -= 1

        DISPLAYSURF.blit(selector_image, (ploc_i*TILESIZE - cameraX + animation_stage_horizontal, ploc_j*TILESIZE - cameraY + animation_stage_vertical, TILESIZE, TILESIZE))

        if animation_stage_horizontal >= TILESIZE:
            animation_stage_horizontal = 0
            ploc_i += 1
            state = "selecting"
        elif animation_stage_horizontal <= -TILESIZE:
            animation_stage_horizontal = 0
            ploc_i -= 1
            state = "selecting"
        elif animation_stage_vertical >= TILESIZE:
            animation_stage_vertical = 0
            ploc_j += 1
            state = "selecting"
        elif animation_stage_vertical <= -TILESIZE:
            animation_stage_vertical = 0
            ploc_j -= 1
            state = "selecting"

    # Display the menus:
    DISPLAYSURF.blit(menu_image_1, (0*TILESIZE, 9*TILESIZE, TILESIZE, TILESIZE))
    DISPLAYSURF.blit(menu_image_2, (3*TILESIZE, 9*TILESIZE, TILESIZE, TILESIZE))
            
    # Update the display:                           
    pygame.display.flip()
    pygame.display.update()







