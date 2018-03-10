import sys
import pygame
from pygame.locals import *

DIRT = 0
GRASS = 1
WATER = 2


textures = {
            DIRT : pygame.image.load('dirt_nw.png'),
            GRASS : pygame.image.load('grass.png'),
            WATER : pygame.image.load('water.png')
            }

tilemap = [
            [GRASS, DIRT, DIRT ],
            [WATER, WATER, GRASS],
            [WATER, GRASS, WATER ],
            [DIRT, GRASS, DIRT ]
          ]

TILESIZE = 32
MAPWIDTH = 3
MAPHEIGHT = 4

pygame.init() #setup the display

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

while True:
    #get all user events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

    pygame.display.update()
