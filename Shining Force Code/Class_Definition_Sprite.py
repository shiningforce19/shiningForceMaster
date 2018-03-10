import pygame

#################################################################################################################################################
#  Sprite Class                                                                                                                              #
#################################################################################################################################################
 
class Sprite(pygame.sprite.Sprite):
    def __init__(self, sprite_dict_S, sprite_dict_W, sprite_dict_N, sprite_dict_E):
        super(Sprite, self).__init__()
        self.images = []

        self.sprite_dict_S = sprite_dict_S
        self.sprite_dict_W = sprite_dict_W
        self.sprite_dict_N = sprite_dict_N
        self.sprite_dict_E = sprite_dict_E
        self.current_sprite_dict = self.sprite_dict_S        # Default to South
        self.orientation = "South"                           # Default to South

        for key, value in self.current_sprite_dict.items():
            self.images.append(value)

        self.counter = 0
        self.index = 0
        self.image = self.images[self.index]

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        
        self.counter += 1
        if (self.counter >= 250): # Frequency of sprite change
            self.counter = 0
            self.index += 1
            
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

    def setOrientation(self, orientation):
        self.orientation = orientation
        if (self.orientation == "South"):
            self.current_sprite_dict = sprite_dict_S
        elif (self.orientation == "West"):
            self.current_sprite_dict = sprite_dict_W
        elif (self.orientation == "North"):
            self.current_sprite_dict = sprite_dict_N
        elif (self.orientation == "East"):
            self.current_sprite_dict = sprite_dict_E
        self.images = self.current_sprite_dict.values()
            
 
