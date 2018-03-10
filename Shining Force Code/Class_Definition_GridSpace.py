#################################################################################################################################################
#  GridSpace Class                                                                                                                              #
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



    
