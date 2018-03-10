from Class_Definition_Equipment import Equipment
  
#################################################################################################################################################
#  Equipment Instantiation                                                                                                                              #
#################################################################################################################################################
 
#### Equipment(self, name, equipment_type, sub_type, actionrange, affinity, style, STRbonus, MAGbonus, DEFbonus, RESbonus,
#              SPDbonus, SKLbonus, effect, effectchance, STRrequirement, MAGrequirement, DEFrequirement, RESrequirement,
#              SPDrequirement, SKLrequirement, moralityrequirement, weight, description) 

# Basic Equipment:
#Sash = Equipment("Sash", "Head", "Wind", "Slash", 1, 1, 0, 0, 2, 2, "None", 0, 0, 0, 0, 0, 3, 0, 101)
 
# Equipment with conditions:
#SpeedwingBoots = Equipment("Speedwing Boots", "Legs", "Wind", "Dodge", 0, 0, 1, 1, 5, 0, "Chance of perfect dodge", 10, 0, 5, 0, 0, 15, 15, 101)
 
# S-rank weapons:
#SwordofPromisedVictory = Equipment("Sword of Promised Victory", "Weapon", "Light", "Slash", 1000, 1000, 1000, 1000, 1000, 1000, "Destroys all engaged. Cannot fail if user is virtuous", 100, 0, 0, 0, 0, 0, 0, 100)
#SwordofSureDefeat = Equipment("Sword of Sure Defeat", "Weapon", "Dark", "Slash", 1000, 1000, 1000, 1000, 1000, 1000, "Destroys both the user and all enemies around them. Cannot fail if user is evil", 100, 0, 0, 0, 0, 0, 0, 100)
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
