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
        image.blit(self.sheet, (0, 0), rect)
        return image

# Need to set up the display in order for image convert to work
pygame.init() 
DISPLAYSURF = pygame.display.set_mode((32, 32))

# Assets path:
path = '../Assets/'
ss = spritesheet(path + 'ShiningForceTileset.png')
TILESIZE = 32
SCALE_CONST = 1.75

# Constants needed to access dictionary:
SAND_NW_GRASS                       = 0
SAND_N_GRASS                        = 1
SAND_NE_GRASS                       = 2
GRASS_NW_WATER                      = 3
GRASS_N_WATER                       = 4
GRASS_NE_WATER                      = 5
SAND_EW_GRASS                       = 6
SAND_W_GRASS                        = 7
SAND                                = 8
SAND_E_GRASS                        = 9
GRASS_W_WATER                       = 10
GRASS                               = 11
GRASS_E_WATER                       = 12
SAND_ENW_GRASS                      = 13
SAND_SW_GRASS                       = 14
SAND_S_GRASS                        = 15
SAND_SE_GRASS                       = 16
GRASS_SW_WATER                      = 17
GRASS_S_WATER                       = 18
GRASS_SE_WATER                      = 19
SAND_ESW_GRASS                      = 20
FOREST_NW_GRASS                     = 21
FOREST_N_GRASS                      = 22
FOREST_NE_GRASS                     = 23
GRASS_NW_WATER_2                    = 24
GRASS_N_WATER_2                     = 25
GRASS_NE_WATER_2                    = 26
SAND_NS_GRASS                       = 27
FOREST_W_GRASS                      = 28
FOREST                              = 29
FOREST_E_GRASS                      = 30
GRASS_W_WATER_2                     = 31
BUSH_NEWS_GRASS                     = 32
GRASS_E_WATER_2                     = 33
SAND_NWS_GRASS                      = 34
FOREST_SW_GRASS                     = 35
FOREST_S_GRASS                      = 36
FOREST_SE_GRASS                     = 37
GRASS_SW_WATER_2                    = 38         
GRASS_S_WATER_2                     = 39
GRASS_SE_WATER_2                    = 40
SAND_NES_GRASS                      = 41
BUSH_NW_GRASS                       = 42
BUSH_N_GRASS                        = 43
BUSH_NE_GRASS                       = 44
SAND_NW_WATER                       = 45
SAND_N_WATER                        = 46
SAND_NE_WATER                       = 47
FOREST_NEW_GRASS                    = 48
BUSH_W_GRASS                        = 49
BUSH                                = 50
BUSH_E_GRASS                        = 51
SAND_W_WATER                        = 52
WATER                               = 53
SAND_E_WATER                        = 54
FOREST_ESW_GRASS                    = 55
BUSH_SW_GRASS                       = 56
BUSH_S_GRASS                        = 57
BUSH_SE_GRASS                       = 58
SAND_SW_WATER                       = 59
SAND_S_WATER                        = 60
SAND_SE_WATER                       = 61
FOREST_NEWS_GRASS                   = 62
SAND_NW_GRASS_2                     = 63
SAND_N_GRASS_2                      = 64
SAND_NE_GRASS_2                     = 65
SAND_NW_WATER_2                     = 66
SAND_N_WATER_2                      = 67
SAND_NE_WATER_2                     = 68
FOREST_NWS_GRASS                    = 69
SAND_W_GRASS_2                      = 70
SAND_2                              = 71
SAND_E_GRASS_2                      = 72
SAND_W_WATER_2                      = 73
WATER_2                             = 74
SAND_E_WATER_2                      = 75
FOREST_NES_GRASS                    = 76
SAND_SW_GRASS_2                     = 77
SAND_S_GRASS_2                      = 78
SAND_SE_GRASS_2                     = 79
SAND_SW_WATER_2                     = 80
SAND_S_WATER_2                      = 81
SAND_SE_WATER_2                     = 82
BUSH_NWS_GRASS                      = 83
BUSH_NES_GRASS                      = 84
BUSH_NEW_GRASS                      = 85
BUSH_ESW_GRASS                      = 86
WAVYSAND_NW_GRASS                   = 87
WAVYSAND_N_GRASS                    = 88
WAVYSAND_NE_GRASS                   = 89
NAZCA_4                             = 90
NAZCA_8                             = 91
NAZCA_12                            = 92
NAZCA_16                            = 93
WAVYSAND_W_GRASS                    = 94
WAVYSAND                            = 95
WAVYSAND_E_GRASS                    = 96
NAZCA_3                             = 97
NAZCA_7                             = 98
NAZCA_11                            = 99
NAZCA_15                            = 100
WAVYSAND_SW_GRASS                   = 101
WAVYSAND_S_GRASS                    = 102
WAVYSAND_SE_GRASS                   = 103
NAZCA_2                             = 104
NAZCA_6                             = 105
NAZCA_10                            = 106
NAZCA_14                            = 107
WAVYSAND_NEWS_GRASS                 = 108
WAVYSAND_NWS_GRASS                  = 109
WAVYSAND_NES_GRASS                  = 110
NAZCA_1                             = 111
NAZCA_5                             = 112
NAZCA_9                             = 113
NAZCA_13                            = 114
BRIDGE_HORIZONTAL_TOP               = 115
WAVYSAND_NEW_GRASS                  = 116
WAVYSAND_ESW_GRASS                  = 117
BROWNMOUNTAINS_NW                   = 118
BROWNMOUNTAINS_N                    = 119
BROWNMOUNTAINS_NE                   = 120
DRIEDRIVER_WATER_VERT_GRASS_HORIZ   = 121
BRIDGE_HORIZONTAL_BOTTOM            = 122
BRIDGE_VERTICAL                     = 123
GRASS_PATCH                         = 124
BROWNMOUNTAINS_W                    = 125
BROWNMOUNTAINS                      = 126
BROWNMOUNTAINS_E                    = 127
DRIEDRIVE_WATER_HORIZ_GRASS_VERT    = 128
BROWNMOUNTAIN_CAVE                  = 129
FORTRESS                            = 130
VILLAGE                             = 131
BROWNMOUNTAINS_SW                   = 132
BROWNMOUNTAINS_S                    = 133
BROWNMOUNTAINS_SE                   = 134
WATER_CAVE_NW                       = 135
WATER_CAVE_NE                       = 136
WATER_CAVE_NW_2                     = 137
WATER_CAVE_NE_2                     = 138
CHOPPED_TREE                        = 139
GREYMOUNTAINS_TOP_1                 = 140
GREYMOUTAINS_TOP_2                  = 141
WATER_CAVE_SW                       = 142
WATER_CAVE_SE                       = 143
WATER_CAVE_SW_2                     = 144
WATER_CAVE_SE_2                     = 145
FOREST_CLEARING_SHADEABBEY          = 146
GREYMOUNTAINS_MIDDLE_1              = 147
GREYMOUNTAINS_MIDDLE_2              = 148
GREYBRIDGE_HORIZ_TOP                = 149
GREY_CAVE                           = 150
GREY_BIG_CAVE_1                     = 151
GREY_BIG_CAVE_2                     = 152
VILLAGE_BY_BROWNMOUNTAINS           = 153
GREYMOUNTAINS_BOTTOM_1              = 154
GREYMOUNTAINS_BOTTOM_2              = 155
GREYBRIDGE_HORIZE_BOTTOM            = 156
GREY_CAVE_BLOCKED                   = 157
FORTRESS_NW                         = 158
FORTRESS_NE                         = 159
GREYMOUNTAINS_3_TOP                 = 160
GREYMOUNTAINS_4_TOP                 = 161
GREYMOUNTAINS_5_TOP                 = 162
GREYMOUNTAINS_6_TOP                 = 163
BRIDGE_OVER_WATER_HORIZ             = 164
FORTRESS_SW                         = 165
FORTRESS_SE                         = 166
GREYMOUNTAINS_3_BOTTOM              = 167
GREYMOUNTAINS_4_BOTTOM              = 168
GREYMOUNTAINS_5_BOTTOM              = 169
GREYMOUNTAINS_6_BOTTOM              = 170
SMALLVILLAGE_1                      = 171
SMALLVILLAGE_2                      = 172
GRASS_LEDGE                         = 173
FOREST_CLEARING_HOUSE               = 174

