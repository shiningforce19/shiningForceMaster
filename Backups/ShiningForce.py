#
#
# To Do:
#
#
# - Make techniques work
#
# canAttack() currently only works for weapon range of 1
# calculateDamage() and calculateMagicDamage() currently empty
# - Need to stop spell from being cast if no enemy in range
#

#
# Stat Bonus 1-5: Very poor, poor, neutral, good, very good. Then randomize a number from them
# Stat growths 1-5: Very poor, poor, neutral, good, very good. Then randomize a number from them.
# #### MAKE SURE THIS NUMBER IS KEPT THE SAME FOR THE ENTIRE PLAYTHROUGH
#
#
# Figure out stat totals for classes and characters. They don't have to be equal, but it will help show who needs more strengths
# Make special weapons for each class

#
# Should implement all character names, place names, etc as constants so I can change them later
#

###########
# Finish section: "Define Spell/Tech LevelUp Learning Dictionaries by Class"
#
#
#
#  INTEGRATE PYGAME
############################################################################################################################




import random, msvcrt, os, copy, time
 
global ploc_i; ploc_i = 0
global ploc_j; ploc_j = 0
global party; party = []
global enemyparty; enemyparty = []
 
#################################################################################################################################################
#  Object Classes                                                                                                                               #
#################################################################################################################################################
 
class Character:
    def __init__(self, charid, name, nametag, HP, MP, STR, MAG, DEF, RES, SPD, SKL, movement, HPgrowth, MPgrowth, STRgrowth, MAGgrowth,
                 DEFgrowth, RESgrowth, SPDgrowth, SKLgrowth, affinity, style, level, charclass, knownspells, knowntechniques,
                 head, torso, arms, legs, weapon, weaponproficiencies, statusafflictions, team):
        
        self.c_id = charid                                  # Id number for the character
        self.c_name = name                                  # Must be <= 6 letters
        self.c_nametag = nametag                            # Must be 3 letters, first is first initial
        self.c_currentHP = HP                               # Current health
        self.c_totalHP = HP                                 # Total health
        self.c_currentMP = MP                               # Current magic power
        self.c_totalMP = MP                                 # Total magic power
        self.c_baseSTR = STR                                # Base Strength, determines attack power
        self.c_currentSTR = STR                             # Current Strength, determines attack power
        self.c_baseMAG = MAG                                # Base Magic, determines magic power
        self.c_currentMAG = MAG                             # Current Magic, determines magic power
        self.c_baseDEF = DEF                                # Base Defense, determines physical resistance
        self.c_currentDEF = DEF                             # Current Defense, determines physical resistance
        self.c_baseRES = RES                                # Base Resistance, determines magical resistance
        self.c_currentRES = RES                             # Current Resistance, determines magical resistance
        self.c_baseSPD = SPD                                # Base Speed, determines double attack and evasion
        self.c_currentSPD = SPD                             # Current Speed, determines double attack and evasion
        self.c_baseSKL = SKL                                # Base Skill, determines blocking ability and critical / secondary effect chance
        self.c_currentSKL = SKL                             # Current Skill, determines blocking ability and critical / secondary effect chance
        self.c_baseMovement = movement                      # How far they can move on a turn
        self.c_currentMovement = movement                   # How far they can move on a turn
        self.c_HPgrowth = HPgrowth                          # HP stat personal growth rate
        self.c_MPgrowth = MPgrowth                          # MP stat personal growth rate
        self.c_STRgrowth = STRgrowth                        # STR stat personal growth rate
        self.c_MAGgrowth = MAGgrowth                        # MAG stat personal growth rate
        self.c_DEFgrowth = DEFgrowth                        # DEF stat personal growth rate
        self.c_RESgrowth = RESgrowth                        # RES stat personal growth rate
        self.c_SPDgrowth = SPDgrowth                        # SPD stat personal growth rate
        self.c_SKLgrowth = SKLgrowth                        # SKL stat personal growth rate
        self.c_affinity = affinity                          # Bonus based on a certain magic type
        self.c_style = style                                # Bonus based on a certain attack style
        self.c_level = level                                # Character level
        self.c_class = charclass                            # Must be < 10 letters
        self.c_knownspells = knownspells                    # Known spells [Slot 1, Slot 2, Slot 3, Slot 4]
        self.c_knowntechniques = knowntechniques            # Known techniques [Slot 1, Slot 2, Slot 3, Slot 4]
        self.c_armor_head = head                            # Armor on head
        self.c_armor_torso = torso                          # Armor on torso
        self.c_armor_arms = arms                            # Armor on arms / hands
        self.c_armor_legs = legs                            # Armor on legs / feet
        self.c_weapon = weapon                              # Weapon equipped
        self.c_currentEXP = 0                               # Current EXP
        self.c_nextlevelEXP = level * 100                   # EXP to next levelup
        self.c_morality = 0                                 # Hidden value, ranges from -100 to 100
        self.c_weaponproficiencies = weaponproficiencies    # Proficiency levels by weapon type (dict)
        self.c_weight = 0                                   # Total weight of equipped equipment
        self.c_statusafflictions = statusafflictions        # List of status afflictions
        self.c_team = team                                  # Team affiliation
 
    # Getter Functions:
    def getId(self):                return self.c_id
    def getName(self):              return self.c_name
    def getNametag(self):           return self.c_nametag
    def getLevel(self):             return self.c_level
    def getBaseMovement(self):      return self.c_baseMovement
    def getCurrentMovement(self):   return self.c_currentMovement
    def getClass(self):             return self.c_class
    def getCurrentHP(self):         return self.c_currentHP
    def getTotalHP(self):           return self.c_totalHP
    def getCurrentMP(self):         return self.c_currentMP
    def getTotalMP(self):           return self.c_totalMP
    def getBaseSTR(self):           return self.c_baseSTR
    def getCurrentSTR(self):        return self.c_currentSTR
    def getBaseMAG(self):           return self.c_baseMAG
    def getCurrentMAG(self):        return self.c_currentMAG
    def getBaseDEF(self):           return self.c_baseDEF
    def getCurrentDEF(self):        return self.c_currentDEF
    def getBaseRES(self):           return self.c_baseRES
    def getCurrentRES(self):        return self.c_currentRES
    def getBaseSPD(self):           return self.c_baseSPD
    def getCurrentSPD(self):        return self.c_currentSPD
    def getBaseSKL(self):           return self.c_baseSKL
    def getCurrentSKL(self):        return self.c_currentSKL
    def getAffinity(self):          return self.c_affinity
    def getStyle(self):             return self.c_style
    def getKnownSpells(self):       return self.c_knownspells
    def getKnownTechniques(self):   return self.c_knowntechniques
    def getArmorHead(self):         return self.c_armor_head
    def getArmorTorso(self):        return self.c_armor_torso
    def getArmorArms(self):         return self.c_armor_arms
    def getArmorLegs(self):         return self.c_armor_legs
    def getWeapon(self):            return self.c_weapon
    def getCurrentEXP(self):        return self.c_currentEXP
    def getNextLevelEXP(self):      return self.c_nextlevelEXP
    def getMorality(self):          return self.c_morality
    def getHPgrowth(self):          return self.c_HPgrowth
    def getMPgrowth(self):          return self.c_MPgrowth
    def getSTRgrowth(self):         return self.c_STRgrowth
    def getMAGgrowth(self):         return self.c_MAGgrowth
    def getDEFgrowth(self):         return self.c_DEFgrowth
    def getRESgrowth(self):         return self.c_RESgrowth
    def getSPDgrowth(self):         return self.c_SPDgrowth
    def getSKLgrowth(self):         return self.c_SKLgrowth
    def getProficiencies(self):     return self.c_weaponproficiencies
    def getWeight(self):            return self.c_weight
    def getStatusAfflictions(self): return self.c_statusafflictions
    def getTeam(self):              return self.c_team
 
    # Setter Functions:
    def setLevel(self, level):                self.c_level = level
    def setBaseMovement(self, movement):      self.c_baseMovement = movement
    def setCurrentMovement(self, movement):   self.c_currentMovement = movement
    def setClass(self, charclass):            self.c_class = charclass
    def setCurrentHP(self, currentHP):        self.c_currentHP = currentHP
    def setTotalHP(self, totalHP):            self.c_totalHP = totalHP
    def setCurrentMP(self, currentMP):        self.c_currentMP = currentMP
    def setTotalMP(self, totalMP):            self.c_totalMP = totalMP
    def setBaseSTR(self, STR):                self.c_baseSTR = STR
    def setCurrentSTR(self, STR):             self.c_currentSTR = STR
    def setBaseMAG(self, MAG):                self.c_baseMAG = MAG
    def setCurrentMAG(self, MAG):             self.c_currentMAG = MAG
    def setBaseDEF(self, DEF):                self.c_baseDEF = DEF
    def setCurrentDEF(self, DEF):             self.c_currentDEF = DEF
    def setBaseRES(self, RES):                self.c_baseRES = RES
    def setCurrentRES(self, RES):             self.c_currentRES = RES
    def setBaseSPD(self, SPD):                self.c_baseSPD = SPD
    def setCurrentSPD(self, SPD):             self.c_currentSPD = SPD
    def setBaseSKL(self, SKL):                self.c_baseSKL = SKL
    def setCurrentSKL(self, SKL):             self.c_currentSKL = SKL
    def setAffinity(self, affinity):          self.c_affinity = affinity
    def setStyle(self, style):                self.c_style = style
    def addKnownSpell(self, spell):           self.c_knownspells.append(spell)
    def addKnownTechnique(self, technique):   self.c_knowntechniques.append(technique)
    def setArmorHead(self, armorhead):        self.c_armor_head = armorhead
    def setArmorTorso(self, armortorso):      self.c_armor_torso = armortorso
    def setArmorArms(self, armorarms):        self.c_armor_arms = armorarms
    def setArmorLegs(self, armorlegs):        self.c_armor_legs = armorlegs
    def setWeapon(self, weapon):              self.c_weapon = weapon
    def changeMorality(self, delta):          self.c_morality += delta
    def setTeam(self, team):                  self.c_team = team
    def increaseProficiency(WPNtype):         self.c_statusafflictions[WPNtype] += 1
    def calculateWeight(self):
        if(self.getArmorHead() != None): self.c_weight += self.getArmorHead().getWeight()
        if(self.getArmorTorso() != None): self.c_weight += self.getArmorTorso().getWeight()
        if(self.getArmorArms() != None): self.c_weight += self.getArmorArms().getWeight()
        if(self.getArmorLegs() != None): self.c_weight += self.getArmorLegs().getWeight()
        if(self.getWeapon() != None): self.c_weight += self.getWeapon().getWeight()
    def addStatusAffliction(affliction): self.c_statusafflictions.append(affliction)
    def addEXP(self, exp):
        self.c_currentEXP += exp
        if (self.c_currentEXP > self.c_nextlevelEXP):
            self.c_currentEXP -= self.c_nextlevelEXP
            levelUp()
     
    # LevelUp and Promotion Functions:
    def levelUp(self):
        self.c_level += 1
        self.c_totalHP += getStatBoost(self.c_HPgrowth, self.c_class.getHPgrowth()); self.c_currentHP += getStatBoost(self.c_HPgrowth, self.c_class.getHPgrowth())
        self.c_totalMP += getStatBoost(self.c_MPgrowth, self.c_class.getMPgrowth()); self.c_currentMP += getStatBoost(self.c_MPgrowth, self.c_class.getMPgrowth())
        self.c_baseSTR += getStatBoost(self.c_STRgrowth, self.c_class.getSTRgrowth()); self.c_currentSTR += getStatBoost(self.c_STRgrowth, self.c_class.getSTRgrowth())
        self.c_baseMAG += getStatBoost(self.c_MAGgrowth, self.c_class.getMAGgrowth()); self.c_currentMAG += getStatBoost(self.c_MAGgrowth, self.c_class.getMAGgrowth())
        self.c_baseDEF += getStatBoost(self.c_DEFgrowth, self.c_class.getDEFgrowth()); self.c_currentDEF += getStatBoost(self.c_DEFgrowth, self.c_class.getDEFgrowth())
        self.c_baseRES += getStatBoost(self.c_RESgrowth, self.c_class.getRESgrowth()); self.c_currentRES += getStatBoost(self.c_RESgrowth, self.c_class.getRESgrowth())
        self.c_baseSPD += getStatBoost(self.c_SPDgrowth, self.c_class.getSPDgrowth()); self.c_currentSPD += getStatBoost(self.c_SPDgrowth, self.c_class.getSPDgrowth())
        self.c_baseSKL += getStatBoost(self.c_SKLgrowth, self.c_class.getSKLgrowth()); self.c_currentSKL += getStatBoost(self.c_SKLgrowth, self.c_class.getSKLgrowth())
 
    def promoteCharacter(self):
        self.c_class = self.c_class.getPromotion()
        self.c_totalHP += self.c_class.getHPBonus(); self.c_currentHP += self.c_class.getHPBonus()
        self.c_totalMP += self.c_class.getMPBonus(); self.c_currentMP += self.c_class.getMPBonus()
        self.c_baseSTR += self.c_class.getSTRBonus(); self.c_currentSTR += self.c_class.getSTRBonus()
        self.c_baseMAG += self.c_class.getMAGBonus(); self.c_currentMAG += self.c_class.getMAGBonus()
        self.c_baseDEF += self.c_class.getDEFBonus(); self.c_currentDEF += self.c_class.getDEFBonus()
        self.c_baseRES += self.c_class.getRESBonus(); self.c_currentRES += self.c_class.getRESBonus()
        self.c_baseSPD += self.c_class.getSPDBonus(); self.c_currentSPD += self.c_class.getSPDBonus()
        self.c_baseSKL += self.c_class.getSKLBonus(); self.c_currentSKL += self.c_class.getSKLBonus()
        self.c_baseMovement += self.c_class.getMovementBonus(); self.c_currentMovement += self.c_class.getMovementBonus()
 
    def getStatBoost(self, personalgrowth, classgrowth):
        return 1 if (random.randrange(personalgrowth + classgrowth, 100) < (personalgrowth + classgrowth)) else 0
 
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
 
