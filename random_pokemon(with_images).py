# Standard Library modules
from fileinput import filename
import os
import sys
import time
import random

# 3rd-Party modules
from PIL import Image


print ('Random Pokemon Generator by Chris "Eva_Fan" Trace')
print ('----------')

# This is the version of the script that uses aditional 3rd party python libraries to display images as well.

#An array that contains a list of pokemon, that will output a random variable when called.
def Pokemon():

    Pokemon_list = ['Bulbasaur','Charmander','Squirtle','Pikachu','Pidgey','Rattata','Sandshrew','Clefairy','Vulpix','Jigglypuff','Zubat','Diglett','Meowth','Magikarp','Psyduck','Gengar','Eevee','Hitmonchan','Snorlax','Wobbuffet']  
    
    #Retuns a random Pokemon from our list and hightlight's the text in or chosen color (yellow).
    return random.choice(Pokemon_list)

def Picture():
    folder_path = "C:\\git_repo\\evafan84\\test_scripts\\pokemon_images\\"
    # Choose a random image file
    random_image = Pokemon() 
    output_image = random_image+'.png'
    filename = (folder_path+output_image)
    img = Image.open(filename)
    img.show()
    return img.show()


color_code = "\033[33m" #ANSI escape_code to set the text color to yellow.

while True:
    print('\n') #Adds a new line, or in this case a linebreak.
    selection = input("Ready to throw a random Pokeball?\nY: Yes\nQ: Q to exit.\n")
    if selection == "Q" or selection == "q":
            print('\n') #Adds a new line, or in this case a linebreak.
            print('Quitting')
            sys.exit()
    if selection == "Y" or selection == "y":
            print('\n')
            result = "This pokeball contains... " + color_code + Pokemon() +"\033[0m!"
            print (result)
            Picture
            print('\n')
           
      
