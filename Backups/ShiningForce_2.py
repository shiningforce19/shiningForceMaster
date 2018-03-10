#
#
# To Do:
#
#
# Stat Bonus 1-5: Very poor, poor, neutral, good, very good. Then randomize a number from them
# Stat growths 1-5: Very poor, poor, neutral, good, very good. Then randomize a number from them.
# #### MAKE SURE THIS NUMBER IS KEPT THE SAME FOR THE ENTIRE PLAYTHROUGH
#
#
# Figure out stat totals for classes and characters. They don't have to be equal, but it will help show who needs more strengths
# Make special weapons for each class
############################################################################################################################




import random, msvcrt, os, copy, time

from Class_Definition_Affinity import Affinity
from Class_Definition_Character import Character
from Class_Definition_Class import Class
from Class_Definition_Equipment import Equipment
from Class_Definition_GridSpace import GridSpace
from Class_Definition_Spell import Spell
from Class_Definition_Style import Style
from Class_Definition_Technique import Technique

import Object_Instantiation_Affinity
import Object_Instantiation_Character
import Object_Instantiation_Class
import Object_Instantiation_Equipment
import Object_Instantiation_Spell
import Object_Instantiation_Style
import Object_Instantiation_Technique
 
global ploc_i; ploc_i = 0
global ploc_j; ploc_j = 0
global party; party = []
global enemyparty; enemyparty = []
   
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
