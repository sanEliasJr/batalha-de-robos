from game_mod import Multiplayer, Solo, Torre, teste
from strings import *


print(Menus.game_cover)
input(Menus.press_any_key)

option = True
while(option):
    
    print(Menus.menu_options)
    mode = int(input("> "))        
        
    if mode == 1:
        Solo.play()
    elif mode == 2:
        Multiplayer.play()
    elif mode == 3:
        Torre.play()
    elif mode == 4: 
        teste.play_teste()
    elif mode == 5:
        exit()