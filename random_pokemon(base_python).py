import sys
import time
import random


print ('Random Pokemon Generator by Chris "Eva_Fan" Trace')
print ('----------')
# This is the base version of the script that uses basic python libraries and no 3rd party modules.

#An array that contains a list of pokemon, that will output a random variable when called.
def Pokemon():

    Pokemon_list = ['Bulbasaur','Charmander','Squirtle','Pikachu','Pidgey','Rattata','Sandshrew','Clefairy','Vulpix','Jigglypuff','Zubat','Diglett','Meowth','Magikarp','Psyduck','Gengar','Eevee','Hitmonchan','Snorlax','Wobbuffet']  
    
    color_code = "\033[33m" #ANSI escape_code to set the text color to yellow.
    return "This pokeball contains... " + color_code + random.choice(Pokemon_list) +"\033[0m!" #Retuns a random Pokemon from our list and hightlight's the text in or chosen color (yellow).


while True:
    print('\n') #Adds a new line, or in this case a linebreak.
    selection = input("Ready to throw a random Pokeball?\nY: Yes\nQ: Q to exit.\n")
    if selection == "Q" or selection == "q":
            print('\n') #Adds a new line, or in this case a linebreak.
            print('Quitting')
            sys.exit()
    if selection == "Y" or selection == "y":
            print('\n')
            result = (Pokemon())
            print (result)
            print('\n')
           
    else:  
        time.sleep(8)
      