class Style:
    def __init__(self, name, STRBonus, DEFBonus, secondaryStyles):
        self.s_name = name                                  # Name of the affinity
        self.s_STRBonus = STRBonus                          # Bonus to physical attack
        self.s_DEFBonus = DEFBonus                          # Bonus to physical defense
        self.s_secondaryStyles = secondaryStyles            # Related styles grant small bonuses
 
    # Getter Functions:
    def getName(self):              return self.s_name
    def getSTRBonus(self):          return self.s_STRBonus
    def getDEFBonus(self):          return self.s_DEFBonus
    def getSecondaryStyles(self):   return self.s_secondaryStyles
 
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
 
#################################################################################################################################################
#  Definitions of all Objects                                                                                                                   #
#################################################################################################################################################
 
# Define Affinities:
Light = Affinity("Light", 0, 1, ["Plant", "Lightning"])
Lightning = Affinity("Lightning", 1, 0, ["Light", "Wind"])
Wind = Affinity("Wind", 0, 1, ["Ice", "Lightning"])
Ice = Affinity("Ice", 1, 0, ["Wind", "Fire"])
Fire = Affinity("Fire", 0, 1, ["Ice", "Dark"])
Dark = Affinity("Dark", 1, 0, ["Fire", "Earth"])
Earth = Affinity("Earth", 0, 1, ["Dark", "Plant"])
Plant = Affinity("Plant", 1, 0, ["Earth", "Light"])
 
# Define Styles:
Slash = Style("Slash", 1, 0, ["Parry", "Clash"])
Clash = Style("Clash", 0, 1, ["Slash", "Bash"])
Bash = Style("Bash", 1, 0, ["Clash", "Block"])
Block = Style("Block", 0, 1, ["Bash", "Throw"])
Throw = Style("Throw", 1, 0, ["Block", "Dodge"])
Dodge = Style("Dodge", 0, 1, ["Throw", "Thrust"])
Thrust = Style("Thrust", 1, 0, ["Dodge", "Parry"])
Parry = Style("Parry", 0, 1, ["Thrust", "Slash"])

# Define Spells:
Shine = Spell("Shine", [2, 3, 5, 10, 15], [5, 7, 10, 15, 30], [], "Light", [2, 2, 2, 3, 3], [0, 1, 2, 2, 0], "Blindness", [2, 3, 4, 5, 10], "Enemies", "A brilliant ray of divine light strikes the foe. May cause blindness.")
Freeze = Spell("Freeze", [2, 3, 5, 10, 15], [5, 7, 10, 15, 30], [], "Ice", [2, 2, 2, 3, 3], [0, 1, 2, 2, 0], "Frozen", [2, 3, 4, 5, 10], "Enemies", "A frigid blizzard strikes the foe. May cause freezing.")
Blaze = Spell("Blaze", [2, 3, 5, 10, 15], [5, 7, 10, 15, 30], [], "Fire", [2, 2, 2, 3, 3], [0, 1, 2, 2, 0], "Burned", [2, 3, 4, 5, 10], "Enemies", "A pillar of flame strikes the foe. May cause burning.")
Bolt = Spell("Bolt", [2, 3, 5, 10, 15], [5, 7, 10, 15, 30], [], "Lightning", [2, 2, 2, 3, 3], [0, 1, 2, 2, 0], "Paralysis", [2, 3, 4, 5, 10], "Enemies", "A bolt of lightning strikes the foe. May cause paralysis.")
Nightshade = Spell("Nightshade", [2, 3, 5, 10, 15], [5, 7, 10, 15, 30], [], "Dark", [2, 2, 2, 3, 3], [0, 1, 2, 2, 0], "Blindness", [2, 3, 4, 5, 10], "Enemies", "A wicked darkness strikes the foe. May cause blindness.")
Gale = Spell("Gale", [2, 3, 5, 10, 15], [5, 7, 10, 15, 30], [], "Wind", [2, 2, 2, 3, 3], [0, 1, 2, 2, 0], "Knocked Down", [2, 3, 4, 5, 10], "Enemies", "A raging wind strikes the foe. May knock foes over.")
Quake = Spell("Quake", [2, 3, 5, 10, 15], [5, 7, 10, 15, 30], [], "Earth", [2, 2, 2, 3, 3], [0, 1, 2, 2, 0], "Knocked Down", [2, 3, 4, 5, 10], "Enemies", "A staggering earthquake strikes the foe. May knock foes over.")
Overgrowth = Spell("Overgrowth", [2, 3, 5, 10, 15], [5, 7, 10, 15, 30], [], "Plant", [2, 2, 2, 3, 3], [0, 1, 2, 2, 0], "Poisoned", [2, 3, 4, 5, 10], "Enemies", "A poewrful vine strikes the foe. May cause poisoning.")
Amplify = Spell("Amplify", [10, 20], [], [10, 20], "None", [1, 2], [0, 1], "Spells Boost 1 Turns", [100, 100], "Allies", "Amplifies the spells of allied mages, boosting their power for a turn.")
Nullify = Spell("Nullify", [10, 20], [], [10, 20], "None", [1, 2], [0, 1], "No Magic 1 Turn", [100, 100], "Enemies", "Nullifies enemy mages, making them unable to use magic for a turn.")
Strengthen = Spell("Strengthen", [10, 20], [], [10, 20], "None", [1, 2], [0, 1], "STR MAG Boost 3 Turns", [100, 100], "Allies", "Increases the STR and MAG of allies for 3 turns.")
Weaken = Spell("Weaken", [10, 20], [], [10, 20], "None", [1, 2], [0, 1], "STR MAG Drop 3 Turns", [100, 100], "Enemies", "Weakens enemy attackers, decreasing their STR and MAG for 3 turns.")
Harden = Spell("Harden", [10, 20], [], [10, 20], "None", [1, 2], [0, 1], "DEF RES Boost 3 Turns", [100, 100], "Allies", "Increases the DEF and RES of allies for 3 turns.")
Soften = Spell("Soften", [10, 20], [], [10, 20], "None", [1, 2], [0, 1], "DEF RES Drop 3 Turns", [100, 100], "Enemies", "Weakens enemy attackers, decreasing their DEF and RES for 3 turns.")
Quicken = Spell("Quicken", [10, 20], [], [10, 20], "None", [1, 2], [0, 1], "SPD Boost 3 Turns", [100, 100], "Allies", "Increases the SPD of allies for 3 turns.")
Heal = Spell("Heal", [2, 3, 5, 10, 15], [], [5, 10, 20, 30, 50], "Light", [1, 1, 2, 2, 3], [0, 0, 0, 0, 0], "Restore HP", [100, 100, 100, 100, 100], "Allies", "Healing light restores an ally's HP.")
DarkHeal = Spell("Dark Heal", [2, 3, 5, 10, 15], [], [10, 20, 40, 60, 100], "Dark", [1, 1, 2, 2, 3], [0, 0, 0, 0, 0], "Restore HP, Drop Morality, Curse Chance", [5, 10, 25, 33, 50], "Allies", "Dark contract restores an ally's HP, but may curse.")
Aura = Spell("Aura", [10, 20, 30, 40, 50], [], [5, 10, 20, 30, 50], "Light", [1, 1, 2, 2, 3], [0, 0, 0, 0, 0], "Restore HP", [100, 100, 100, 100, 100], "Allies", "Healing aura restores the HP of all allies in range.")
DarkAura = Spell("Dark Aura", [10, 20, 30, 40, 50], [], [10, 20, 40, 60, 100], "Dark", [1, 1, 2, 2, 3], [0, 0, 0, 0, 0], "Restore HP, Drop Morality, Curse Chance", [5, 10, 25, 33, 50], "Allies", "Malevolent aura restores the HP of all allies in range, but may curse.")
EnergyTransfer = Spell("Energy Transfer", [1, 2], [], [20, 50], "None", [0, 0], [0, 0], "HP -> MP", [100, 100], "Allies", "Transfers life energy into mana.")
PhysicalSwap = Spell("Physical Swap", [5, 10], [], [], "None", [1, 2], [0, 0], "STR <-> DEF", [100, 100], "Allies", "Swaps an ally's STR and DEF stats.")
MagicalSwap = Spell("Magical Swap", [5, 10], [], [], "None", [1, 2], [0, 0], "MAG <-> RES", [100, 100], "Allies", "Swaps an ally's MAG and RES stats.")
DualSwap = Spell("Dual Swap", [5, 10], [], [], "None", [1, 2], [0, 0], "STR <-> DEF, MAG <-> RES", [100, 100], "Allies", "Swaps an ally's STR and DEF stats, and its MAG and RES stats.")
PowerWithin = Spell("Power Within", [5, 10], [], [], "None", [1, 2], [0, 0], "DEF Drop -> STR Boost, RES Drop -> MAG Boost", [100, 100], "Allies", "Reduces an ally's DEF and RES and increases their STR and MAG respectively.")
ProtectionWithin = Spell("Protection Within", [5, 10], [], [], "None", [1, 2], [0, 0], "STR Drop -> DEF Boost, MAG Drop -> RES Boost", [100, 100], "Allies", "Reduces an ally's STR and MAG and increases their DEF and RES respectively.")
Restore = Spell("Restore", [10, 15], [], [], "None", [1, 2], [0, 0], "All Stats -> Base, Afflictions cleared", [100, 100], "Allies", "Cures an ally of all stat changes and afflictions.")
DivineJudgement = Spell("Divine Judgement", [20], [], [], "None", [2], [1], "If enemy morality < 0, Damage taken = totalHP * morality / 100", [100], "Enemies", "Immoral enemies receive damage in proportion to their wickedness.")
SheerCold = Spell("Sheer Cold", [20], [], [30], "Ice", [2], [1], "Movement Zero 1 Turn, SPD drop 1 Turn", [100], "Enemies", "A bone-chilling frost reduces enemy SPD and freezes them in place for a turn.")
Overheat = Spell("Overheat", [20], [], [], "Fire", [2], [1], "Chance for enemies to remove armors", [20], "Enemies", "An oppressive heat forces enemies to reduce armor load.")
ElectricReflexes = Spell("Electric Reflexes", [20], [], [], "Lightning", [2], [2], "SPD Boost, SKL Boost, and Movement + 1, 3 Turns", [100], "Allies", "Electric impulses boost allies' SPD and SKL, and grant further movement for 3 turns.")
UnholyDrain = Spell("Unholy Drain", [20], [10], [10], "Dark", [2], [2], "Enemy HP -> User's HP", [100], "Enemies", "Dark powers drain HP from all enemies in range, restoring the user.")
Galeforce = Spell("Galeforce", [20], [], [], "Wind", [2], [1], "Allies in range can take another turn after next one", [100], "Allies", "A strong tailwind allows allies in range to take another turn immediately after their next one.")
MagicalMud = Spell("Magical Mud", [20], [], [30], "Earth", [2], [2], "DEF Boost and RES Boost for 3 turns", [100], "Allies", "Enchanted mud coats allies in range, boosting their DEF and RES for 3 turns.")
Aromatherapy = Spell("Aromatherapy", [20], [], [10], "Plant", [3], [3], "Cures Afflictions, Restores HP and MP, Boosts all stats", [100], "Allies", "Soothing magic cures afflictions, restores HP and MP, and boosts all stats of allies in range for 3 turns.")
DragonBreath = Spell("Dragon Breath", [5, 10, 15, 20, 30], [10, 20, 30, 40, 50], [], "None", [2, 2, 3, 3, 3,], [0, 1, 1, 2, 2], "No Effect", [100, 100, 100, 100, 100], "Ancient Mana erupts from the mouth of a dragon.") 

