#################################################################################################################################################
#  Technique Class                                                                                                                              #
#################################################################################################################################################
 
class Technique():
    def __init__(self, name, MPcost, damage, buff, style, techniquerange, effect, effectchance, affected, description):
        self.s_name = name                                  # Name of the technique
        self.s_MPcost = MPcost                              # MP cost to use per level [Lv.1 cost, Lv.2 cost, etc.]
        self.s_damage = damage                              # Damage per level [Lv.1 damage, Lv.2 damage, etc.]
        self.s_buff = buff                                  # Buff/Debuff power per level [Lv.1 buff, Lv.2 buff, etc.]
        self.s_style = style                                # Style tied to the technique
        self.s_techniquerange = techniquerange              # Technique range per level [Lv.1 range, Lv.2 range, etc.]
        self.s_effect = effect                              # Secondary Effect of the technique
        self.s_effectchance = effectchance                  # Chance of activating secondary effect per level [Lv.1 chance, Lv2. chance, etc.]
        self.s_affected = affected                          # Affected parties (Allies, Enemies, or Both)
        self.s_description = description                    # Description
 
    # Getter Functions:
    def getName(self):              return self.s_name
    def getMPcost(self):            return self.s_MPcost
    def getDamage(self):            return self.s_damage
    def getBuff(self):              return self.s_buff
    def getStyle(self):             return self.s_style
    def getTechniqueRange(self):    return self.s_techniquerange
    def getEffect(self):            return self.s_effect
    def getEffectChance(self):      return self.s_effectchance
    def getAffected(self):          return self.s_affected
    def getDescription(self):       return self.s_description
