# Standard Library modules
import time
import sys
import subprocess
import datetime
import random

# local modules (in-house modules)
from PrintLog import *




time.sleep(0.5)

Human_Female_names = ['Alice','Anastasia','Ann','Annabeth','Antônia','Anya','Arya','Avva','Bella','Bellatrix','Bodicia','Camila','Carys','Celeste','Coraline','Daisy','Elena','Emilia','Francisca','Freya','Giselle','Ilya','Isabella','Kira','Kyra','Maria','Mia','Misha','Nakita','Olivia','Paige','Renata','Sasha','Sofía','Valentina','Valeria','Viktoria','Willow']  
Human_Male_names = ['Alistair','Alexei','Angus','Bellamy','Caleb','Caspian','Cornelius','Conrad','Constantine','Dimitri','Donovan','Eduard','Egbert','Elias','Fergus','Fraser','Gideon','Godfreid','Hayden','Hugo','Ivan','John','Konstantin','Leon','Luther','Martin','Nathaniel','Píetro','Rainier','Simeon','Theodore','Vasily','Vladimir','Yuri']
Elf_Male_names = ['Acer','Ash','Argus','Arlen','Belanor','Boreas','Ciaran','Dakath','Darian','Durlan','Eldrin','Emyr','Erlik','Fiore','Glorandal','Haelyn','Helios','Jareth','Kai','Kayden','Kendel','Luca','Lycidas','Narek','Oberon','Oriel','Pyrder','Rowan','Ruven','Tabor','Timur','Trinty','Valen']
Elf_Female_names = ['Aisling','Arcaena','Arwen','Ashe','Aurora','Circe','Elisei','Eowyn','Eris','Essenaree','Fenella','Francessca','Galadriel','Glinda','Gweyr','Ishika','Isla','Laela','Léna','Luna','Lyra','Makari, Maeve','Maura','Morrigan','Roanmara','Ruven','Shalendra','Sylleth','Tatiana','Tauriel','Vita','Zene']

print()

while True:
    selection = input("Ready to continue?\n Y: Yes:\n Q: Quit\n")
    if selection == "Q" or selection == "q":
        print("Quitting")
        sys.exit()
    if selection == "Y" or selection == "y":
        PrintLog.title("Comencing Fantasy Chracter Name Generator.\n")
        break

    else:  
        time.sleep(1)

 

time.sleep (0.5)
print("------------------\n")
PrintLog.info("Select what gender you want the character to be.\n")

gender = input("1: Male\n2: Female\nQ: Q to exit.\n")
if gender == "Q" or gender == "q":
        PrintLog.debug('Quitting')
        sys.exit()
if gender == "1":
        print('Male\n')
if gender == "2":
        print('Female\n')

print('\n')


print("Select what race you want the character to be.\n")

selection = input("1: Human\n2: Elf\n3: Dwarf\n4: Half-Orc\n5: Half-Elf\n6: Hafling\n7: Teifling\nQ: Q to exit.\n")
if selection == "Q" or selection == "q":
        PrintLog.debug('Quitting')
        sys.exit()
if selection == "1":
    print('Human\n')
    if gender == "1":
        print(random.choice(Human_Male_names))
        print('\n')
    if gender == "2":
        print(random.choice(Human_Female_names))
        print('\n')
if selection == "2":
        print('Elf\n')
        if gender == "1":
            print(random.choice(Elf_Male_names))
        print('\n')
        if gender == "2":
            print(random.choice(Elf_Female_names))
        print('\n')
if selection == "3":
        print('Dwarf\n')
if selection == "4":
        print('Half-Orc\n')
if selection == "5":
        print('Half-Elf\n')
        if gender == "1":
            print(random.choice(Human_Male_names),(Elf_Male_names))
            print('\n')
        if gender == "2":
            print(random.choice(Human_Female_names),(Elf_Female_names))
            print('\n')
if selection == "6":
        print('Halfling\n')
if selection == "7":
        print('Teifling\n')        
 