spells_dict = {}; spells_dict["Shine"] = Shine; spells_dict["Freeze"] = Freeze; spells_dict["Blaze"] = Blaze; spells_dict["Bolt"] = Bolt; spells_dict["Nightshade"] = Nightshade;
spells_dict["Gale"] = Gale; spells_dict["Quake"] = Quake; spells_dict["Overgrowth"] = Overgrowth; spells_dict["Amplify"] = Amplify; spells_dict["Nullify"] = Nullify;
spells_dict["Strengthen"] = Strengthen; spells_dict["Weaken"] = Weaken; spells_dict["Harden"] = Harden; spells_dict["Soften"] = Soften; spells_dict["Quicken"] = Quicken;
spells_dict["Heal"] = Heal; spells_dict["Dark Heal"] = DarkHeal; spells_dict["Aura"] = Aura; spells_dict["Dark Aura"] = DarkAura; spells_dict["Energy Transfer"] = EnergyTransfer;
spells_dict["Physical Swap"] = PhysicalSwap; spells_dict["Magical Swap"] = MagicalSwap; spells_dict["Dual Swap"] = DualSwap; spells_dict["Power Within"] = PowerWithin;
spells_dict["Protection Within"] = ProtectionWithin; spells_dict["Restore"] = Restore; spells_dict["Divine Judgement"] = DivineJudgement; spells_dict["Sheer Cold"] = SheerCold;
spells_dict["Overheat"] = Overheat; spells_dict["Electric Reflexes"] = ElectricReflexes; spells_dict["Unholy Drain"] = UnholyDrain; spells_dict["Galeforce"] = Galeforce;
spells_dict["Magical Mud"] = MagicalMud; spells_dict["Aromatherapy"] = Aromatherapy; spells_dict["Dragon Breath"] = DragonBreath;
 
# Define Techniques:
Rend = Technique("Rend", [2, 3, 5, 10, 15], [7, 10, 15, 25, 40], [], "Slash", [1, 1, 1, 1, 1], "Chance of decapitation", [1, 2, 3, 4, 5], "Enemies", "A powerful slash that may rend an enemy's head from its shoulders.")
Disarm = Technique("Disarm", [5, 15, 30], [5, 10, 15], [], "Clash",[1, 1, 1], "Chance to remove opponent's weapon", [20, 33, 40], "Enemies", "A swift twist during a clash that may disarm the enemy's weapon.")
Crush = Technique("Crush", [3, 7, 15, 20, 30], [7, 12, 20, 35, 50], [], "Bash", [1, 1, 1, 1, 1], "Chance to obliterate", [1, 2, 3, 4, 5], "Enemies", "A crushing blow that may obliterate an enemy on the spot.")
IronDefense = Technique("Iron Defense", [5, 15, 30], [], [10, 25, 50], "Block", [0, 0, 0], "Chance of perfect defense", [5, 10, 25], "Enemies", "A strong blocking stance which may block all damage.")
PowerThrow = Technique("Power Throw", [2, 5, 10, 15, 20], [5, 7, 10, 20, 35], [], "Throw", [2, 2, 3, 3, 3], "Chance of critical aim", [1, 2, 3, 4, 5], "Enemies", "A calculated, powerful throw that may strike the enemy's weak point.")
Vanish = Technique("Vanish", [10, 20, 30], [], [10, 20, 30], "Dodge", [0, 0, 0], "Chance of perfect dodge", [5, 10, 25], "Enemies", "A dodge so fast that the user appears to vanish and reappear. May avoid damage entirely.")
PiercingThrust = Technique("Piercing Thrust", [3, 5, 10, 15, 20], [], [7, 10, 15, 25, 40], "Thrust", [1, 1, 1, 1, 1], "Chance of critical aim", [2, 4, 6, 8, 10], "Enemies", "A precise stab that may pierce the enemy's heart.")
Riposte = Technique("Riposte", [5, 15, 30], [10, 30, 50], [], "Parry", [1, 1, 1], "Chance of perfect riposte", [3, 5, 7], "Enemies", "A deft parry that leads into a devastating riposte. May devastate the enemy.")
DefendAlly = Technique("Defend Ally", [5, 10], [], [15, 30], "None", [1, 1], "Chance of perfect defense", [5, 10], "Allies", "Stand next to an ally and assist them in defense until your next turn. May result in perfect defense.")
AssistAlly = Technique("Assist Ally", [5, 10], [15, 30], [], "None", [1, 1], "Chance of overwhelming enemy", [5, 10], "Allies", "Stand next to an ally and assist them in their attack. May overwhelm the enemy.")
Brace = Technique("Brace", [5, 10], [], [10, 20], "None", [0, 0], "DEF Boost and RES Boost", [100, 100], "Allies", "Brace yourself against an attack. Raises DEF and RES.")
Overexertion = Technique("Overexertion", [5, 10], [], [10, 20], "None", [0, 0], "STR Boost and MAG Boost", [100, 100], "Allies", "Fire up to raise STR and MAG, then attack with greater power.")
Quickstep = Technique("Quickstep", [5, 10], [], [20, 40], "None", [0, 0], "SPD Boost", [100, 100], "Allies", "Quickstep to raise SPD.")
Observe = Technique("Observe", [5, 10], [], [10, 20], "None", [0, 0], "SKL Boost", [100, 100], "Allies", "Observe the enemy to increase battle prowess. Raises SKL.")
PowerShot = Technique("Power Shot", [5, 10, 15, 20, 30], [10, 20, 30, 40, 50], [], "None", [2, 2, 3, 3, 4,], [0, 0, 0, 0, 0], "No Effect", [100, 100, 100, 100, 100], "The user lets loose with a powerful attack from a ranged weapon.")

skills_dict = {}; skills_dict["Rend"] = Rend; skills_dict["Disarm"] = Disarm; skills_dict["Crush"] = Crush; skills_dict["Iron Defense"] = IronDefense; skills_dict["Power Throw"] = PowerThrow;
skills_dict["Vanish"] = Vanish; skills_dict["Piercing Thrust"] = PiercingThrust; skills_dict["Riposte"] = Riposte; skills_dict["Defend Ally"] = DefendAlly; skills_dict["Assist Ally"] = AssistAlly;
skills_dict["Brace"] = Brace; skills_dict["Overexertion"] = Overexertion; skills_dict["Quickstep"] = Quickstep; skills_dict["Observe"] = Observe;

# Define Spell/Tech LevelUp Learning Dictionaries by Class:
LvlDict_Lord = {3:"AffinBaseSpell Lv. 1", 5:"TechBaseSpell Lv. 1", 8:"AffinBaseSpell Lv. 2", 10:"TechBaseSpell Lv. 2", 13:"AffinBaseSpell Lv. 3", 15:"TechBaseSpell Lv. 3", 20:"AssistAlly Lv. 1"}
LvlDict_Hero = {25:"AffinBaseSpell Lv. 4", 30:"TechBaseSpell Lv. 4", 35:"AssistAlly Lv. 2", 40:"AffinMasterSpell Lv. 1", 45:"AffinBaseSpell Lv. 5", 50:"TechBaseSpell Lv. 5"}
LvlDict_Manakete = {5:"Dragon Breath Lv. 1", 10:"Brace Lv. 1", 13:"Dragon Breath Lv. 2", 15:"Power Within Lv. 1", 20:"Amplify Lv. 1"}
LvlDict_Dragon = {25:"Dragon Breath Lv. 3", 30:"Brace Lv. 2", 35:"Dragon Breath Lv. 4", 40:"Power Within Lv. 2", 45:"Amplify Lv. 2", 50:"Dragon Breath Lv. 5"}
LvlDict_PegasusRider = {5:"Heal Lv. 1", 10:"Strengthen Lv. 1", 13:"Heal Lv. 2", 15:"Harden Lv. 1", 20:"Restore Lv. 1"}
LvlDict_PegasusKnight = {25:"Heal Lv. 3", 30:"Strengthen Lv. 2", 35:"Heal Lv. 4", 40:"Harden Lv. 2", 45:"Restore Lv. 2", 50:"Heal Lv. 5"}
LvlDict_Archer = {5:"Power Shot Lv. 1", 10:"Power Within Lv. 1", 13:"Power Shot Lv. 2", 15:"Assist Ally Lv. 1", 20:"Observe Lv. 1"}
LvlDict_Sniper = {25:"Power Shot Lv. 3", 30:"Power Within Lv. 2", 35:"Power Shot Lv. 4", 40:"Assist Ally Lv. 2", 45:"Observe Lv. 2", 50:"Power Shot Lv. 5"}
LvlDict_Shaman = {3:"Nightshade Lv. 1", 5:"Dark Heal Lv. 1", 8:"Nightshade Lv. 2", 10:"Dark Heal Lv. 2", 13:"Nightshade Lv. 3", 15:"Dark Heal Lv. 3", 20:"Dark Aura Lv. 1"}
LvlDict_Necromancer = {25:"Dark Aura Lv. 2", 30:"Nightshade Lv. 4", 33: "Dark Aura Lv. 3", 35:"Dark Heal Lv. 4", 38:"Dark Aura Lv. 4" ,40:"Dark Heal Lv. 5", 45:"Nightshade Lv. 5", 48:"Dark Aura Lv. 5", 50:"Unholy Drain Lv. 1"}
LvlDict_FireMage = {5:"Blaze Lv. 1", 10:"Blaze Lv. 2", 15:"Strengthen Lv. 1", 20:"Blaze Lv. 3"}
LvlDict_Pyromancer = {25:"Dual Swap Lv. 1", 30:"Blaze Lv. 4", 35:"Strengthen Lv. 2", 40:"Dual Swap Lv. 2", 45:"Blaze Lv. 5", 50:"Overheat Lv. 1"}
LvlDict_EarthMage = {5:"Quake Lv. 1", 10:"Harden Lv. 1", 15:"Quake Lv. 2", 20:"Quake Lv. 3"}
LvlDict_Geomancer = {25:"Harden Lv. 2", 30:"Nullify Lv. 1", 35:"Quake Lv. 4", 40:"Nullify Lv. 2", 45:"Quake Lv. 5", 50:"Magical Mud Lv. 1"}
LvlDict_WindMage = {5:"Gale Lv. 1", 10:"Quicken Lv. 1", 15:"Gale Lv. 2", 20:"Soften Lv. 1"}
LvlDict_Aeromancer = {25:"Gale Lv. 3", 30:"Quicken Lv. 2", 35:"Gale Lv. 4", 40:"Soften Lv. 2", 45:"Gale Lv. 5", 50:"Galeforce Lv. 1"}
LvlDict_IceMage = {5:"Freeze Lv. 1", 10:"Weaken Lv. 1", 15:"Freeze Lv. 2", 20:"Freeze Lv. 3"}
LvlDict_Hydromancer = {25:"Energy Transfer Lv. 1", 30:"Weaken Lv. 2", 35:"Freeze Lv. 4", 40:"Energy Transfer Lv. 2", 45:"Freeze Lv. 5", 50:"Sheer Cold Lv. 1"}
LvlDict_Blitzer = {5:"Bolt Lv. 1", 10:"Magical Swap Lv. 1", 15:"Bolt Lv. 2", 20:"Bolt Lv. 3"}
LvlDict_Electromaster = {25:"Protection Within Lv. 1", 30:"Magical Swap Lv. 2", 35:"Bolt Lv. 4", 40:"Protection Within Lv. 2", 45:"Bolt Lv. 5", 50:"Electric Reflexes Lv. 1"}
LvlDict_Monk = {3:"Shine Lv. 1", 5:"Heal Lv. 1", 8:"Shine Lv. 2", 10:"Heal Lv. 2", 13:"Shine Lv. 3", 15:"Heal Lv. 3", 20:"Aura Lv. 1"}
LvlDict_Hierophant = {25:"Aura Lv. 2", 30:"Shine Lv. 4", 33: "Aura Lv. 3", 35:"Heal Lv. 4", 38:"Aura Lv. 4", 40:"Heal Lv. 5", 45:"Shine Lv. 5", 48:"Aura Lv. 5", 50:"Divine Judgement Lv. 1"}
LvlDict_Dryad = {5:"Overgrowth Lv. 1", 8:"Heal Lv. 1", 10:"Overgrowth Lv. 2", 13:"Heal Lv.2", 15:"Overgrowth Lv. 3", 18:"Heal Lv. 3", 20: "Amplify Lv. 1"}
LvlDict_Floromancer = {25:"Heal Lv. 4", 30:"Overgrowth Lv. 4", 35:"Heal Lv. 5", 40:"Amplify Lv. 2", 45:"Overgrowth Lv. 5", 50:"Aromatherapy Lv. 1"}
LvlDict_Thief = {5:"Vanish Lv. 1", 10:"Power Throw Lv. 1", 13:"Piercing Thrust Lv. 1", 15:"Vanish Lv. 2", 20:"Observe Lv. 1"}
LvlDict_Rogue = {25:"Vanish Lv. 3", 28:"Power Throw Lv. 2", 30:"Piercing Thrust Lv. 2", 35:"Vanish Lv. 4", 38:"Power Throw Lv. 3", 40:"Piercing Thrust Lv. 3", 45:"Observe Lv. 2", 50:"Vanish Lv. 5"}
LvlDict_Mercenary = {5:"Rend Lv. 1", 10:"Riposte Lv. 1", 13:"Disarm Lv. 1", 15:"Rend Lv. 2", 20:"AssistAlly Lv. 1"}
LvlDict_Verteran = {25:"Rend Lv. 3", 28:"Riposte Lv. 2", 30:"Disarm Lv. 2", 35:"Rend Lv. 4", 38:"Riposte Lv. 3", 40:"Disarm Lv. 3", 45:"Assist Ally Lv. 2", 50:"Rend Lv. 5"}
LvlDict_Swordsman = {5:"Disarm Lv. 1", 10:"Rend Lv. 1", 13:"Crush Lv. 1", 15:"Disarm Lv. 2", 20:"DefendAlly Lv. 1"}
LvlDict_Swordmaster = {25:"Disarm Lv. 3", 28:"Rend Lv. 2", 30:"Crush Lv. 2", 35:"Disarm Lv. 4", 38:"Rend Lv. 3", 40:"Crush Lv. 3", 45:"Defend Ally Lv. 2", 50:"Disarm Lv. 5"}
LvlDict_Warrior = {5:"Crush Lv. 1", 10:"Disarm Lv. 1", 13:"Iron Defense Lv. 1", 15:"Crush Lv. 2", 20:"Overexertion Lv. 1"}
LvlDict_Berserker = {25:"Crush Lv. 3", 28:"Disarm Lv. 2", 30:"Iron Defense Lv. 2", 35:"Crush Lv. 4", 38:"Disarm Lv. 3", 40:"Iron Defense Lv. 3", 45:"Overexertion Lv. 2", 50:"Crush Lv. 5"}
LvlDict_Knight = {5:"Iron Defense Lv. 1", 10:"Crush Lv. 1", 13:"Power Throw Lv. 1", 15:"Iron Defense Lv. 2", 20:"Brace Lv. 1"}
LvlDict_General = {25:"Iron Defense Lv. 3", 28:"Crush Lv. 2", 30:"Power Throw Lv. 2", 35:"Iron Defense Lv. 4", 38:"Crush Lv. 3", 40:"Power Throw Lv. 3", 45:"Brace Lv. 2", 50:"Iron Defense Lv. 5"}
LvlDict_Spearman = {5:"Power Throw Lv. 1", 10:"Iron Defense Lv. 1", 13:"Vanish Lv. 1", 15:"Power Throw Lv. 2", 20:"Power Shot Lv. 1"}
LvlDict_Lancer = {25:"Power Throw Lv. 3", 28:"Iron Defense Lv. 2", 30:"Vanish Lv. 2", 33:"Power Shot Lv. 2", 35:"Power Throw Lv. 4", 38:"Iron Defense Lv. 3", 40:"Vanish Lv. 3", 45:"Power Shot Lv. 3", 50:"Power Throw Lv. 5"}
LvlDict_Duelist = {5:"Riposte Lv. 1", 10:"Piercing Thrust Lv. 1", 13:"Rend Lv. 1", 15:"Riposte Lv. 2", 20:"Quickstep Lv. 1"}
LvlDict_Duelmaster = {25:"Riposte Lv. 3", 28:"Piercing Thrust Lv. 2", 30:"Rend Lv. 2", 35:"Riposte Lv. 4", 38:"Piercing Thrust Lv. 3", 40:"Rend Lv. 3", 45:"Quickstep Lv. 2", 50:"Riposte Lv. 5"}
LvlDict_Cavalier = {5:"Piercing Thrust Lv. 1", 10:"Vanish Lv. 1", 13:"Riposte Lv. 1", 15:"Piercing Thrust Lv. 2", 20:"Heal Lv. 1"}
LvlDict_Paladin = {25:"Piercing Thrust Lv. 3", 28:"Vanish Lv. 2", 30:"Riposte Lv. 2", 33:"Heal Lv. 2", 35:"Piercing Thrust Lv. 4", 38:"Vanish Lv. 3", 40:"Riposte Lv. 3", 45:"Heal Lv. 3", 50:"Piercing Thrust Lv. 5"}
#LvlDict_Crusader =
#LvlDict_HolyKnight = 
#LvlDict_StormCaller =
#LvlDict_MageGeneral = 
#LvlDict_Druid = 
#LvlDict_DarkConqueror = 
#LvlDict_Poisoner = 
#LvlDict_Assassin = 
#LvlDict_Falconer = 
#LvlDict_SkyRider = 
#LvlDict_Trenchman = 
#LvlDict_Trapmaster = 
#LvlDict_FlameKnight = 
#LvlDict_LordofFlame = 
#LvlDict_FrostKnight = 
#LvlDict_LordofFrost = 

