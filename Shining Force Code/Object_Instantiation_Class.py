from Class_Definition_Class import Class
  
#################################################################################################################################################
#  Class Instantiation                                                                                                                              #
#################################################################################################################################################

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
#LvlDict_Dryad = {5:"Overgrowth Lv. 1", 8:"Heal Lv. 1", 10:"Overgrowth Lv. 2", 13:"Heal Lv.2", 15:"Overgrowth Lv. 3", 18:"Heal Lv. 3", 20: "Amplify Lv. 1"}
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
#Dryad = Class("Dryad", "Floromancer", "None", "Plant", "None",          2, 3, 3, 3, 2, 2, 4, 4, 0, 2, 3, 3, 3, 2, 2, 4, 3, ["artifact", "sword"], "A practitioner of plant magic. Able to control nature to inflict pain on their enemies.", LvlDict_Dryad)
Floromancer = Class("Floromancer", "None", "Plant", "None",             3, 4, 3, 3, 3, 2, 4, 5, 0, 3, 4, 3, 3, 3, 2, 4, 4, ["artifact", "sword", "stave"], "A skilled practitioner of plant magic. Versatile and dangerous.", LvlDict_Floromancer)
                                                                      # HP MP ST MG DF RS SP SK MV HP MP ST MG DF RS SP SK
