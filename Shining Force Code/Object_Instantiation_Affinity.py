from Class_Definition_Affinity import Affinity
  
#################################################################################################################################################
#  Affinity Instantiation                                                                                                                              #
#################################################################################################################################################
 
Light = Affinity("Light", 0, 1, ["Plant", "Lightning"])
Lightning = Affinity("Lightning", 1, 0, ["Light", "Wind"])
Wind = Affinity("Wind", 0, 1, ["Ice", "Lightning"])
Ice = Affinity("Ice", 1, 0, ["Wind", "Fire"])
Fire = Affinity("Fire", 0, 1, ["Ice", "Dark"])
Dark = Affinity("Dark", 1, 0, ["Fire", "Earth"])
Earth = Affinity("Earth", 0, 1, ["Dark", "Plant"])
Plant = Affinity("Plant", 1, 0, ["Earth", "Light"])