# Define Classes:                                                     # HP MP ST MG DF RS SP SK MV HP MP ST MG DF RS SP SK
Lord = Class("Lord", "Hero", "None", "None",                            2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, ["sword", "lance", "axe", "stave", "artifact", "ranged"], "A well-balanced fighter with unlimited potential.", LvlDict_Lord)
Hero = Class("Hero", "None", "None", "None",                            4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, ["sword", "lance", "axe", "stave", "artifact", "ranged"], "A unique hero with great power.", LvlDict_Hero)
Manakete = Class("Manakete", "Dragon", "None", "None",                  4, 4, 4, 2, 4, 4, 2, 1, 2, 4, 4, 3, 3, 2, 3, 1, 1, ["artifact"], "A young dragon.", LvlDict_Manakete)
Dragon = Class("Dragon", "None", "None", "None",                        5, 4, 5, 2, 4, 5, 2, 1, 1, 5, 4, 4, 3, 3, 4, 2, 1, ["artifact"], "A powerful dragon.", LvlDict_Dragon)
Villager = Class("Villager", "AnyClass", "None", "None",                1, 1, 1, 1, 1, 1, 1, 1, 0, 5, 5, 5, 5, 5, 5, 5, 5, ["sword", "lance", "axe", "stave", "artifact", "ranged"], "A weak fighter with room to improve.", {})
PegasusRider = Class("Pegasus Rider", "Pegasus Knight", "None", "None", 2, 1, 3, 1, 1, 4, 4, 3, 3, 2, 2, 3, 1, 1, 4, 3, 3, ["sword", "lance"], "A pegasus rider. Soars over the enemy to strike.", LvlDict_PegasusRider)
PegasusKnight = Class("Pegasus Knight", "None", "None", "None",         4, 3, 4, 1, 2, 5, 5, 4, 3, 4, 3, 4, 1, 1, 5, 5, 4, ["sword", "lance", "stave"], "A skilled pegasus rider. Rider and steed work as one to vanquish enemies.", LvlDict_PegasusKnight)
Archer = Class("Archer", "Sniper", "None", "None",                      1, 2, 3, 1, 1, 1, 4, 5, 1, 2, 2, 3, 1, 1, 1, 5, 5, ["ranged"], "An archer adept with the bow. Can shoot long-range.", LvlDict_Archer)                      
Sniper = Class("Sniper", "None", "None", "None",                        3, 3, 5, 1, 2, 2, 5, 5, 1, 3, 3, 5, 1, 2, 2, 5, 5, ["ranged", "artifact"], "A skilled archer with precise long-range aim.", LvlDict_Sniper)
                                                                      # HP MP ST MG DF RS SP SK MV HP MP ST MG DF RS SP SK
Shaman = Class("Shaman", "Necromancer", "Dark", "None",                 2, 4, 1, 3, 1, 5, 1, 4, 0, 1, 3, 1, 3, 0, 4, 1, 4, ["artifact"], "A practitioner of the dark arts. Trained in magic skill and tolerance from a young age.", LvlDict_Shaman)
Necromancer = Class("Necromancer", "None", "Dark", "None",              3, 4, 1, 4, 1, 5, 2, 4, 0, 1, 4, 1, 3, 1, 5, 1, 4, ["stave", "artifact"], "A skilled practitioner of the dark arts. Well-studied in many obscure ways to use magic.", LvlDict_Necromancer)
FireMage = Class("Fire Mage", "Pyromancer", "Fire", "None",             3, 4, 3, 4, 2, 1, 4, 3, 0, 2, 4, 2, 4, 1, 1, 3, 2, ["stave"], "A practitioner of flame magic. Trained for offensive battle.", LvlDict_FireMage)
Pyromancer = Class("Pyromancer", "None", "Fire", "None",                3, 5, 4, 5, 2, 2, 4, 3, 0, 3, 5, 3, 5, 1, 2, 3, 3, ["artifact"], "A skilled practitioner of flame magic. Fierece magical offensive capabilites.", LvlDict_Pyromancer)
EarthMage = Class("Earth Mage", "Geomancer", "Earth", "None",           4, 2, 3, 4, 4, 2, 1, 2, 0, 4, 2, 2, 3, 4, 3, 0, 1, ["axe", "artifact"], "A practitioner of earth magic. Adept at defending themselves from enemies.", LvlDict_EarthMage)
Geomancer = Class("Geomancer", "None", "Earth", "None",                 4, 3, 3, 4, 4, 3, 1, 2, 0, 4, 4, 3, 3, 5, 4, 1, 1, ["axe", "artifact", "stave"], "A skilled practitioner of earth magic. Powerful attackers, but even better defenders.", LvlDict_Geomancer)
WindMage = Class("Wind Mage", "Aeromancer", "Wind", "None",             2, 3, 2, 3, 1, 1, 4, 3, 0, 3, 4, 2, 4, 2, 2, 4, 4, ["stave", "ranged"], "A practitioner of wind magic. Weak until skilled enough to control storms.", LvlDict_WindMage)
Aeromancer = Class("Aeromancer", "None", "Wind", "None",                2, 4, 2, 5, 1, 1, 5, 5, 0, 3, 5, 2, 5, 2, 2, 5, 5, ["stave", "artifact", "ranged"], "A skilled practitioner of wind magic. Able to overcome even the difficulties of manipulating weather.", LvlDict_Aeromancer)
IceMage = Class("Ice Mage", "Hydromancer", "Ice", "None",               1, 4, 2, 4, 2, 3, 3, 4, 0, 2, 3, 1, 3, 1, 2, 2, 3, ["lance", "stave"], "A practitioner of ice magic. Fragile but powerful.", LvlDict_IceMage)
Hydromancer = Class("Hydromancer", "None", "Ice", "None",               3, 5, 2, 4, 3, 3, 3, 4, 0, 4, 4, 1, 5, 3, 3, 2, 4, ["lance", "stave", "artifact"], "A skilled practitioner of ice magic. Gained bulk by learning to control all states of water.", LvlDict_Hydromancer) 
Blitzer = Class("Blitzer", "Electromaster", "Lightning", "None",        2, 3, 2, 4, 1, 1, 5, 4, 0, 2, 3, 1, 5, 1, 1, 5, 4, ["artifact", "ranged"], "A practitioner of lightning magic. Fast and hard-hitting.", LvlDict_Blitzer)
Electromaster = Class("Electromaster", "None", "Lightning", "None",     3, 5, 2, 5, 1, 1, 5, 5, 0, 2, 5, 2, 5, 1, 1, 5, 5, ["artifact", "stave", "ranged"], "A skilled practitioner of lightning magic. Lightning-fast and powerful.", LvlDict_Electromaster)
Monk = Class("Monk", "Hierophant", "Light", "None",                     3, 4, 2, 2, 3, 3, 2, 2, 0, 3, 3, 2, 2, 3, 3, 2, 1, ["stave"], "A practitioner of light magic. Well-balanced and adept at healing.", LvlDict_Monk)
Hierophant = Class("Hierophant", "None", "Light", "None",               3, 5, 2, 3, 3, 3, 2, 2, 0, 4, 4, 2, 3, 3, 3, 2, 2, ["stave", "artifact"], "A skilled practitioner of light magic. Has mana as high as its faith.", LvlDict_Hierophant)
Dryad = Class("Dryad", "Floromancer", "None", "Plant", "None",          2, 3, 3, 3, 2, 2, 4, 4, 0, 2, 3, 3, 3, 2, 2, 4, 3, ["artifact", "sword"], "A practitioner of plant magic. Able to control nature to inflict pain on their enemies.", LvlDict_Dryad)
Floromancer = Class("Floromancer", "None", "Plant", "None",             3, 4, 3, 3, 3, 2, 4, 5, 0, 3, 4, 3, 3, 3, 2, 4, 4, ["artifact", "sword", "stave"], "A skilled practitioner of plant magic. Versatile and dangerous.", LvlDict_Floromancer)
                                                                      # HP MP ST MG DF RS SP SK MV HP MP ST MG DF RS SP SK
