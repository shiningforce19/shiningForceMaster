


## The character Tilesheet has each character sprite being 24x24






import sys
import pygame
from pygame.locals import *

pygame.init() #setup the display
DISPLAYSURF = pygame.display.set_mode((5*32, 5*32))

class spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)





ss = spritesheet('ShiningForceTileset.png')
# Sprite is 16x16 pixels at location 0,0 in the file...
image = ss.image_at((0, 0, 32, 32))
images = []
# Load two images into an array, their transparent bit is (255, 255, 255)
images = ss.images_at([(0, 0, 32, 32),(33, 0, 32,32)])

    



DISPLAYSURF.blit(images[0], (0*32, 1*32, 32, 32))
DISPLAYSURF.blit(images[1], (0*32, 2*32, 32, 32))

pygame.display.update()
