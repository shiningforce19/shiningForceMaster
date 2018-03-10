import sys
import pygame
from pygame.locals import *

class useMyClass(object):
    def __init__(self, myVar):
        self.myVar = myVar
    def getThing(self):
        return self.myVar