Thief = Class("Thief", "Rogue", "None", "Dodge",                        1, 2, 3, 1, 1, 2, 4, 4, 1, 2, 2, 3, 1, 1, 2, 4, 4, ["sword"], "A devilish trickster. Good at dodging and finding enemy weak points.", LvlDict_Thief)
Rogue = Class("Rogue", "None", "None", "Dodge",                         2, 3, 4, 1, 1, 2, 5, 5, 1, 2, 3, 3, 1, 1, 2, 5, 5, ["sword", "ranged"], "A seasoned trickster with sharp attacks and sharp wit.", LvlDict_Rogue)
Mercenary = Class("Mercenary", "Veteran", "None", "Slash",              2, 2, 3, 1, 3, 2, 2, 3, 0, 3, 2, 3, 1, 3, 2, 2, 3, ["sword", "axe"], "A mercenary who loves money.", LvlDict_Mercenary)
Verteran = Class("Veteran", "None", "None", "Slash",                    3, 2, 4, 1, 4, 2, 2, 4, 0, 4, 2, 4, 1, 4, 2, 2, 4, ["sword", "axe", "ranged"], "A hardened veteran who has amassed skills and wealth on the battlefield.", LvlDict_Veteran)
Swordsman = Class("Swordsman", "Swordmaster", "None", "Clash",          1, 1, 3, 1, 2, 2, 3, 4, 0, 2, 1, 3, 1, 2, 2, 3, 4, ["sword"], "A nimble warrior devoted to the sword.", LvlDict_Swordsman)
Swordmaster = Class("Swordmaster", "None", "None", "Clash",             2, 2, 4, 1, 2, 2, 4, 5, 0, 2, 3, 4, 1, 3, 2, 5, 5, ["sword"], "An experienced warrior who has mastered the art of the blade.", LvlDict_Swordmaster)
Warrior = Class("Warrior", "Berseker", "None", "Bash",                  2, 1, 3, 0, 3, 3, 2, 1, 0, 3, 1, 4, 0, 3, 3, 3, 1, ["axe"], "A ruffian with a bloodlust.", LvlDict_Warrior)
Berserker = Class("Berserker", "None", "None", "Bash",                  3, 2, 5, 0, 4, 3, 3, 2, 0, 3, 2, 5, 0, 4, 3, 3, 2, ["axe"], "A master of axes, crazed by battle.", LvlDict_Berserker)
Knight = Class("Knight", "General", "None", "Block",                    4, 1, 3, 0, 5, 0, 1, 1, 0, 4, 1, 3, 0, 5, 0, 1, 2, ["lance", "axe"], "A cautious, sturdy fighter who packs a punch.", LvlDict_Knight)
General = Class("General", "None", "None", "Block",                     5, 1, 3, 0, 5, 0, 1, 2, 0, 5, 1, 4, 0, 5, 0, 1, 2, ["lance", "axe", "sword"], "A walking fortress of pain.", LvlDict_General)
Spearman = Class("Spearman", "Lancer", "None", "Throw",                 3, 2, 3, 1, 2, 2, 3, 2, 0, 3, 2, 3, 1, 2, 2, 3, 2, ["lance"], "A lithe fighter devoted to the lance.", LvlDict_Spearman)
Lancer = Class("Lancer", "None", "None", "Throw",                       4, 3, 4, 2, 3, 3, 4, 3, 0, 4, 3, 4, 2, 3, 3, 4, 3, ["lance"], "A smart warrior who has mastered spear combat.", LvlDict_Lancer)
Duelist = Class("Duelist", "None", "None", "Parry",                     2, 2, 2, 1, 1, 2, 3, 4, 0, 2, 2, 2, 1, 1, 2, 3, 4, ["sword", "lance"], "A rough fighter who likse to live dangerously.", LvlDict_Duelist)
Duelmaster = Class("Duelmaster", "None", "None", "Parry",               3, 3, 3, 1, 2, 2, 4, 5, 0, 3, 3, 4, 1, 2, 2, 5, 5, ["sword", "lance", "artifact"], "A polished master of one-on-one combat.", LvlDict_Duelmaster)
Cavalier = Class("Cavalier", "Paladin", "None", "Thrust",               3, 1, 4, 1, 1, 2, 2, 1, 2, 3, 1, 4, 1, 2, 2, 3, 1, ["sword", "lance"], "A spry warrior who does battle atop their steed.", LvlDict_Cavalier)
Paladin = Class("Paladin", "None", "None", "Thrust",                    4, 2, 5, 2, 2, 2, 3, 2, 2, 4, 2, 5, 2, 2, 2, 3, 1, ["sword", "lance", "stave"], "A hardened warrior who conquers the field with their mount.", LvlDict_Paladin)
                                                                      # HP MP ST MG DF RS SP SK MV HP MP ST MG DF RS SP SK
Crusader = Class("Crusader", "Holy Knight", "Light", "None",            4, 3, 2, 2, 3, 4, 2, 2, 0, 4, 3, 2, 2, 3, 4, 2, 2, ["sword", "stave"], "A warrior who uses light magic.", LvlDict_Crusader)
HolyKnight = Class("Holy Knight", "None", "Light", "None",              5, 4, 3, 3, 3, 5, 2, 3, 0, 5, 4, 3, 3, 3, 5, 2, 3, ["sword", "stave", "lance"], "A strong warrior guided by light magic.", LvlDict_HolyKnight)
StormCaller = Class("Storm Caller", "Mage General", "Lightning", "None",1, 2, 1, 2, 1, 3, 2, 3, 0, 1, 2, 1, 2, 1, 3, 2, 3, ["artifact"], "A weak fighter who tries to call lightning from the heavens.", LvlDict_StormCaller)
MageGeneral = Class("Mage General", "None", "Lightning", "None",        3, 5, 3, 5, 3, 5, 2, 4, 0, 3, 5, 3, 5, 3, 5, 2, 4, ["artifact", "sword", "stave"], "A fiercesome tactician with extreme magical capabilities.", LvlDict_MageGeneral)
Druid = Class("Druid", "Dark Conqueror", "Dark", "None",                2, 3, 2, 3, 1, 3, 1, 4, 0, 2, 3, 2, 3, 1, 3, 1, 4, ["artifact", "lance"], "A warrior who uses dark magic.", LvlDict_Druid) 
DarkConqueror = Class("Dark Conqueror", "None", "Dark", "None",         3, 4, 4, 3, 3, 4, 3, 5, 0, 3, 4, 4, 3, 3, 4, 3, 5, ["artifact", "lance", "axe"], "A terrifying warrior who uses their dark knowledge for conquest.", LvlDict_DarkConqueror)
Poisoner = Class("Poisoner", "Assassin", "Plant", "None",               2, 3, 1, 2, 2, 3, 2, 4, 0, 2, 3, 1, 2, 2, 3, 2, 4, ["artifact"], "An unassuming horticulturist skilled in poisons.", LvlDict_Poisoner)
Assassin = Class("Assassin", "None", "Plant", "None",                   3, 4, 4, 2, 2, 4, 5, 5, 1, 3, 4, 4, 2, 2, 4, 5, 5, ["artifact", "sword"], "A shadowy assassin that can decimate opponents.", LvlDict_Assassin)
Falconer = Class("Falconer", "Sky Rider", "Wind", "None",               2, 2, 2, 3, 2, 4, 4, 4, 2, 2, 2, 2, 3, 2, 4, 4, 4, ["lance", "ranged"], "Fights from atop their large falcon companion.", LvlDict_Falconer)
SkyRider = Class("Sky Rider", "None", "Wind", "None",                   3, 3, 3, 3, 3, 4, 5, 4, 3, 3, 3, 3, 3, 3, 4, 5, 4, ["lance", "ranged", "axe"], "Masters of all airborn beasts, they guide the wind itself.", LvlDict_SkyRider)
Trenchman = Class("Trenchman", "Trapmaster", "Earth", "None",           2, 2, 2, 3, 4, 3, 1, 5, 0, 2, 2, 2, 3, 4, 3, 1, 5, ["axe"], "Calculating movers of earth.", LvlDict_Trenchman)
Trapmaster = Class("Trapmaster", "None", "Earth", "None",               3, 3, 3, 4, 5, 3, 2, 5, 0, 3, 3, 3, 4, 5, 3, 2, 5, ["axe", "ranged"], "Fierce fighters and trap-makers.", LvlDict_Trapmaster)
FlameKnight = Class("Flame Knight", "Lord of Flame", "Fire", "None",    3, 3, 3, 2, 2, 2, 1, 2, 0, 3, 3, 3, 2, 2, 2, 1, 2, ["sword"], "Diligent keepers of the flame of battle.", LvlDict_FlameKnight)
LordofFlame = Class("Lord of Flame", "None", "Fire", "None",            4, 4, 4, 3, 3, 2, 2, 2, 0, 4, 4, 4, 3, 3, 2, 2, 2, ["sword", "axe"], "Masters of fire and physical combat.", LvlDict_LorofFlame)
FrostKnight = Class("Frost Knight", "Lord of Frost", "Ice", "None",     3, 3, 3, 2, 2, 2, 1, 2, 0, 3, 3, 3, 2, 2, 2, 1, 2, ["lance"], "Diligent defenders of ice magic.", LvlDict_FrostKnight)
LordofFrost = Class("Lord of Frost", "None", "Ice", "None",             4, 4, 4, 3, 3, 2, 2, 2, 0, 4, 4, 4, 3, 3, 2, 2, 2, ["lance", "stave"], "Masters of ice and physical combat.", LvlDict_LordofFrost)

