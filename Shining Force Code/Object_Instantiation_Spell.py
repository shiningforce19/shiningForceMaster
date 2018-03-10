from Class_Definition_Spell import Spell
  
#################################################################################################################################################
#  Spell Instantiation                                                                                                                              #
#################################################################################################################################################
 
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
DragonBreath = Spell("Dragon Breath", [5, 10, 15, 20, 30], [10, 20, 30, 40, 50], [], "None", [2, 2, 3, 3, 3,], [0, 1, 1, 2, 2], "No Effect", [100, 100, 100, 100, 100], "Enemies", "Ancient Mana erupts from the mouth of a dragon.") 

spells_dict = {}; spells_dict["Shine"] = Shine; spells_dict["Freeze"] = Freeze; spells_dict["Blaze"] = Blaze; spells_dict["Bolt"] = Bolt; spells_dict["Nightshade"] = Nightshade;
spells_dict["Gale"] = Gale; spells_dict["Quake"] = Quake; spells_dict["Overgrowth"] = Overgrowth; spells_dict["Amplify"] = Amplify; spells_dict["Nullify"] = Nullify;
spells_dict["Strengthen"] = Strengthen; spells_dict["Weaken"] = Weaken; spells_dict["Harden"] = Harden; spells_dict["Soften"] = Soften; spells_dict["Quicken"] = Quicken;
spells_dict["Heal"] = Heal; spells_dict["Dark Heal"] = DarkHeal; spells_dict["Aura"] = Aura; spells_dict["Dark Aura"] = DarkAura; spells_dict["Energy Transfer"] = EnergyTransfer;
spells_dict["Physical Swap"] = PhysicalSwap; spells_dict["Magical Swap"] = MagicalSwap; spells_dict["Dual Swap"] = DualSwap; spells_dict["Power Within"] = PowerWithin;
spells_dict["Protection Within"] = ProtectionWithin; spells_dict["Restore"] = Restore; spells_dict["Divine Judgement"] = DivineJudgement; spells_dict["Sheer Cold"] = SheerCold;
spells_dict["Overheat"] = Overheat; spells_dict["Electric Reflexes"] = ElectricReflexes; spells_dict["Unholy Drain"] = UnholyDrain; spells_dict["Galeforce"] = Galeforce;
spells_dict["Magical Mud"] = MagicalMud; spells_dict["Aromatherapy"] = Aromatherapy; spells_dict["Dragon Breath"] = DragonBreath;




