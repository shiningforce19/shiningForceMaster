#################################################################################################################################################
#  NPC Class                                                                                                                              #
#################################################################################################################################################
 
class NPC:
    def __init__(self, charid, name, speechlines):
        
        self.c_id = charid                                  # Id number for the character
        self.c_name = name                                  # Must be <= 6 letters
        self.c_speechlines = speechlines                    # Dictionary of speech lines. Key is a special string designating the map,
                                                            #     and the value is a list of text strings for their lines
    # Getter Functions:
    def getId(self):                return self.c_id
    def getName(self):              return self.c_name
    def getSpeechLines(self, skey): return self.c_speechlines[skey]
 
