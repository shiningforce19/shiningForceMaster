from Class_Definition_Sprite import Sprite

import Asset_Instantiation_Sprites as n
  
#################################################################################################################################################
#  Sprite Instantiation                                                                                                                         #
#################################################################################################################################################

max_sprite_dict_S = {'MAX_S_1': n.sprites[0], 'MAX_S_2': n.sprites[1]}
max_sprite_dict_W = {'MAX_W_1': n.sprites[2], 'MAX_W_2': n.sprites[3]}
max_sprite_dict_N = {'MAX_N_1': n.sprites[4], 'MAX_N_2': n.sprites[5]}
max_sprite_dict_E = {'MAX_E_1': n.sprites[6], 'MAX_E_2': n.sprites[7]}

bat_sprite_dict_S = {'BAT_S_1': n.sprites[8], 'BAT_S_2': n.sprites[9]}
bat_sprite_dict_W = {'BAT_W_1': n.sprites[10], 'BAT_W_2': n.sprites[11]}
bat_sprite_dict_N = {'BAT_N_1': n.sprites[12], 'BAT_N_2': n.sprites[13]}
bat_sprite_dict_E = {'BAT_E_1': n.sprites[14], 'BAT_E_2': n.sprites[15]}

Max_Sprite = Sprite(max_sprite_dict_S, max_sprite_dict_W, max_sprite_dict_N, max_sprite_dict_E,)
Bat_Sprite_1 = Sprite(bat_sprite_dict_S, bat_sprite_dict_W, bat_sprite_dict_N, bat_sprite_dict_E,)
Bat_Sprite_2 = Sprite(bat_sprite_dict_S, bat_sprite_dict_W, bat_sprite_dict_N, bat_sprite_dict_E,)


