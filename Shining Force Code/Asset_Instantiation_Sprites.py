import sys
import pygame
from pygame.locals import *

#################################################################################################################################################
#  Asset Instantiation                                                                                                                              #
#################################################################################################################################################

class spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()

    # Load a specific image from a specific rectangle:
    def image_at(self, rectangle):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.set_colorkey((248,0,248),0)
        image.blit(self.sheet, (0, 0), rect)
        return image

def load_image(filename):
    image = pygame.image.load(filename).convert()
    image.set_colorkey((248,0,248),0)
    return image

# Need to set up the display in order for image convert to work
TILESIZE = 24
SCALE_CONST = 1.75
pygame.init() 
DISPLAYSURF = pygame.display.set_mode((int(TILESIZE * SCALE_CONST), int(TILESIZE * SCALE_CONST)))

# Assets path:
path = '../Assets/'
ss = spritesheet(path + 'SF_Spritemap.png')

# Constants needed to access dictionary:
MAX_S_1                     = 0
MAX_S_2                     = 1
MAX_W_1                     = 2
MAX_W_2                     = 3
MAX_N_1                     = 4
MAX_N_2                     = 5
MAX_E_1                     = 6
MAX_E_2                     = 7

BAT_S_1                     = 8
BAT_S_2                     = 9
BAT_W_1                     = 10
BAT_W_2                     = 11
BAT_N_1                     = 12
BAT_N_2                     = 13
BAT_E_1                     = 14
BAT_E_2                     = 15

# Define the images:
sprites = {
            # Sprite is 24x24 pixels at location x,y in the file:
            MAX_S_1                     : pygame.transform.scale(ss.image_at((0*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            MAX_S_2                     : pygame.transform.scale(ss.image_at((1*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            MAX_W_1                     : pygame.transform.scale(ss.image_at((2*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            MAX_W_2                     : pygame.transform.scale(ss.image_at((3*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            MAX_N_1                     : pygame.transform.scale(ss.image_at((4*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            MAX_N_2                     : pygame.transform.scale(ss.image_at((5*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            MAX_E_1                     : pygame.transform.scale(pygame.transform.flip(ss.image_at((2*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)), True, False), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            MAX_E_2                     : pygame.transform.scale(pygame.transform.flip(ss.image_at((3*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)), True, False), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),

            BAT_S_1                     : pygame.transform.scale(load_image(path + 'Bat_S_1.png'), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            BAT_S_2                     : pygame.transform.scale(load_image(path + 'Bat_S_2.png'), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            BAT_W_1                     : pygame.transform.scale(load_image(path + 'Bat_W_1.png'), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            BAT_W_2                     : pygame.transform.scale(load_image(path + 'Bat_W_2.png'), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            BAT_N_1                     : pygame.transform.scale(load_image(path + 'Bat_N_1.png'), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            BAT_N_2                     : pygame.transform.scale(load_image(path + 'Bat_N_2.png'), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            BAT_E_1                     : pygame.transform.scale(load_image(path + 'Bat_E_1.png'), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            BAT_E_2                     : pygame.transform.scale(load_image(path + 'Bat_E_2.png'), (int(24 * SCALE_CONST), int(24 * SCALE_CONST))),
            }


    
