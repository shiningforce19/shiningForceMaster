#################################################################################################################################################
#  Equipment Class                                                                                                                              #
#################################################################################################################################################
 
class Equipment():
    def __init__(self, name, equipment_type, sub_type, actionrange, affinity, style, STRbonus, MAGbonus, DEFbonus, RESbonus,
                 SPDbonus, SKLbonus, effect, effectchance, STRrequirement, MAGrequirement, DEFrequirement, RESrequirement,
                 SPDrequirement, SKLrequirement, moralityrequirement, weight, description):
        self.s_name = name                                  # Name of the piece of equipment
        self.s_type = equipment_type                        # Type of equipment (Head, Torso, Arms, Legs, or Weapon)
        self.s_subtype = sub_type                           # Sub-type, mostly used for weapons
        self.s_actionrange = actionrange                    # Range of weapon, or effect radius
        self.s_affinity = affinity                          # Affinity associated with the equipment
        self.s_style = style                                # Style associated with the equipment
        self.s_STRbonus = STRbonus                          # STR bonus granted by the equipment
        self.s_MAGbonus = MAGbonus                          # MAG bonus granted by the equipment
        self.s_DEFbonus = DEFbonus                          # DEF bonus granted by the equipment
        self.s_RESbonus = RESbonus                          # RES bonus granted by the equipment
        self.s_SPDbonus = SPDbonus                          # SPD bonus granted by the equipment
        self.s_SKLbonus = SKLbonus                          # SKL bonus granted by the equipment
        self.s_effect = effect                              # Secondary Effect of the equipment
        self.s_effectchance = effectchance                  # Chance of activating secondary effect
        self.s_STRrequirement = STRrequirement              # Minimum STR stat necessary to equip
        self.s_MAGrequirement = MAGrequirement              # Minimum MAG stat necessary to equip
        self.s_DEFrequirement = DEFrequirement              # Minimum DEF stat necessary to equip
        self.s_RESrequirement = RESrequirement              # Minimum RES stat necessary to equip
        self.s_SPDrequirement = SPDrequirement              # Minimum SPD stat necessary to equip
        self.s_SKLrequirement = SKLrequirement              # Minimum SKL stat necessary to equip
        self.s_moralityrequirement = moralityrequirement    # Minimum morality stat necessary to equip
        self.s_weight = weight                              # Weight cost of the equipment
        self.s_description = description                    # Equipment Description
 
    # Getter Functions:   
    def getName(self):                  return self.s_name
    def getType(self):                  return self.s_type
    def getSubType(self):               return self.s_subtype
    def getRage(self):                  return self.s_actionrange
    def getAffinity(self):              return self.s_affinity   
    def getStyle(self):                 return self.s_style
    def getSTRBonus(self):              return self.s_STRbonus
    def getMAGBonus(self):              return self.s_MAGbonus
    def getDEFBonus(self):              return self.s_DEFbonus
    def getRESBonus(self):              return self.s_RESbonus
    def getSPDBonus(self):              return self.s_SPDbonus
    def getSKLBonus(self):              return self.s_SKLbonus
    def getEffect(self):                return self.s_effect
    def getEffectChance(self):          return self.s_effectchance
    def getSTRRequirement(self):        return self.s_STRrequirement
    def getMAGRequirement(self):        return self.s_MAGrequirement
    def getDEFRequirement(self):        return self.s_DEFrequirement
    def getRESRequirement(self):        return self.s_RESrequirement
    def getSPDRequirement(self):        return self.s_SPDrequirement
    def getSKLRequirement(self):        return self.s_SKLrequirement
    def getMoralityRequirement(self):   return self.s_moralityrequirement
    def getWeight(self):                return self.s_weight
    def getDescription(self):           return self.s_description




    