# Define the images:
textures = {
            # Sprite is 32x32 pixels at location x,y in the file:
            SAND_NW_GRASS                       : pygame.transform.scale(ss.image_at((1*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_N_GRASS                        : pygame.transform.scale(ss.image_at((2*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_NE_GRASS                       : pygame.transform.scale(ss.image_at((3*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_NW_WATER                      : pygame.transform.scale(ss.image_at((4*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_N_WATER                       : pygame.transform.scale(ss.image_at((5*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_NE_WATER                      : pygame.transform.scale(ss.image_at((6*TILESIZE, 0*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_EW_GRASS                       : pygame.transform.scale(ss.image_at((0*TILESIZE, 1*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_W_GRASS                        : pygame.transform.scale(ss.image_at((1*TILESIZE, 1*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND                                : pygame.transform.scale(ss.image_at((2*TILESIZE, 1*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_E_GRASS                        : pygame.transform.scale(ss.image_at((3*TILESIZE, 1*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_W_WATER                       : pygame.transform.scale(ss.image_at((4*TILESIZE, 1*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS                               : pygame.transform.scale(ss.image_at((5*TILESIZE, 1*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_E_WATER                       : pygame.transform.scale(ss.image_at((6*TILESIZE, 1*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_ENW_GRASS                      : pygame.transform.scale(ss.image_at((0*TILESIZE, 2*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_SW_GRASS                       : pygame.transform.scale(ss.image_at((1*TILESIZE, 2*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_S_GRASS                        : pygame.transform.scale(ss.image_at((2*TILESIZE, 2*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_SE_GRASS                       : pygame.transform.scale(ss.image_at((3*TILESIZE, 2*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_SW_WATER                      : pygame.transform.scale(ss.image_at((4*TILESIZE, 2*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_S_WATER                       : pygame.transform.scale(ss.image_at((5*TILESIZE, 2*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_SE_WATER                      : pygame.transform.scale(ss.image_at((6*TILESIZE, 2*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_ESW_GRASS                      : pygame.transform.scale(ss.image_at((0*TILESIZE, 3*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_NW_GRASS                     : pygame.transform.scale(ss.image_at((1*TILESIZE, 3*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_N_GRASS                      : pygame.transform.scale(ss.image_at((2*TILESIZE, 3*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_NE_GRASS                     : pygame.transform.scale(ss.image_at((3*TILESIZE, 3*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_NW_WATER_2                    : pygame.transform.scale(ss.image_at((4*TILESIZE, 3*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_N_WATER_2                     : pygame.transform.scale(ss.image_at((5*TILESIZE, 3*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_NE_WATER_2                    : pygame.transform.scale(ss.image_at((6*TILESIZE, 3*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_NS_GRASS                       : pygame.transform.scale(ss.image_at((0*TILESIZE, 4*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_W_GRASS                      : pygame.transform.scale(ss.image_at((1*TILESIZE, 4*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST                              : pygame.transform.scale(ss.image_at((2*TILESIZE, 4*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_E_GRASS                      : pygame.transform.scale(ss.image_at((3*TILESIZE, 4*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_W_WATER_2                     : pygame.transform.scale(ss.image_at((4*TILESIZE, 4*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH_NEWS_GRASS                     : pygame.transform.scale(ss.image_at((5*TILESIZE, 4*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_E_WATER_2                     : pygame.transform.scale(ss.image_at((6*TILESIZE, 4*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_NWS_GRASS                      : pygame.transform.scale(ss.image_at((0*TILESIZE, 5*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_SW_GRASS                     : pygame.transform.scale(ss.image_at((1*TILESIZE, 5*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_S_GRASS                      : pygame.transform.scale(ss.image_at((2*TILESIZE, 5*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_SE_GRASS                     : pygame.transform.scale(ss.image_at((3*TILESIZE, 5*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_SW_WATER_2                    : pygame.transform.scale(ss.image_at((4*TILESIZE, 5*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_S_WATER_2                     : pygame.transform.scale(ss.image_at((5*TILESIZE, 5*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_SE_WATER_2                    : pygame.transform.scale(ss.image_at((6*TILESIZE, 5*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_NES_GRASS                      : pygame.transform.scale(ss.image_at((0*TILESIZE, 6*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH_NW_GRASS                       : pygame.transform.scale(ss.image_at((1*TILESIZE, 6*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH_N_GRASS                        : pygame.transform.scale(ss.image_at((2*TILESIZE, 6*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH_NE_GRASS                       : pygame.transform.scale(ss.image_at((3*TILESIZE, 6*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_NW_WATER                       : pygame.transform.scale(ss.image_at((4*TILESIZE, 6*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_N_WATER                        : pygame.transform.scale(ss.image_at((5*TILESIZE, 6*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_NE_WATER                       : pygame.transform.scale(ss.image_at((6*TILESIZE, 6*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_NEW_GRASS                    : pygame.transform.scale(ss.image_at((0*TILESIZE, 7*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH_W_GRASS                        : pygame.transform.scale(ss.image_at((1*TILESIZE, 7*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH                                : pygame.transform.scale(ss.image_at((2*TILESIZE, 7*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH_E_GRASS                        : pygame.transform.scale(ss.image_at((3*TILESIZE, 7*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_W_WATER                        : pygame.transform.scale(ss.image_at((4*TILESIZE, 7*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WATER                               : pygame.transform.scale(ss.image_at((5*TILESIZE, 7*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_E_WATER                        : pygame.transform.scale(ss.image_at((6*TILESIZE, 7*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_ESW_GRASS                    : pygame.transform.scale(ss.image_at((0*TILESIZE, 8*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH_SW_GRASS                       : pygame.transform.scale(ss.image_at((1*TILESIZE, 8*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH_S_GRASS                        : pygame.transform.scale(ss.image_at((2*TILESIZE, 8*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH_SE_GRASS                       : pygame.transform.scale(ss.image_at((3*TILESIZE, 8*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_SW_WATER                       : pygame.transform.scale(ss.image_at((4*TILESIZE, 8*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_S_WATER                        : pygame.transform.scale(ss.image_at((5*TILESIZE, 8*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_SE_WATER                       : pygame.transform.scale(ss.image_at((6*TILESIZE, 8*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_NEWS_GRASS                   : pygame.transform.scale(ss.image_at((0*TILESIZE, 9*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_NW_GRASS_2                     : pygame.transform.scale(ss.image_at((1*TILESIZE, 9*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_N_GRASS_2                      : pygame.transform.scale(ss.image_at((2*TILESIZE, 9*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_NE_GRASS_2                     : pygame.transform.scale(ss.image_at((3*TILESIZE, 9*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_NW_WATER_2                     : pygame.transform.scale(ss.image_at((4*TILESIZE, 9*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_N_WATER_2                      : pygame.transform.scale(ss.image_at((5*TILESIZE, 9*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_NE_WATER_2                     : pygame.transform.scale(ss.image_at((6*TILESIZE, 9*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_NWS_GRASS                    : pygame.transform.scale(ss.image_at((0*TILESIZE, 10*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_W_GRASS_2                      : pygame.transform.scale(ss.image_at((1*TILESIZE, 10*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_2                              : pygame.transform.scale(ss.image_at((2*TILESIZE, 10*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_E_GRASS_2                      : pygame.transform.scale(ss.image_at((3*TILESIZE, 10*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_W_WATER_2                      : pygame.transform.scale(ss.image_at((4*TILESIZE, 10*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WATER_2                             : pygame.transform.scale(ss.image_at((5*TILESIZE, 10*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_E_WATER_2                      : pygame.transform.scale(ss.image_at((6*TILESIZE, 10*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_NES_GRASS                    : pygame.transform.scale(ss.image_at((0*TILESIZE, 11*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_SW_GRASS_2                     : pygame.transform.scale(ss.image_at((1*TILESIZE, 11*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_S_GRASS_2                      : pygame.transform.scale(ss.image_at((2*TILESIZE, 11*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_SE_GRASS_2                     : pygame.transform.scale(ss.image_at((3*TILESIZE, 11*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_SW_WATER_2                     : pygame.transform.scale(ss.image_at((4*TILESIZE, 11*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_S_WATER_2                      : pygame.transform.scale(ss.image_at((5*TILESIZE, 11*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SAND_SE_WATER_2                     : pygame.transform.scale(ss.image_at((6*TILESIZE, 11*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH_NWS_GRASS                      : pygame.transform.scale(ss.image_at((0*TILESIZE, 12*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH_NES_GRASS                      : pygame.transform.scale(ss.image_at((1*TILESIZE, 12*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH_NEW_GRASS                      : pygame.transform.scale(ss.image_at((2*TILESIZE, 12*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BUSH_ESW_GRASS                      : pygame.transform.scale(ss.image_at((3*TILESIZE, 12*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND_NW_GRASS                   : pygame.transform.scale(ss.image_at((4*TILESIZE, 12*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND_N_GRASS                    : pygame.transform.scale(ss.image_at((5*TILESIZE, 12*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND_NE_GRASS                   : pygame.transform.scale(ss.image_at((6*TILESIZE, 12*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_4                             : pygame.transform.scale(ss.image_at((0*TILESIZE, 13*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_8                             : pygame.transform.scale(ss.image_at((1*TILESIZE, 13*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_12                            : pygame.transform.scale(ss.image_at((2*TILESIZE, 13*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_16                            : pygame.transform.scale(ss.image_at((3*TILESIZE, 13*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND_W_GRASS                    : pygame.transform.scale(ss.image_at((4*TILESIZE, 13*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND                            : pygame.transform.scale(ss.image_at((5*TILESIZE, 13*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND_E_GRASS                    : pygame.transform.scale(ss.image_at((6*TILESIZE, 13*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_3                             : pygame.transform.scale(ss.image_at((0*TILESIZE, 14*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_7                             : pygame.transform.scale(ss.image_at((1*TILESIZE, 14*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_11                            : pygame.transform.scale(ss.image_at((2*TILESIZE, 14*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_15                            : pygame.transform.scale(ss.image_at((3*TILESIZE, 14*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND_SW_GRASS                   : pygame.transform.scale(ss.image_at((4*TILESIZE, 14*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND_S_GRASS                    : pygame.transform.scale(ss.image_at((5*TILESIZE, 14*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND_SE_GRASS                   : pygame.transform.scale(ss.image_at((6*TILESIZE, 14*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_2                             : pygame.transform.scale(ss.image_at((0*TILESIZE, 15*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_6                             : pygame.transform.scale(ss.image_at((1*TILESIZE, 15*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_10                            : pygame.transform.scale(ss.image_at((2*TILESIZE, 15*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_14                            : pygame.transform.scale(ss.image_at((3*TILESIZE, 15*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND_NEWS_GRASS                 : pygame.transform.scale(ss.image_at((4*TILESIZE, 15*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND_NWS_GRASS                  : pygame.transform.scale(ss.image_at((5*TILESIZE, 15*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND_NES_GRASS                  : pygame.transform.scale(ss.image_at((6*TILESIZE, 15*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_1                             : pygame.transform.scale(ss.image_at((0*TILESIZE, 16*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_5                             : pygame.transform.scale(ss.image_at((1*TILESIZE, 16*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_9                             : pygame.transform.scale(ss.image_at((2*TILESIZE, 16*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            NAZCA_13                            : pygame.transform.scale(ss.image_at((3*TILESIZE, 16*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BRIDGE_HORIZONTAL_TOP               : pygame.transform.scale(ss.image_at((4*TILESIZE, 16*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND_NEW_GRASS                  : pygame.transform.scale(ss.image_at((5*TILESIZE, 16*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WAVYSAND_ESW_GRASS                  : pygame.transform.scale(ss.image_at((6*TILESIZE, 16*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BROWNMOUNTAINS_NW                   : pygame.transform.scale(ss.image_at((0*TILESIZE, 17*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BROWNMOUNTAINS_N                    : pygame.transform.scale(ss.image_at((1*TILESIZE, 17*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BROWNMOUNTAINS_NE                   : pygame.transform.scale(ss.image_at((2*TILESIZE, 17*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            DRIEDRIVER_WATER_VERT_GRASS_HORIZ   : pygame.transform.scale(ss.image_at((3*TILESIZE, 17*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BRIDGE_HORIZONTAL_BOTTOM            : pygame.transform.scale(ss.image_at((4*TILESIZE, 17*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BRIDGE_VERTICAL                     : pygame.transform.scale(ss.image_at((5*TILESIZE, 17*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_PATCH                         : pygame.transform.scale(ss.image_at((6*TILESIZE, 17*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BROWNMOUNTAINS_W                    : pygame.transform.scale(ss.image_at((0*TILESIZE, 18*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BROWNMOUNTAINS                      : pygame.transform.scale(ss.image_at((1*TILESIZE, 18*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BROWNMOUNTAINS_E                    : pygame.transform.scale(ss.image_at((2*TILESIZE, 18*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            DRIEDRIVE_WATER_HORIZ_GRASS_VERT    : pygame.transform.scale(ss.image_at((3*TILESIZE, 18*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BROWNMOUNTAIN_CAVE                  : pygame.transform.scale(ss.image_at((4*TILESIZE, 18*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FORTRESS                            : pygame.transform.scale(ss.image_at((5*TILESIZE, 18*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            VILLAGE                             : pygame.transform.scale(ss.image_at((6*TILESIZE, 18*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BROWNMOUNTAINS_SW                   : pygame.transform.scale(ss.image_at((0*TILESIZE, 19*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BROWNMOUNTAINS_S                    : pygame.transform.scale(ss.image_at((1*TILESIZE, 19*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BROWNMOUNTAINS_SE                   : pygame.transform.scale(ss.image_at((2*TILESIZE, 19*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WATER_CAVE_NW                       : pygame.transform.scale(ss.image_at((3*TILESIZE, 19*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WATER_CAVE_NE                       : pygame.transform.scale(ss.image_at((4*TILESIZE, 19*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WATER_CAVE_NW_2                     : pygame.transform.scale(ss.image_at((5*TILESIZE, 19*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WATER_CAVE_NE_2                     : pygame.transform.scale(ss.image_at((6*TILESIZE, 19*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            CHOPPED_TREE                        : pygame.transform.scale(ss.image_at((0*TILESIZE, 20*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUNTAINS_TOP_1                 : pygame.transform.scale(ss.image_at((1*TILESIZE, 20*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUTAINS_TOP_2                  : pygame.transform.scale(ss.image_at((2*TILESIZE, 20*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WATER_CAVE_SW                       : pygame.transform.scale(ss.image_at((3*TILESIZE, 20*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WATER_CAVE_SE                       : pygame.transform.scale(ss.image_at((4*TILESIZE, 20*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WATER_CAVE_SW_2                     : pygame.transform.scale(ss.image_at((5*TILESIZE, 20*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            WATER_CAVE_SE_2                     : pygame.transform.scale(ss.image_at((6*TILESIZE, 20*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_CLEARING_SHADEABBEY          : pygame.transform.scale(ss.image_at((0*TILESIZE, 21*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUNTAINS_MIDDLE_1              : pygame.transform.scale(ss.image_at((1*TILESIZE, 21*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUNTAINS_MIDDLE_2              : pygame.transform.scale(ss.image_at((2*TILESIZE, 21*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYBRIDGE_HORIZ_TOP                : pygame.transform.scale(ss.image_at((3*TILESIZE, 21*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREY_CAVE                           : pygame.transform.scale(ss.image_at((4*TILESIZE, 21*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREY_BIG_CAVE_1                     : pygame.transform.scale(ss.image_at((5*TILESIZE, 21*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREY_BIG_CAVE_2                     : pygame.transform.scale(ss.image_at((6*TILESIZE, 21*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            VILLAGE_BY_BROWNMOUNTAINS           : pygame.transform.scale(ss.image_at((0*TILESIZE, 22*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUNTAINS_BOTTOM_1              : pygame.transform.scale(ss.image_at((1*TILESIZE, 22*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUNTAINS_BOTTOM_2              : pygame.transform.scale(ss.image_at((2*TILESIZE, 22*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYBRIDGE_HORIZE_BOTTOM            : pygame.transform.scale(ss.image_at((3*TILESIZE, 22*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREY_CAVE_BLOCKED                   : pygame.transform.scale(ss.image_at((4*TILESIZE, 22*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FORTRESS_NW                         : pygame.transform.scale(ss.image_at((5*TILESIZE, 22*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FORTRESS_NE                         : pygame.transform.scale(ss.image_at((6*TILESIZE, 22*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUNTAINS_3_TOP                 : pygame.transform.scale(ss.image_at((0*TILESIZE, 23*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUNTAINS_4_TOP                 : pygame.transform.scale(ss.image_at((1*TILESIZE, 23*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUNTAINS_5_TOP                 : pygame.transform.scale(ss.image_at((2*TILESIZE, 23*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUNTAINS_6_TOP                 : pygame.transform.scale(ss.image_at((3*TILESIZE, 23*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            BRIDGE_OVER_WATER_HORIZ             : pygame.transform.scale(ss.image_at((4*TILESIZE, 23*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FORTRESS_SW                         : pygame.transform.scale(ss.image_at((5*TILESIZE, 23*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FORTRESS_SE                         : pygame.transform.scale(ss.image_at((6*TILESIZE, 23*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUNTAINS_3_BOTTOM              : pygame.transform.scale(ss.image_at((0*TILESIZE, 24*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUNTAINS_4_BOTTOM              : pygame.transform.scale(ss.image_at((1*TILESIZE, 24*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUNTAINS_5_BOTTOM              : pygame.transform.scale(ss.image_at((2*TILESIZE, 24*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GREYMOUNTAINS_6_BOTTOM              : pygame.transform.scale(ss.image_at((3*TILESIZE, 24*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SMALLVILLAGE_1                      : pygame.transform.scale(ss.image_at((4*TILESIZE, 24*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            SMALLVILLAGE_2                      : pygame.transform.scale(ss.image_at((5*TILESIZE, 24*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            GRASS_LEDGE                         : pygame.transform.scale(ss.image_at((6*TILESIZE, 24*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            FOREST_CLEARING_HOUSE               : pygame.transform.scale(ss.image_at((3*TILESIZE, 25*TILESIZE, TILESIZE, TILESIZE)),(int(32 * SCALE_CONST), int(32 * SCALE_CONST))),
            }




    