##Thief = Class("Thief", "Rogue", "None", "Dodge",                        1, 2, 3, 1, 1, 2, 4, 4, 1, 2, 2, 3, 1, 1, 2, 4, 4, ["sword"], "A devilish trickster. Good at dodging and finding enemy weak points.", LvlDict_Thief)
##Rogue = Class("Rogue", "None", "None", "Dodge",                         2, 3, 4, 1, 1, 2, 5, 5, 1, 2, 3, 3, 1, 1, 2, 5, 5, ["sword", "ranged"], "A seasoned trickster with sharp attacks and sharp wit.", LvlDict_Rogue)
##Mercenary = Class("Mercenary", "Veteran", "None", "Slash",              2, 2, 3, 1, 3, 2, 2, 3, 0, 3, 2, 3, 1, 3, 2, 2, 3, ["sword", "axe"], "A mercenary who loves money.", LvlDict_Mercenary)
##Verteran = Class("Veteran", "None", "None", "Slash",                    3, 2, 4, 1, 4, 2, 2, 4, 0, 4, 2, 4, 1, 4, 2, 2, 4, ["sword", "axe", "ranged"], "A hardened veteran who has amassed skills and wealth on the battlefield.", LvlDict_Veteran)
##Swordsman = Class("Swordsman", "Swordmaster", "None", "Clash",          1, 1, 3, 1, 2, 2, 3, 4, 0, 2, 1, 3, 1, 2, 2, 3, 4, ["sword"], "A nimble warrior devoted to the sword.", LvlDict_Swordsman)
##Swordmaster = Class("Swordmaster", "None", "None", "Clash",             2, 2, 4, 1, 2, 2, 4, 5, 0, 2, 3, 4, 1, 3, 2, 5, 5, ["sword"], "An experienced warrior who has mastered the art of the blade.", LvlDict_Swordmaster)
##Warrior = Class("Warrior", "Berseker", "None", "Bash",                  2, 1, 3, 0, 3, 3, 2, 1, 0, 3, 1, 4, 0, 3, 3, 3, 1, ["axe"], "A ruffian with a bloodlust.", LvlDict_Warrior)
##Berserker = Class("Berserker", "None", "None", "Bash",                  3, 2, 5, 0, 4, 3, 3, 2, 0, 3, 2, 5, 0, 4, 3, 3, 2, ["axe"], "A master of axes, crazed by battle.", LvlDict_Berserker)
##Knight = Class("Knight", "General", "None", "Block",                    4, 1, 3, 0, 5, 0, 1, 1, 0, 4, 1, 3, 0, 5, 0, 1, 2, ["lance", "axe"], "A cautious, sturdy fighter who packs a punch.", LvlDict_Knight)
##General = Class("General", "None", "None", "Block",                     5, 1, 3, 0, 5, 0, 1, 2, 0, 5, 1, 4, 0, 5, 0, 1, 2, ["lance", "axe", "sword"], "A walking fortress of pain.", LvlDict_General)
##Spearman = Class("Spearman", "Lancer", "None", "Throw",                 3, 2, 3, 1, 2, 2, 3, 2, 0, 3, 2, 3, 1, 2, 2, 3, 2, ["lance"], "A lithe fighter devoted to the lance.", LvlDict_Spearman)
##Lancer = Class("Lancer", "None", "None", "Throw",                       4, 3, 4, 2, 3, 3, 4, 3, 0, 4, 3, 4, 2, 3, 3, 4, 3, ["lance"], "A smart warrior who has mastered spear combat.", LvlDict_Lancer)
##Duelist = Class("Duelist", "None", "None", "Parry",                     2, 2, 2, 1, 1, 2, 3, 4, 0, 2, 2, 2, 1, 1, 2, 3, 4, ["sword", "lance"], "A rough fighter who likse to live dangerously.", LvlDict_Duelist)
##Duelmaster = Class("Duelmaster", "None", "None", "Parry",               3, 3, 3, 1, 2, 2, 4, 5, 0, 3, 3, 4, 1, 2, 2, 5, 5, ["sword", "lance", "artifact"], "A polished master of one-on-one combat.", LvlDict_Duelmaster)
##Cavalier = Class("Cavalier", "Paladin", "None", "Thrust",               3, 1, 4, 1, 1, 2, 2, 1, 2, 3, 1, 4, 1, 2, 2, 3, 1, ["sword", "lance"], "A spry warrior who does battle atop their steed.", LvlDict_Cavalier)
##Paladin = Class("Paladin", "None", "None", "Thrust",                    4, 2, 5, 2, 2, 2, 3, 2, 2, 4, 2, 5, 2, 2, 2, 3, 1, ["sword", "lance", "stave"], "A hardened warrior who conquers the field with their mount.", LvlDict_Paladin)
##                                                                      # HP MP ST MG DF RS SP SK MV HP MP ST MG DF RS SP SK
##Crusader = Class("Crusader", "Holy Knight", "Light", "None",            4, 3, 2, 2, 3, 4, 2, 2, 0, 4, 3, 2, 2, 3, 4, 2, 2, ["sword", "stave"], "A warrior who uses light magic.", LvlDict_Crusader)
##HolyKnight = Class("Holy Knight", "None", "Light", "None",              5, 4, 3, 3, 3, 5, 2, 3, 0, 5, 4, 3, 3, 3, 5, 2, 3, ["sword", "stave", "lance"], "A strong warrior guided by light magic.", LvlDict_HolyKnight)
##StormCaller = Class("Storm Caller", "Mage General", "Lightning", "None",1, 2, 1, 2, 1, 3, 2, 3, 0, 1, 2, 1, 2, 1, 3, 2, 3, ["artifact"], "A weak fighter who tries to call lightning from the heavens.", LvlDict_StormCaller)
##MageGeneral = Class("Mage General", "None", "Lightning", "None",        3, 5, 3, 5, 3, 5, 2, 4, 0, 3, 5, 3, 5, 3, 5, 2, 4, ["artifact", "sword", "stave"], "A fiercesome tactician with extreme magical capabilities.", LvlDict_MageGeneral)
##Druid = Class("Druid", "Dark Conqueror", "Dark", "None",                2, 3, 2, 3, 1, 3, 1, 4, 0, 2, 3, 2, 3, 1, 3, 1, 4, ["artifact", "lance"], "A warrior who uses dark magic.", LvlDict_Druid) 
##DarkConqueror = Class("Dark Conqueror", "None", "Dark", "None",         3, 4, 4, 3, 3, 4, 3, 5, 0, 3, 4, 4, 3, 3, 4, 3, 5, ["artifact", "lance", "axe"], "A terrifying warrior who uses their dark knowledge for conquest.", LvlDict_DarkConqueror)
##Poisoner = Class("Poisoner", "Assassin", "Plant", "None",               2, 3, 1, 2, 2, 3, 2, 4, 0, 2, 3, 1, 2, 2, 3, 2, 4, ["artifact"], "An unassuming horticulturist skilled in poisons.", LvlDict_Poisoner)
##Assassin = Class("Assassin", "None", "Plant", "None",                   3, 4, 4, 2, 2, 4, 5, 5, 1, 3, 4, 4, 2, 2, 4, 5, 5, ["artifact", "sword"], "A shadowy assassin that can decimate opponents.", LvlDict_Assassin)
##Falconer = Class("Falconer", "Sky Rider", "Wind", "None",               2, 2, 2, 3, 2, 4, 4, 4, 2, 2, 2, 2, 3, 2, 4, 4, 4, ["lance", "ranged"], "Fights from atop their large falcon companion.", LvlDict_Falconer)
##SkyRider = Class("Sky Rider", "None", "Wind", "None",                   3, 3, 3, 3, 3, 4, 5, 4, 3, 3, 3, 3, 3, 3, 4, 5, 4, ["lance", "ranged", "axe"], "Masters of all airborn beasts, they guide the wind itself.", LvlDict_SkyRider)
##Trenchman = Class("Trenchman", "Trapmaster", "Earth", "None",           2, 2, 2, 3, 4, 3, 1, 5, 0, 2, 2, 2, 3, 4, 3, 1, 5, ["axe"], "Calculating movers of earth.", LvlDict_Trenchman)
##Trapmaster = Class("Trapmaster", "None", "Earth", "None",               3, 3, 3, 4, 5, 3, 2, 5, 0, 3, 3, 3, 4, 5, 3, 2, 5, ["axe", "ranged"], "Fierce fighters and trap-makers.", LvlDict_Trapmaster)
##FlameKnight = Class("Flame Knight", "Lord of Flame", "Fire", "None",    3, 3, 3, 2, 2, 2, 1, 2, 0, 3, 3, 3, 2, 2, 2, 1, 2, ["sword"], "Diligent keepers of the flame of battle.", LvlDict_FlameKnight)
##LordofFlame = Class("Lord of Flame", "None", "Fire", "None",            4, 4, 4, 3, 3, 2, 2, 2, 0, 4, 4, 4, 3, 3, 2, 2, 2, ["sword", "axe"], "Masters of fire and physical combat.", LvlDict_LorofFlame)
##FrostKnight = Class("Frost Knight", "Lord of Frost", "Ice", "None",     3, 3, 3, 2, 2, 2, 1, 2, 0, 3, 3, 3, 2, 2, 2, 1, 2, ["lance"], "Diligent defenders of ice magic.", LvlDict_FrostKnight)
##LordofFrost = Class("Lord of Frost", "None", "Ice", "None",             4, 4, 4, 3, 3, 2, 2, 2, 0, 4, 4, 4, 3, 3, 2, 2, 2, ["lance", "stave"], "Masters of ice and physical combat.", LvlDict_LordofFrost)










