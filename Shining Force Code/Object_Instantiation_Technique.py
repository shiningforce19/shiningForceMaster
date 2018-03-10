from Class_Definition_Technique import Technique
  
#################################################################################################################################################
#  Technique Instantiation                                                                                                                              #
#################################################################################################################################################
 
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

