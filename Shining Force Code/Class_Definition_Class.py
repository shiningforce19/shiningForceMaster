import random, os, copy, time
  
#################################################################################################################################################
#  Class Class                                                                                                                              #
#################################################################################################################################################
 
class Class:
    def __init__(self, name, promotion, affinityBonus, styleBonus,
                 HPBonus, MPBonus, STRBonus, MAGBonus, DEFBonus, RESBonus, SPDBonus, SKLBonus, movementBonus, HPgrowth,
                 MPgrowth, STRgrowth, MAGgrowth, DEFgrowth, RESgrowth, SPDgrowth, SKLgrowth, weapontypes, description, levelgains):
        self.c_name = name                                  # Name of the class
        self.c_promotion = promotion                        # Name of the promoted class
        self.c_affinityBonus = affinityBonus                # Affinity bonus for the class
        self.c_styleBonus = styleBonus                      # Style bonus for the class
        self.c_HPBonus = HPBonus                            # HP bonus for the class
        self.c_MPBonus = MPBonus                            # MP bonus for the class
        self.c_STRBonus = STRBonus                          # STR bonus for the class
        self.c_MAGBonus = MAGBonus                          # MAG bonus for the class
        self.c_DEFBonus = DEFBonus                          # DEF bonus for the class
        self.c_RESBonus = RESBonus                          # RES bonus for the class
        self.c_SPDBonus = SPDBonus                          # SPD bonus for the class
        self.c_SKLBonus = SKLBonus                          # SKL bonus for the class
        self.c_movementBonus = movementBonus                # Movement bonus for the class
        self.c_HPgrowth = HPgrowth                          # Increased % chance of getting a levelup in HP for this class
        self.c_MPgrowth = MPgrowth                          # Increased % chance of getting a levelup in MP for this class
        self.c_STRgrowth = STRgrowth                        # Increased % chance of getting a levelup in STR for this class
        self.c_MAGgrowth = MAGgrowth                        # Increased % chance of getting a levelup in MAG for this class
        self.c_DEFgrowth = DEFgrowth                        # Increased % chance of getting a levelup in DEF for this class
        self.c_RESgrowth = RESgrowth                        # Increased % chance of getting a levelup in RES for this class
        self.c_SPDgrowth = SPDgrowth                        # Increased % chance of getting a levelup in SPD for this class
        self.c_SKLgrowth = SKLgrowth                        # Increased % chance of getting a levelup in SKL for this class
        self.c_weapontypes = weapontypes                    # Weapon types that can be wielded by this class
        self.c_description = description                    # Class description
        self.c_levelgains = levelgains                      # Dictionary of new spells and techniques learned at each level
       
    # Getter Functions:
    def getName(self):              return self.c_name
    def getPromotion(self):         return self.c_promotion
    def getAffinityBonus(self):     return self.c_affinityBonus
    def getStyleBonus(self):        return self.c_styleBonus
    def getHPBonus(self):           return self.c_HPBonus
    def getMPBonus(self):           return self.c_MPBonus
    def getSTRBonus(self):          return self.c_STRBonus
    def getMAGBonus(self):          return self.c_MAGBonus
    def getDEFBonus(self):          return self.c_DEFBonus
    def getRESBonus(self):          return self.c_RESBonus
    def getSPDBonus(self):          return self.c_SPDBonus
    def getSKLBonus(self):          return self.c_SKLBonus
    def getMovementBonus(self):     return self.c_MovementBonus
    def getHPgrowth(self):          return self.c_HPgrowth
    def getMPgrowth(self):          return self.c_MPgrowth
    def getSTRgrowth(self):         return self.c_STRgrowth
    def getMAGgrowth(self):         return self.c_MAGgrowth
    def getDEFgrowth(self):         return self.c_DEFgrowth
    def getRESgrowth(self):         return self.c_RESgrowth
    def getSPDgrowth(self):         return self.c_SPDgrowth
    def getSKLgrowth(self):         return self.c_SKLgrowth
    def getWeaponTypes(self):       return self.c_weapontypes
    def getDescription(self):       return self.c_description
    def getLevelGains(self):        return self.c_levelgains


    

 
