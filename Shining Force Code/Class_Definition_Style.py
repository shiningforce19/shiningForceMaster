#################################################################################################################################################
#  Style Class                                                                                                                              #
#################################################################################################################################################
 
class Style:
    def __init__(self, name, STRBonus, DEFBonus, secondaryStyles):
        self.s_name = name                                  # Name of the style
        self.s_STRBonus = STRBonus                          # Bonus to physical attack
        self.s_DEFBonus = DEFBonus                          # Bonus to physical defense
        self.s_secondaryStyles = secondaryStyles            # Related styles grant small bonuses
 
    # Getter Functions:
    def getName(self):              return self.s_name
    def getSTRBonus(self):          return self.s_STRBonus
    def getDEFBonus(self):          return self.s_DEFBonus
    def getSecondaryStyles(self):   return self.s_secondaryStyles




 
