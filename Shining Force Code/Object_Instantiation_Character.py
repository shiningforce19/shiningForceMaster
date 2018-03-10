import random, os, copy, time

from Class_Definition_Character import Character
import Asset_Instantiation_Sprites as n
from Object_Instantiation_Sprite import Max_Sprite
from Object_Instantiation_Sprite import Bat_Sprite

from Object_Instantiation_Class import Lord

  
#################################################################################################################################################
#  Character Instantiation                                                                                                                              #
#################################################################################################################################################
 
# Define Characters:                        HP MP ST MG DF RS SP SK MV HP MP ST MG DF RS SP SK
Max = Character (1, "Max", "MAX",           7, 7, 6, 6, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, "None", "None", 1, Lord, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force", Max_Sprite)

# Define Enemy Characters:                  HP MP ST MG DF RS SP SK MV HP MP ST MG DF RS SP SK
Bat_1 = Character (101, "Bat", "BAT",       10,   0,   4,  0,  2,  2,  3,  0,  5, 0, 0, 0, 0, 0, 0, 0, 0, "None", "None", 1, None, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Enemy", Bat_Sprite)
Bat_2 = Character (101, "Bat", "BAT",       10,   0,   4,  0,  2,  2,  3,  0,  5, 0, 0, 0, 0, 0, 0, 0, 0, "None", "None", 1, None, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Enemy", Bat_Sprite)










##Kaname = Character (2, "Kaname", "KAN",     6, 6, 6, 5, 4, 4, 3, 1, 6, 4, 3, 5, 4, 3, 3, 2, 1, "None", "None", 1, Manakete, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Donnel = Character (3, "Donnel", "DNL",     5, 1, 2, 2, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, "None", "None", 1, Villager, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Sabrina = Character (4, "Sabrina", "SAB",   6, 6, 2, 5, 2, 5, 2, 8, 5, 2, 4, 1, 4, 2, 3, 2, 5, "Dark", "None", 1, Shaman, ["Nightshade Lv. 1", "Dark Heal Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Tao = Character (5, "Tao", "TAO",           6, 5, 3, 8, 1, 4, 4, 2, 5, 1, 4, 2, 5, 1, 2, 1, 3, "Fire", "None", 1, FireMage, ["Blaze Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Brock = Character (6, "Brock", "BRK",       7, 5, 5, 5, 4, 4, 1, 2, 5, 4, 3, 4, 4, 4, 3, 1, 1, "Earth", "None", 1, EarthMage, ["Quake Lv. 1", "Power Within Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Iris = Character (7, "Iris", "IRS",         6, 6, 2, 6, 2, 6, 7, 6, 5, 2, 4, 1, 4, 1, 2, 5, 3, "Wind", "None", 1, WindMage, ["Gale Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Anri = Character (8, "Anri", "ANR",         6, 8, 2, 8, 2, 3, 3, 2, 5, 2, 4, 1, 5, 1, 2, 2, 3, "Ice", "None", 1, IceMage, ["Heal Lv. 1", "Freeze Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Xander = Character (9, "Xander", "XND",     6, 6, 1, 9, 1, 1, 8, 5, 5, 2, 5, 2, 5, 1, 1, 4, 2, "Lightning", "None", 1, Blitzer, ["Bolt Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force") 
##Khris = Character (10, "Khris", "KRS",      7, 8, 1, 5, 2, 5, 4, 6, 5, 4, 4, 1, 3, 2, 4, 3, 3, "Light", "None", 1, Monk, ["Heal Lv. 1", "Strengthen Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force") 
##Elise = Character (11, "Elise", "ELS",      6, 7, 2, 6, 4, 7, 6, 5, 5, 3, 4, 2, 3, 3, 4, 4, 2, "Plant", "None", 1, Dryad, ["Overgrowth Lv. 1", "Energy Transfer Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Raven = Character (12, "Raven", "RVN",      6, 2, 5, 1, 3, 3, 8, 7, 6, 2, 1, 4, 1, 2, 2, 4, 4, "None", "Dodge", 1, Thief, [], ["Quickstep Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Gregor = Character (13, "Gregor", "GRG",    8, 2, 8, 1, 5, 2, 4, 4, 5, 4, 2, 5, 1, 3, 1, 3, 2, "None", "Slash", 1, Mercenary, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Mark = Character (14, "Mark", "MRK",        6, 1, 6, 1, 5, 4, 6, 6, 5, 3, 1, 4, 1, 4, 2, 3, 4, "None", "Clash", 1, Swordsman, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Bernard = Character (15, "Bernard", "BRN",  6, 2, 9, 1, 7, 2, 2, 3, 5, 2, 2, 5, 1, 4, 1, 1, 2, "None", "Bash", 1, Warrior, [], ["Overexertion Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Wallace = Character (16, "Wallace", "WLC",  9, 2, 8, 1, 9, 2, 1, 2, 4, 5, 1, 5, 1, 5, 1, 1, 2, "None", "Block", 1, Knight, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Ephraim = Character (17, "Ephraim", "EPH",  7, 3, 5, 2, 2, 5, 4, 4, 5, 3, 3, 3, 2, 1, 3, 3, 3, "None", "Throw", 1, Spearman, [], ["Assist Ally Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")  
##Lucina = Character (18, "Lucina", "LUC",    6, 5, 5, 3, 3, 1, 6, 7, 5, 2, 2, 3, 2, 1, 2, 4, 5, "None", "Parry", 1, Duelist, [], ["Observe Lv. 1", "Riposte Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Flex = Character (19, "Flex", "FLX",        7, 2, 6, 1, 4, 3, 4, 3, 6, 4, 1, 3, 1, 3, 2, 3, 2, "None", "Thrust", 1, Cavalier, [], ["Defend Ally Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Quentin = Character (20, "Quentin", "QNT",  6, 2, 6, 2, 2, 4, 5, 7, 5, 2, 2, 5, 1, 2, 2, 4, 4, "None", "None", 1, Archer, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Cordelia = Character (21, "Cordelia", "COR",7, 4, 4, 4, 2, 7, 6, 4, 7, 4, 3, 2, 2, 1, 4, 3, 3, "None", "None", 1, PegasusRider, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Chrom = Character (22, "Chrom", "CHR",      6, 6, 5, 5, 4, 4, 3, 2, 5, 4, 3, 3, 3, 3, 3, 1, 1, "Light", "Slash", 1, Crusader, ["Shine Lv. 1"], ["Rend Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Nino = Character (23, "Nino", "NIN",        6, 9, 1, 1, 1, 1, 2, 3, 5, 5, 5, 4, 4, 3, 3, 3, 3, "Lightning", "None", 1, StormCaller, ["Bolt Lv. 1"], ["Assist Ally Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Leo = Character (24, "Leo", "LEO",          6, 5, 5, 4, 3, 5, 1, 6, 5, 2, 3, 4, 4, 3, 3, 1, 4, "Dark", "None", 1, Druid, ["Dark Heal Lv. 1", "Nullify"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")         
##Jaffar = Character (25, "Jaffar", "JFR",    6, 4, 6, 2, 1, 2, 7, 9, 6, 2, 2, 4, 1, 1, 1, 4, 5, "Plant", "None", 1, Poisoner, [],["Overexertion Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##V.Swift = Character (26, "V. Swift", "VSW", 6, 3, 5, 4, 6, 2, 6, 6, 7, 3, 2, 4, 2, 4, 2, 4, 3, "Wind", "None", 1, Falconer, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Loggs = Character (27, "Loggs", "LOG",      8, 5, 4, 4, 5, 4, 1, 2, 5, 3, 3, 3, 3, 4, 4, 1, 1, "Earth", "None", 1, Trenchman, ["Quake Lv. 1"], ["Brace Lv. 1"], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Thoros = Character (28, "Thoros", "THO",    7, 5, 6, 6, 2, 2, 3, 3, 5, 3, 3, 4, 4, 2, 2, 2, 2, "Fire", "None", 1, FlameKnight, ["Blaze Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##Miriel = Character (29, "Miriel", "MIR",    7, 5, 3, 3, 5, 5, 4, 3, 5, 3, 3, 2, 2, 4, 4, 3, 2, "Ice", "None", 1, FrostKnight, ["Freeze Lv. 1"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Shining Force")
##
### Enemy Characters:
##                                                  # HP    MP   ST  MG  DF  RS  SP  SK  MV HP MP ST MG DF RS SP SK
##Wolf_1 = Character (51, "Wolf", "WLF",              10,   0,   4,  0,  2,  2,  3,  0,  5, 0, 0, 0, 0, 0, 0, 0, 0, "Ice", "None", 1, None, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Enemy")
##Wolf_2 = Character (52, "Wolf", "WLF",              10,   0,   4,  0,  2,  2,  3,  0,  5, 0, 0, 0, 0, 0, 0, 0, 0, "Ice", "None", 1, None, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Enemy")
##Wolf_3 = Character (53, "Wolf", "WLF",              10,   0,   4,  0,  2,  2,  3,  0,  5, 0, 0, 0, 0, 0, 0, 0, 0, "Ice", "None", 1, None, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Enemy")
##Hydra = Character (900, "Hydra", "HYD",             500,  100, 50, 50, 50, 50, 40, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, "None", "None", 50, None, [], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Enemy")
##ElementalHydra = Character (901, "ElementalHydra",  1000, 500, 90, 90, 70, 70, 50, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, "All", "None", 100, None, ["Shine Lv. 5", "Freeze Lv. 5", "Blaze Lv. 5", "Bolt Lv. 5", "Gale Lv. 5", "Nightshade Lv. 5", "Quake Lv. 5", "Overgrowth Lv. 5"], [], "None", "None", "None", "None", "None", {"sword":"E", "lance":"E", "axe":"E", "artifact":"E", "ranged":"E", "stave":"E"}, [], "Enemy")


