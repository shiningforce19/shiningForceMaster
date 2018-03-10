#################################################################################################################################################
#  Spell Class                                                                                                                              #
#################################################################################################################################################
 
class Spell:
    def __init__(self, name, MPcost, damage, buff, affinity, castrange, spellrange, effect, effectchance, affected, description):
        self.s_name = name                                  # Name of the spell
        self.s_MPcost = MPcost                              # MP cost to cast per level [Lv.1 cost, Lv.2 cost, etc.]
        self.s_damage = damage                              # Damage per level [Lv.1 damage, Lv.2 damage, etc.]
        self.s_buff = buff                                  # Buff/Debuff power per level [Lv.1 buff, Lv.2 buff, etc.]
        self.s_affinity = affinity                          # Affinity tied to the spell
        self.s_castrange = castrange                        # Casting range per level [Lv.1 range, Lv.2 range, etc.]
        self.s_spellrange = spellrange                      # Spell range per level [Lv.1 range, Lv.2 range, etc.]
        self.s_effect = effect                              # Secondary Effect of the spell
        self.s_effectchance = effectchance                  # Chance of activating secondary effect per level [Lv.1 chance, Lv2. chance, etc.]
        self.s_affected = affected                          # Affected parties (Allies, Enemies, or Both)
        self.s_description = description                    # Description
 
    # Getter Functions:
    def getName(self):              return self.s_name
    def getMPcost(self):            return self.s_MPcost
    def getDamage(self):            return self.s_damage
    def getBuff(self):              return self.s_buff
    def getAffinity(self):          return self.s_affinity
    def getCastRange(self):         return self.s_castrange
    def getSpellRange(self):        return self.s_spellrange
    def getEffect(self):            return self.s_effect
    def getEffectChance(self):      return self.s_effectchance
    def getAffected(self):          return self.s_affected
    def getDescription(self):       return self.s_description
 
