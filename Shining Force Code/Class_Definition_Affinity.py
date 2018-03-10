#################################################################################################################################################
#  Affinity Class                                                                                                                              #
#################################################################################################################################################
 
class Affinity:
    def __init__(self, name, MAGBonus, RESBonus, secondaryAffinities):
        self.a_name = name                                  # Name of the affinity
        self.a_MAGBonus = MAGBonus                          # Bonus to magic attack
        self.a_RESBonus = RESBonus                          # Bonus to magic resistance
        self.a_secondaryAffinities = secondaryAffinities    # Related affinities grant small bonuses
 
    # Getter Functions:
    def getName(self):                  return self.a_name
    def getMAGBonus(self):              return self.a_MAGBonus
    def getRESBonus(self):              return self.a_RESBonus
    def getSecondaryAffinities(self):   return self.a_secondaryAffinities
 

 
