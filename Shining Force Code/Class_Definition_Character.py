import random
  
#################################################################################################################################################
#  Character Class                                                                                                                              #
#################################################################################################################################################
 
class Character:
    def __init__(self, charid, name, nametag, HP, MP, STR, MAG, DEF, RES, SPD, SKL, movement, HPgrowth, MPgrowth, STRgrowth, MAGgrowth,
                 DEFgrowth, RESgrowth, SPDgrowth, SKLgrowth, affinity, style, level, charclass, knownspells, knowntechniques,
                 head, torso, arms, legs, weapon, weaponproficiencies, statusafflictions, team, sprite):
        
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
        self.c_sprite = sprite                              # Sprite object instantiation
 
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
    def getSprite(self):            return self.c_sprite
 
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
    def increaseProficiency(self, WPNtype):   self.c_statusafflictions[WPNtype] += 1
    def setSprite(self, sprite):              self.c_sprite = sprite
    
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


 
