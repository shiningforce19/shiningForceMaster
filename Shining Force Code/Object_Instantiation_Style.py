from Class_Definition_Style import Style
  
#################################################################################################################################################
#  Style Instantiation                                                                                                                              #
#################################################################################################################################################
 
Slash = Style("Slash", 1, 0, ["Parry", "Clash"])
Clash = Style("Clash", 0, 1, ["Slash", "Bash"])
Bash = Style("Bash", 1, 0, ["Clash", "Block"])
Block = Style("Block", 0, 1, ["Bash", "Throw"])
Throw = Style("Throw", 1, 0, ["Block", "Dodge"])
Dodge = Style("Dodge", 0, 1, ["Throw", "Thrust"])
Thrust = Style("Thrust", 1, 0, ["Dodge", "Parry"])
Parry = Style("Parry", 0, 1, ["Thrust", "Slash"])