# Define Characters:                        HP MP ST MG DF RS SP SK MV HP MP ST MG DF RS SP SK
Max = Character (1, "Max", "MAX",           7, 7, 6, 6, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, "None", "None", 1, Lord, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Kaname = Character (2, "Kaname", "KAN",     6, 6, 6, 5, 4, 4, 3, 1, 6, 4, 3, 5, 4, 3, 3, 2, 1, "None", "None", 1, Manakete, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Donnel = Character (3, "Donnel", "DNL",     5, 1, 2, 2, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, "None", "None", 1, Villager, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Sabrina = Character (4, "Sabrina", "SAB",   6, 6, 2, 5, 2, 5, 2, 8, 5, 2, 4, 1, 4, 2, 3, 2, 5, "Dark", "None", 1, Shaman, ["Nightshade Lv. 1", "Dark Heal Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Tao = Character (5, "Tao", "TAO",           6, 5, 3, 8, 1, 4, 4, 2, 5, 1, 4, 2, 5, 1, 2, 1, 3, "Fire", "None", 1, FireMage, ["Blaze Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Brock = Character (6, "Brock", "BRK",       7, 5, 5, 5, 4, 4, 1, 2, 5, 4, 3, 4, 4, 4, 3, 1, 1, "Earth", "None", 1, EarthMage, ["Quake Lv. 1", "Power Within Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Iris = Character (7, "Iris", "IRS",         6, 6, 2, 6, 2, 6, 7, 6, 5, 2, 4, 1, 4, 1, 2, 5, 3, "Wind", "None", 1, WindMage, ["Gale Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Anri = Character (8, "Anri", "ANR",         6, 8, 2, 8, 2, 3, 3, 2, 5, 2, 4, 1, 5, 1, 2, 2, 3, "Ice", "None", 1, IceMage, ["Heal Lv. 1", "Freeze Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Xander = Character (9, "Xander", "XND",     6, 6, 1, 9, 1, 1, 8, 5, 5, 2, 5, 2, 5, 1, 1, 4, 2, "Lightning", "None", 1, Blitzer, ["Bolt Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force") 
Khris = Character (10, "Khris", "KRS",      7, 8, 1, 5, 2, 5, 4, 6, 5, 4, 4, 1, 3, 2, 4, 3, 3, "Light", "None", 1, Monk, ["Heal Lv. 1", "Strengthen Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force") 
Elise = Character (11, "Elise", "ELS",      6, 7, 2, 6, 4, 7, 6, 5, 5, 3, 4, 2, 3, 3, 4, 4, 2, "Plant", "None", 1, Dryad, ["Overgrowth Lv. 1", "Energy Transfer Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Raven = Character (12, "Raven", "RVN",      6, 2, 5, 1, 3, 3, 8, 7, 6, 2, 1, 4, 1, 2, 2, 4, 4, "None", "Dodge", 1, Thief, [], ["Quickstep Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Gregor = Character (13, "Gregor", "GRG",    8, 2, 8, 1, 5, 2, 4, 4, 5, 4, 2, 5, 1, 3, 1, 3, 2, "None", "Slash", 1, Mercenary, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Mark = Character (14, "Mark", "MRK",        6, 1, 6, 1, 5, 4, 6, 6, 5, 3, 1, 4, 1, 4, 2, 3, 4, "None", "Clash", 1, Swordsman, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Bernard = Character (15, "Bernard", "BRN",  6, 2, 9, 1, 7, 2, 2, 3, 5, 2, 2, 5, 1, 4, 1, 1, 2, "None", "Bash", 1, Warrior, [], ["Overexertion Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Wallace = Character (16, "Wallace", "WLC",  9, 2, 8, 1, 9, 2, 1, 2, 4, 5, 1, 5, 1, 5, 1, 1, 2, "None", "Block", 1, Knight, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Ephraim = Character (17, "Ephraim", "EPH",  7, 3, 5, 2, 2, 5, 4, 4, 5, 3, 3, 3, 2, 1, 3, 3, 3, "None", "Throw", 1, Spearman, [], ["Assist Ally Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")  
Lucina = Character (18, "Lucina", "LUC",    6, 5, 5, 3, 3, 1, 6, 7, 5, 2, 2, 3, 2, 1, 2, 4, 5, "None", "Parry", 1, Duelist, [], ["Observe Lv. 1", "Riposte Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Flex = Character (19, "Flex", "FLX",        7, 2, 6, 1, 4, 3, 4, 3, 6, 4, 1, 3, 1, 3, 2, 3, 2, "None", "Thrust", 1, Cavalier, [], ["Defend Ally Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Quentin = Character (20, "Quentin", "QNT",  6, 2, 6, 2, 2, 4, 5, 7, 5, 2, 2, 5, 1, 2, 2, 4, 4, "None", "None", 1, Archer, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Cordelia = Character (21, "Cordelia", "COR",7, 4, 4, 4, 2, 7, 6, 4, 7, 4, 3, 2, 2, 1, 4, 3, 3, "None", "None", 1, PegasusRider, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Chrom = Character (22, "Chrom", "CHR",      6, 6, 5, 5, 4, 4, 3, 2, 5, 4, 3, 3, 3, 3, 3, 1, 1, "Light", "Slash", 1, Crusader, ["Shine Lv. 1"], ["Rend Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Nino = Character (23, "Nino", "NIN",        6, 9, 1, 1, 1, 1, 2, 3, 5, 5, 5, 4, 4, 3, 3, 3, 3, "Lightning", "None", 1, StormCaller, ["Bolt Lv. 1"], ["Assist Ally Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Leo = Character (24, "Leo", "LEO",          6, 5, 5, 4, 3, 5, 1, 6, 5, 2, 3, 4, 4, 3, 3, 1, 4, "Dark", "None", 1, Druid, ["Dark Heal Lv. 1", "Nullify"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")         
Jaffar = Character (25, "Jaffar", "JFR",    6, 4, 6, 2, 1, 2, 7, 9, 6, 2, 2, 4, 1, 1, 1, 4, 5, "Plant", "None", 1, Poisoner, [],["Overexertion Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
V.Swift = Character (26, "V. Swift", "VSW", 6, 3, 5, 4, 6, 2, 6, 6, 7, 3, 2, 4, 2, 4, 2, 4, 3, "Wind", "None", 1, Falconer, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Loggs = Character (27, "Loggs", "LOG",      8, 5, 4, 4, 5, 4, 1, 2, 5, 3, 3, 3, 3, 4, 4, 1, 1, "Earth", "None", 1, Trenchman, ["Quake Lv. 1"], ["Brace Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Thoros = Character (28, "Thoros", "THO",    7, 5, 6, 6, 2, 2, 3, 3, 5, 3, 3, 4, 4, 2, 2, 2, 2, "Fire", "None", 1, FlameKnight, ["Blaze Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
Miriel = Character (29, "Miriel", "MIR",    7, 5, 3, 3, 5, 5, 4, 3, 5, 3, 3, 2, 2, 4, 4, 3, 2, "Ice", "None", 1, FrostKnight, ["Freeze Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
                                                  # HP    MP   ST  MG  DF  RS  SP  SK  MV HP MP ST MG DF RS SP SK
Wolf_1 = Character (51, "Wolf", "WLF",              10,   0,   4,  0,  2,  2,  3,  0,  5, 0, 0, 0, 0, 0, 0, 0, 0, "Ice", "None", 1, None, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Enemy")
Wolf_2 = Character (52, "Wolf", "WLF",              10,   0,   4,  0,  2,  2,  3,  0,  5, 0, 0, 0, 0, 0, 0, 0, 0, "Ice", "None", 1, None, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Enemy")
Wolf_3 = Character (53, "Wolf", "WLF",              10,   0,   4,  0,  2,  2,  3,  0,  5, 0, 0, 0, 0, 0, 0, 0, 0, "Ice", "None", 1, None, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Enemy")
Hydra = Character (900, "Hydra", "HYD",             500,  100, 50, 50, 50, 50, 40, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, "None", "None", 50, None, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Enemy")
ElementalHydra = Character (901, "ElementalHydra",  1000, 500, 90, 90, 70, 70, 50, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, "All", "None", 100, None, ["Shine Lv. 5", "Freeze Lv. 5", "Blaze Lv. 5", "Bolt Lv. 5", "Gale Lv. 5", "Nightshade Lv. 5", "Quake Lv. 5", "Overgrowth Lv. 5"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Enemy")








 
#### Equipment(self, name, equipment_type, sub_type, actionrange, affinity, style, STRbonus, MAGbonus, DEFbonus, RESbonus,
#              SPDbonus, SKLbonus, effect, effectchance, STRrequirement, MAGrequirement, DEFrequirement, RESrequirement,
#              SPDrequirement, SKLrequirement, moralityrequirement, weight, description) 

# Basic Equipment:
Sash = Equipment("Sash", "Head", "Wind", "Slash", 1, 1, 0, 0, 2, 2, "None", 0, 0, 0, 0, 0, 3, 0, 101)
 
# Equipment with conditions:
SpeedwingBoots = Equipment("Speedwing Boots", "Legs", "Wind", "Dodge", 0, 0, 1, 1, 5, 0, "Chance of perfect dodge", 10, 0, 5, 0, 0, 15, 15, 101)
 
# S-rank weapons:
SwordofPromisedVictory = Equipment("Sword of Promised Victory", "Weapon", "Light", "Slash", 1000, 1000, 1000, 1000, 1000, 1000, "Destroys all engaged. Cannot fail if user is virtuous", 100, 0, 0, 0, 0, 0, 0, 100)
SwordofSureDefeat = Equipment("Sword of Sure Defeat", "Weapon", "Dark", "Slash", 1000, 1000, 1000, 1000, 1000, 1000, "Destroys both the user and all enemies around them. Cannot fail if user is evil", 100, 0, 0, 0, 0, 0, 0, 100)
## (PLANT) - Neurotoxic Whip - Can attack from range 3. Does STR + MAG damage + afflicts poison. Enemy cannot move after encounter. Requires SKL > 100
## (EARTH) - Mountain Cleaver - Massive slab of iron that boosts STR + 50. Requires STR > 100 to equip, SKL > 100
## (ICE) - Frozen Falchion - Thick blade of unbreakable ice. After the battle, opponent cannot move, and SPD = 0.
## (FIRE) - Burning Blade - Sword of Flame. Attacks once, then again with Blaze Lv. 5. Requires STR > 50, MAG > 50, RES > 100, SKL > 50
## (WIND) - Storm Ruler - Calls upon a whirlwind to remove foes whose weight < user's. Requires STR > 50, MAG > 50, DEF > 50, RES > 50
## (LIGHTNING) - Chaos Breaker - Legendary blade that attacks once, then again with Bolt Lv. 5. Requires SPD > 50, STR > 50, MAG > 50
## (SLASH) - Ignis - Attacks with STR + MAG power, and spells gain +STR power when equipped. Requires STR > 50, MAG > 50, and SKL > 50
## (CLASH) - Melting Sword - Glows white-hot. Enemy weapons are destroyed upon engaging. Requires MAG > 100, RES > 100, STR > 50, SKL > 50
## (THROW) - Babylonian Lance - Infinite spears pierce the target. Hits between 5 and 10 times for (damage calculation / 5) damage each time. Requires MAG > 100 and SKL > 50
## (BASH) - Megaton Hammer - Shockwave does damage to all enemies within 2 squares of the attacked enemy. requires STR > 100
## (DODGE) - Rune Dagger - crit rate + 10% and user receives no damage from enemy counterattacks. Requires SPD > 100, SKL > 50, and user equip weight < 10
## (THRUST) - Needlepoint Rapier - User crit rate + 25% when attacking first. Requires SKL > 100
## (PARRY) - Curved Shield and Sword - User receives no damage when enemy strikes first. Requires SKL > 100
## (BLOCK) - Phalanx Shield and Spear - Blocks damage equal to (DEF / 2 or RES / 2, whichever is higher). Requires STR > 50, DEF > 50, SKL > 50
 
 
# Weapons:
## Blood-Magic Staff - uses HP to cast spells instead of MP
 
# Armor:
## Warding Shroud - Wearer takes damage to their MP bar instead of their HP bar until MP runs out
 
# S-Rank Armor:
## 
## (PLANT) - Crown of Thorns - Draws 10 HP per turn, but grants MAG +50. Grants immunity to PLANT magic. Requires DEF > 50 and RES > 50
## (EARTH) - Diamond Armor - Adds +100 DEF, but takes -50 RES and is very heavy. Requires STR > 100
## (ICE) - Nevermelt Ring - Boosts ICE magic by +100 MAG, but cannot equip any non-ICE equipment. Requires RES > 100
## (FIRE) - Forged Ring - Boosts FIRE magic by +100 MAG, but cannot equip any non-FIRE equipment. Requires RES > 100
## (WIND) - Thousand-League Boots - Boosts SPD by 100 and movement + 2, but requires weight < 10
## (LIGHTNING) - Lightningrod helm - 50% chance for user to be struck by lightning, dealing 30 HP damage but boosting STR, MAG, and SPD +50
## (DARK) - Soul-Draining Gauntlets - Drains 20HP per turn, but gain 30 HP for every enemy defeated. Grants +20 SKL, requires HP > 100 and morality <-50
## (LIGHT) - Angelic Armor - Boosts DEF + 50 and RES +50, but requires STR < 100 and morality > 50
## (SLASH) - Sash of Sight - boosts SLASH move crit rate +50%. Requires SKL > 50
## (CLASH) - Knee-Spikes - When CLASH activated, user has 50% chance to end clash by dealing a critical attack to the enemy. Requires STR > 50 and SKL > 50
## (THROW) - Steampowered Exoskeleton - A full suit of armor that grants extra torque, doubling the damage dealt by throws. Reduces SPD - 50 and reduces movement to 1, but increases attack range by 1. Requires STR > 50 and SKL > 50
## (BASH) - Torqued Gloves - Gloves bound with magical energy, which is released during attacks. Grants STR +50 and SPD +50, but requires weapon with weight > 50
## (DODGE) - Swift Slippers - Light slippers which increases dodge chance +40%. Requires SPD > 50 and SKL > 50
## (THRUST) - Mystic Lens - Identifies enemy's weak point, granting 100% crit. Curses the user, and drains 20 HP per turn.
## (PARRY) - Guided Hands - Grant no DEF or RES boosts, but has 50% chance to block and counter-attacks with *2 power. Drains 20HP per turn. Requires MAG > 100.
## (BLOCK) - Dragonscale Chestpiece - Grants DEF +50 and RES +50, but reduces SPD -50 and reduces movement by 1. Requires 50 STR and 50 MAG

 
#################################################################################################################################################
#  Game Classes                                                                                                                                 #
#################################################################################################################################################
 
class GridSpace:
    def __init__(self, occupant, movement_selected, attack_range_selected, cast_range_selected, spell_range_selected, technique_range_selected, visited):
        self.g_occupant = occupant
        self.g_movement_selected = movement_selected
        self.g_attack_range_selected = attack_range_selected
        self.g_cast_range_selected = cast_range_selected
        self.g_spell_range_selected = spell_range_selected
        self.g_technique_range_selected = technique_range_selected
        self.g_visited = visited
       
    # Getter Functions:
    def getOccupant(self):              return self.g_occupant
    def isVisited(self):                return self.g_visited
    def isInMovementRange(self):        return self.g_movement_selected
    def isInAttackRange(self):          return self.g_attack_range_selected
    def isInCastRange(self):            return self.g_cast_range_selected
    def isInSpellRange(self):           return self.g_spell_range_selected
    def isInTechniqueRange(self):       return self.g_technique_range_selected
    def isOccupied(self):               return 1 if (self.g_occupant != None) else 0
 
    # Setter Functions:
    def setOccupant(self, newoccupant): self.g_occupant = newoccupant
    def setVisited(self):               self.g_visited = 1
    def setInMovementRange(self):       self.g_movement_selected = 1
    def setInAttackRange(self):         self.g_attack_range_selected = 1
    def setInCastRange(self):           self.g_cast_range_selected = 1
    def setInSpellRange(self):          self.g_spell_range_selected = 1
    def setInTechniqueRange(self):      self.g_technique_range_selected = 1
 
    # Clear Functions:
    def clrOccupant(self):              self.g_occupant = None
    def clrVisited(self):               self.g_visited = 0
    def clrInMovementRange(self):       self.g_movement_selected = 0
    def clrInAttackRange(self):         self.g_attack_range_selected = 0
    def clrInCastRange(self):           self.g_cast_range_selected = 0
    def clrInSpellRange(self):          self.g_spell_range_selected = 0
    def clrInTechniqueRange(self):      self.g_technique_range_selected = 0
            
#################################################################################################################################################
#  Game Function Definitions                                                                                                                    #
#################################################################################################################################################
 
def printGrid(grid, ploc_i, ploc_j):
    if grid[ploc_i][ploc_j].getOccupant() != None:
        stat_screen_lines = ['    {:<6}'.format(grid[ploc_i][ploc_j].getOccupant().getName())
                            + '{:<6}'.format('Lv. ' + str(grid[ploc_i][ploc_j].getOccupant().getLevel())) + ' '
                            + '{:<10}'.format(grid[ploc_i][ploc_j].getOccupant().getClass()),
                            '    -------------------------',
                            '    HP: {:>3}'.format(grid[ploc_i][ploc_j].getOccupant().getCurrentHP()) + "/"
                            + '{:<3}'.format(grid[ploc_i][ploc_j].getOccupant().getTotalHP())
                            + '   MP: {:>3}'.format(grid[ploc_i][ploc_j].getOccupant().getCurrentMP()) + "/"
                            + '{:<3}'.format(grid[ploc_i][ploc_j].getOccupant().getTotalMP()),
                            '                             ',
                            '    STR: {:<3}'.format(grid[ploc_i][ploc_j].getOccupant().getCurrentSTR())
                            + '      MAG: {:<3}'.format(grid[ploc_i][ploc_j].getOccupant().getCurrentMAG()),
                            '    DEF: {:<3}'.format(grid[ploc_i][ploc_j].getOccupant().getCurrentDEF())
                            + '      RES: {:<3}'.format(grid[ploc_i][ploc_j].getOccupant().getCurrentRES()),
                            '    SPD: {:<3}'.format(grid[ploc_i][ploc_j].getOccupant().getCurrentSPD())
                            + '      SKL: {:<3}'.format(grid[ploc_i][ploc_j].getOccupant().getCurrentSKL()),
                            '                             ',
                            '    AFN: {:<5}'.format(grid[ploc_i][ploc_j].getOccupant().getAffinity())
                            + '    STY: {:<5}'.format(grid[ploc_i][ploc_j].getOccupant().getStyle()),
                            '                             ',
                            '    HLM: ' + grid[ploc_i][ploc_j].getOccupant().getArmorHead(),
                            '    BDY: ' + grid[ploc_i][ploc_j].getOccupant().getArmorTorso(),
                            '    GLV: ' + grid[ploc_i][ploc_j].getOccupant().getArmorArms(),
                            '    SHO: ' + grid[ploc_i][ploc_j].getOccupant().getArmorLegs(),
                            '    WPN: ' + grid[ploc_i][ploc_j].getOccupant().getWeapon(),
                            '                             ']
        if (grid[ploc_i][ploc_j].getOccupant().getTeam() == "Shining Force"):
            stat_screen_lines.append('    Exp: {:>7}'.format(grid[ploc_i][ploc_j].getOccupant().getCurrentEXP()) + ' / {:<7}'.format(grid[ploc_i][ploc_j].getOccupant().getNextLevelEXP()))
 
    os.system('cls'); line = 0; n = ((4 * gridsize) + 1); print("\n")
    if (state == "magiclevelmenu" or state == "usingmagic"):
        getSpellCastingRange()
    for i in range (0,gridsize):
        for x in range (0, n):
            print("-", end="", sep="")
        if (line % 2 == 0 and grid[ploc_i][ploc_j].getOccupant() != None and line < len(stat_screen_lines)): print (stat_screen_lines[line])
        else: print ("\n", end="", sep="")
        line += 1
        for j in range (0,gridsize):
            if grid[i][j].getOccupant() != None:
                OccupantId = grid[i][j].getOccupant().getId()
            else: OccupantId = 0
            if (grid[i][j].isInSpellRange() == 1):
                if (OccupantId in party or OccupantId in enemyparty): print ("|", u"\u2592", grid[i][j].getOccupant().getName()[0], u"\u2592", end="", sep="")
                else: print ("|", u"\u2592", u"\u2592", u"\u2592", end="", sep="")
            else:
                if (i == ploc_i and j == ploc_j):
                    if (OccupantId == 999): print ("|", "[", u"\u2588", "]", end="", sep="")
                    elif (OccupantId in party or OccupantId in enemyparty): print ("|[", grid[i][j].getOccupant().getName()[0], "]", end="", sep="")
                    elif (grid[i][j].isInMovementRange()): print ("|", "[", u"\u2591", "]", end="", sep="")
                    else: print ("|", "[ ]", end="", sep="")
                else:  
                    if (grid[i][j].isInCastRange()):
                        if (OccupantId == 999): print ("|", u"\u2591", u"\u2588", u"\u2591", end="", sep="")
                        elif (OccupantId in party or OccupantId in enemyparty): print ("|", u"\u2591", grid[i][j].getOccupant().getName()[0], u"\u2591", end="", sep="")
                        elif (grid[i][j].isInMovementRange()): print ("|", u"\u2591", u"\u2591", u"\u2591", end="", sep="")
                        else: print ("|", u"\u2591", u"\u2591", u"\u2591", end="", sep="")
                    else:
                        if (OccupantId == 999): print ("|", u"\u2588", u"\u2588", u"\u2588", end="", sep="")
                        elif (OccupantId in party or OccupantId in enemyparty): print ("|", grid[i][j].getOccupant().getNametag(), end="", sep="")
                        elif (grid[i][j].isInMovementRange()): print ("|", u"\u2591", u"\u2591", u"\u2591", end="", sep="")
                        else: print ("|", "   ", end="", sep="")
        print("|", end="", sep="")
        if (line % 2 == 1 and grid[ploc_i][ploc_j].getOccupant() != None and line < len(stat_screen_lines)): print (stat_screen_lines[line])
        else: print ("\n", end="", sep="")
        line += 1
    for x in range (0, n):
        print("-", end="", sep="")
    if (gridsize == 8):
        if (grid[ploc_i][ploc_j].getOccupant() != None):
            if (grid[ploc_i][ploc_j].getOccupant().getTeam() == "Shining Force"):
                print(stat_screen_lines[line], end="", sep="")
    print("\n")
    if (state == "movementmenu" or state == "magicmenu" or state == "magiclevelmenu"): printMenuByState(state)
    print("\n", dialogmessage);
 
def printWelcomeMessage():
    print ("""\n ======================================
           * SHINING FORCE *            
 --------------------------------------\n
An RPG.
Menu coming soon.
======================================""")
 
def printMenuByState(state):
    if (state == "movementmenu"): options = getMenuOptions("action")
    elif (state == "magicmenu"): options = getMenuOptions("magic")
    elif (state == "magiclevelmenu"): options = getMenuOptions("magiclevel")
    for i in range (0, len(options)):
        if menu_loc == i: print(" -> ", end="", sep="")
        else: print ("    ", end="", sep="")
        print (options[i], end="", sep="")
        if (state == "magiclevelmenu"):
            spellname = options[i][:-6]
            level = int(options[i][-1])
            print ("     MP Cost: ", chosenspell.getMPcost()[level - 1], "\n", end="", sep="")
        else:
            print ("\n", end="", sep="")
 
def getMenuOptions(menutype):
    options = []
    if (menutype == "action"):
        if canAttack(): options.append("Attack")
        if canUseMagic(): options.append("Use Magic")
        if canUseTechnique(): options.append("Use Technique")
        options.append("Stay")
    elif (menutype == "magic"):
        spells = grid[ploc_i][ploc_j].getOccupant().getKnownSpells()
        for i in range (0, len(spells)):
            options.append(spells[i][0:-5])
    elif (menutype == "magiclevel"):
        maxmagiclevel = int(selected[0].getKnownSpells()[magicchoice][-1]); count = 1
        while count < maxmagiclevel + 1:
            options.append(selected[0].getKnownSpells()[magicchoice][:-1] + str(count))
            count += 1
    return options

def getPassFailfromPercent(percent):
    return 1 if random.randint(1, 100) <= percent else 0
 
def canAttack():
    if (ploc_i - 1 >= 0):
        if (grid[ploc_i - 1][ploc_j].isOccupied() == 1):
            if (grid[ploc_i - 1][ploc_j].getOccupant().getTeam() == "Enemy"): return 1
    if (ploc_j - 1 >= 0):
        if (grid[ploc_i][ploc_j - 1].isOccupied() == 1):
            if (grid[ploc_i][ploc_j - 1].getOccupant().getTeam() == "Enemy"): return 1
    if (ploc_i + 1 <= gridsize - 1):
        if (grid[ploc_i + 1][ploc_j].isOccupied() == 1):
            if (grid[ploc_i + 1][ploc_j].getOccupant().getTeam() == "Enemy"): return 1
    if (ploc_j + 1 <= gridsize - 1):
        if (grid[ploc_i][ploc_j + 1].isOccupied() == 1):
            if (grid[ploc_i][ploc_j + 1].getOccupant().getTeam() == "Enemy"): return 1
    return 0
 
def canUseMagic():
    return 1 if (len(grid[temp_selected[1]][temp_selected[2]].getOccupant().getKnownSpells()) > 0) else 0
 
def canUseTechnique():
    return 1 if (len(grid[temp_selected[1]][temp_selected[2]].getOccupant().getKnownTechniques()) > 0) else 0
 
def attackCharacter(attacker, defender):
    damage = calculateDamage(attacker, defender)
    defender.setCurrentHP(defender.getCurrentHP() - damage)
    if (defender.getCurrentHP() <= 0):
        defender.setCurrentHP(0)
        grid[ploc_i][ploc_j].clrOccupant()

def getAreaByType(i, j, givenrange, giventype):
    if givenrange >= 0:
        givenrange -= 1
        if (givenrange >= 0):
            delta_i = [i, i - 1, i, i + 1, i]
            delta_j = [j, j, j - 1, j, j + 1]
        else:
            delta_i = [i]
            delta_j = [j]
        for x in range (0, len(delta_i)):
            if ((delta_i[x] >= 0 and delta_i[x] <= gridsize - 1) and (delta_j[x] >= 0 and delta_j[x] <= gridsize - 1)):
                if (giventype == "movement"):
                    if (grid[delta_i[x]][delta_j[x]].isOccupied() == 1):
                        if (grid[delta_i[x]][delta_j[x]].getOccupant().getTeam() == "Shining Force"):
                            getAreaByType(delta_i[x], delta_j[x], givenrange, "movement")
                    else:
                        grid[delta_i[x]][delta_j[x]].setInMovementRange()
                        getAreaByType(delta_i[x], delta_j[x], givenrange, "movement")
                elif (giventype == "spell"):
                    grid[delta_i[x]][delta_j[x]].setInSpellRange()
                    getAreaByType(delta_i[x], delta_j[x], givenrange, "spell")
                elif (giventype == "casting"):
                    grid[delta_i[x]][delta_j[x]].setInCastRange()
                    getAreaByType(delta_i[x], delta_j[x], givenrange, "casting")
                elif (giventype == "spelldamage"):                        
                    if (grid[delta_i[x]][delta_j[x]].isOccupied() == 1):
                        if (grid[delta_i[x]][delta_j[x]].getOccupant().getTeam() == "Enemy" and grid[delta_i[x]][delta_j[x]].isVisited() == 0):
                            magicdamage = calculateMagicDamage(selected[0], grid[delta_i[x]][delta_j[x]].getOccupant())
                            grid[delta_i[x]][delta_j[x]].getOccupant().setCurrentHP(grid[delta_i[x]][delta_j[x]].getOccupant().getCurrentHP() - magicdamage)
                            if (grid[delta_i[x]][delta_j[x]].getOccupant().getCurrentHP() <= 0):
                                grid[delta_i[x]][delta_j[x]].getOccupant().setCurrentHP(0)
                                grid[delta_i[x]][delta_j[x]].clrOccupant()
                            grid[delta_i[x]][delta_j[x]].setVisited()
                    getAreaByType(delta_i[x], delta_j[x], givenrange, "spelldamage")
  
def getMagicAreaofEffect():
    if magiclevelchoice != "None":
        name = magiclevelchoice[:-6]
        level = magiclevelchoice[-1]
        magicrange = chosenspell.getSpellRange()[int(level) - 1]
        getAreaByType(ploc_i, ploc_j, magicrange, "spell")
 
def magicAttackCharacter(attacker, magiclevelchoice):
    clearRangeFlagsByType("spell")
    if magiclevelchoice != "None":
        spellname = magiclevelchoice[:-6]
        level = int(magiclevelchoice[-1])
        MPcost = chosenspell.getMPcost()[level - 1]
        attacker.setCurrentMP(attacker.getCurrentMP() - MPcost)
        if (attacker.getCurrentMP() < 0): attacker.setCurrentMP(0)
        magicrange = chosenspell.getSpellRange()[level - 1]
        getAreaByType(ploc_i, ploc_j, magicrange, "spelldamage")
        clearRangeFlagsByType("visited")
 
def getSpellCastingRange():
    clearRangeFlagsByType("casting")
    magicleveloptions = getMenuOptions("magiclevel")
    for i in range (0, len(magicleveloptions)):
        if menu_loc == i:
            name = magicleveloptions[i][:-6]
            level = int(magicleveloptions[i][-1])
    spellcastrange = chosenspell.getCastRange()[level - 1]
    grid[temp_selected[1]][temp_selected[2]].setInCastRange()
    getAreaByType(temp_selected[1], temp_selected[2], spellcastrange, "casting")

def clearRangeFlagsByType(rangeflagtype):
    for i in range (0, gridsize):
        for j in range (0, gridsize):
            if (rangeflagtype == "movement"):
                if (grid[i][j].isInMovementRange() == 1):
                    grid[i][j].clrInMovementRange()
            elif (rangeflagtype == "casting"):
                if (grid[i][j].isInCastRange() == 1):
                    grid[i][j].clrInCastRange()
            elif (rangeflagtype == "spell"):
                if grid[i][j].isInSpellRange() == 1:
                    grid[i][j].clrInSpellRange()
            elif (rangeflagtype == "visited"):
                if grid[i][j].isVisited() == 1:
                    grid[i][j].clrVisited()

def calculateDamage(attacker, defender):
    return 10
 
def calculateMagicDamage(attacker, defender):
    return 2
 
#################################################################################################################################################
#  Initializations and Globally-Accessible Variables                                                                                            #
#################################################################################################################################################
 
state = "startnewbattle"
gridsize = 8                                        # 8 should be the minimum map size
selected = []; temp_selected = []
menu_loc = 0; dialogmessage = ""
magicchoice = "None"; magiclevelchoice = "None"; chosenspell = None;
printWelcomeMessage(); 
 
#################################################################################################################################################
#  Key Press Handling                                                                                                                           #
#################################################################################################################################################

while (state != "exiting"):
    pressedKey = msvcrt.getch()
    if pressedKey == b'q':   
        state = "exiting"
    elif pressedKey == b'K':   
        if (state == "playing" or state == "moving" or state == "attacking"):
            if (ploc_j != 0): ploc_j -= 1
        if (state == "usingmagic"):
            getSpellCastingRange()
            if (ploc_j != 0):
                if (grid[ploc_i][ploc_j - 1].isInCastRange()): ploc_j -= 1             
    elif pressedKey == b'M':
        if (state == "playing" or state == "moving" or state == "attacking"):
            if (ploc_j != (gridsize - 1)): ploc_j += 1
        if (state == "usingmagic"):
            getSpellCastingRange()
            if (ploc_j != (gridsize - 1)):
                if (grid[ploc_i][ploc_j + 1].isInCastRange()): ploc_j += 1                
    elif pressedKey == b'P':   
        if (state == "playing" or state == "moving" or state == "attacking"):
            if (ploc_i != (gridsize - 1)): ploc_i += 1
        if (state == "movementmenu"):
            menu_loc += 1
            if (menu_loc >= len(getMenuOptions("action"))): menu_loc = 0
        if (state == "magicmenu"):
            menu_loc += 1
            if (menu_loc >= len(getMenuOptions("magic"))): menu_loc = 0
        if (state == "magiclevelmenu"):
            menu_loc += 1
            if (menu_loc >= len(getMenuOptions("magiclevel"))): menu_loc = 0
        if (state == "usingmagic"):
            getSpellCastingRange()
            if (ploc_i != (gridsize - 1)):
                if (grid[ploc_i + 1][ploc_j].isInCastRange()): ploc_i += 1              
    elif pressedKey == b'H':   
        if (state == "playing" or state == "moving" or state == "attacking"):
            if (ploc_i != 0): ploc_i -= 1
        if (state == "movementmenu"):
            menu_loc -= 1
            if (menu_loc < 0): menu_loc = len(getMenuOptions("action")) - 1
        if (state == "magicmenu"):
            menu_loc -= 1
            if (menu_loc < 0): menu_loc = len(getMenuOptions("magic")) - 1
        if (state == "magiclevelmenu"):
            menu_loc -= 1
            if (menu_loc < 0): menu_loc = len(getMenuOptions("magiclevel")) - 1
        if (state == "usingmagic"):
            getSpellCastingRange()
            if (ploc_i != 0):
                if (grid[ploc_i - 1][ploc_j].isInCastRange()): ploc_i -= 1                
    elif pressedKey == b'z':
        if (state == "playing"):
            if (grid[ploc_i][ploc_j].isOccupied() == 1):
                if (grid[ploc_i][ploc_j].getOccupant().getTeam() == "Shining Force"):
                    selected = [grid[ploc_i][ploc_j].getOccupant(), ploc_i, ploc_j]
                    temp_selected = [grid[ploc_i][ploc_j].getOccupant(), ploc_i, ploc_j]
                    getAreaByType(ploc_i, ploc_j, selected[0].getCurrentMovement(), "movement")
                    state = "moving"
        elif (state == "moving"):
            menu_loc = 0
            if (grid[ploc_i][ploc_j].isInMovementRange() == 1):
                grid[ploc_i][ploc_j].setOccupant(selected[0])
                grid[selected[1]][selected[2]].clrOccupant()
                grid[selected[1]][selected[2]].setInMovementRange()
                temp_selected = [selected[0], ploc_i, ploc_j]
                state = "movementmenu"
            elif ((grid[ploc_i][ploc_j].isOccupied() == 1) and (grid[ploc_i][ploc_j].getOccupant().getId() == selected[0].getId())):
                state = "movementmenu"           
        elif (state == "movementmenu"):
            moveoptions = getMenuOptions("action")
            movechoice = moveoptions[menu_loc]
            if movechoice == "Attack":
                state = "attacking"
            elif movechoice == "Use Magic":
                state = "magicmenu"
                menu_loc = 0
            elif movechoice == "Use Special Attack":
                state = "usingtechnique"
            elif movechoice == "Stay":
                grid[selected[1]][selected[2]].clrOccupant()
                grid[ploc_i][ploc_j].setOccupant(selected[0])
                clearRangeFlagsByType("movement")
                selected = []
                state = "playing"             
        elif (state == "attacking"):
            if (grid[ploc_i][ploc_j].isOccupied() == 1):
                if (grid[ploc_i][ploc_j].getOccupant().getTeam() != "Shining Force"):
                    dialogmessage = str(selected[0].getName()) + " attacks!"
                    attackCharacter(selected[0], grid[ploc_i][ploc_j].getOccupant())
                    clearRangeFlagsByType("movement")
                    state = "playing"               
        elif (state == "magicmenu"):
            magicoptions = getMenuOptions("magic")
            magicchoice = menu_loc
            chosenspell = spells_dict[selected[0].getKnownSpells()[magicchoice][0:-6]]
            state = "magiclevelmenu"
            clearRangeFlagsByType("movement")
            menu_loc = 0;             
        elif (state == "magiclevelmenu"):
            magicleveloptions = getMenuOptions("magiclevel")
            magiclevelchoice = magicleveloptions[menu_loc]
            level = int(magiclevelchoice[-1])
            MPcost = chosenspell.getMPcost()[level - 1]
            if (MPcost <= selected[0].getCurrentMP()): state = "usingmagic"
            else: dialogmessage = "Not enough MP to cast this spell!"
        elif (state == "usingmagic"):
            dialogmessage = str(selected[0].getName()) + " casts " + magiclevelchoice + "!"
            magicAttackCharacter(selected[0], magiclevelchoice)
            selected = []; temp_selected = []; magicchoice = "None"; magiclevelchoice = "None"; chosenspell = None; menu_loc = 0;
            clearRangeFlagsByType("spell")
            clearRangeFlagsByType("casting")
            state = "playing"; 
    elif pressedKey == b'x':
        if (state == "moving"):
            selected = []
            clearRangeFlagsByType("movement")
            menu_loc = 0
            state = "playing"
        if (state == "movementmenu"):
            menu_loc = 0
            grid[ploc_i][ploc_j].setInMovementRange()
            grid[ploc_i][ploc_j].clrOccupant()
            grid[selected[1]][selected[2]].setOccupant(selected[0])
            ploc_i = selected[1]
            ploc_j = selected[2]
            state = "moving"
        if (state == "attacking"):                   
            menu_loc = 0
            ploc_i = temp_selected[1]
            ploc_j = temp_selected[2]
            state = "movementmenu"            
        if (state == "magicmenu"):
            menu_loc = 0
            ploc_i = temp_selected[1]
            ploc_j = temp_selected[2]
            state = "movementmenu"
        if (state == "magiclevelmenu"):
            clearRangeFlagsByType("casting")
            getAreaByType(selected[1], selected[2], selected[0].getCurrentMovement(), "movement")
            state = "magicmenu"
        if (state == "usingmagic"):
            ploc_i = temp_selected[1]
            ploc_j = temp_selected[2]
            clearRangeFlagsByType("movement")
            state = "magiclevelmenu"
           
#################################################################################################################################################
#  Game State Handling                                                                                                                           #
#################################################################################################################################################

    if (state == "startnewbattle"):
        grid = []
        for i in range (0, gridsize):
            grid.append([])
            for j in range (0, gridsize):
                grid[i].append(0)
        for i in range (0, gridsize):
            for j in range (0, gridsize):
                x = GridSpace(None, 0, 0, 0, 0, 0, 0)
                grid[i][j] = x
        state = "playing"       
      
        # Place Max in the bottom right, Anri in bottom middle, and enemies in the middle:
        grid[gridsize - 2][gridsize - 2].setOccupant(Max)
        grid[gridsize - 2][4].setOccupant(Anri)
        grid[3][3].setOccupant(Wolf_1)
        grid[4][4].setOccupant(Wolf_2)
        party.append(Max.getId()); party.append(Anri.getId())
        enemyparty.append(Wolf_1.getId()); enemyparty.append(Wolf_2.getId())
 
    if (state == "playing" or state == "moving" or state == "movementmenu" or state == "attacking" or state == "magicmenu" or state == "magiclevelmenu" or state == "usingmagic"):   
        if (state == "usingmagic"):
            getMagicAreaofEffect()           
        printGrid(grid, ploc_i, ploc_j)
        clearRangeFlagsByType("spell"); dialogmessage = ""; spellcastingaread = []
