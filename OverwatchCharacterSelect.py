import sys
import random
import time

#3 arrays that can output a random variable when called.
Tanks = ['D.Va','Doomfist','Hazard','Junker Queen','Mauga','Orisa','Ramattra','Reinhardt','Roadhog','Sigma','Winston','Wrecking Ball','Zarya']  
DPS = ['Ashe','Bastion','Cassidy','Echo','Genji','Hanzo','Junkrat','Mei','Pharah','Reaper','Sojourn','Soldier: 76','Sombra','Symmetra','Torbjörn','Tracer','Venture','Widowmaker'] 
Support = ['Ana','Baptiste','Brigitte','Illari','Juno','Kiriko', 'Lifeweaver','Lúcio','Mercy','Moira','Zenyatta'] 


#An array that groups all the other arrays togeather.
All_Characters = [Tanks,DPS,Support]
#This allows for a random variable to be generated from across all the arrays.
No_Limits = random.choice(random.choices(All_Characters)) 

#Each of the 4 imput options returns a random value from one of the 4 arrays.
while True:
    print('\n') #Adds a new line, or in this case a linebreak.
    print("What role are you?")
    selection = input("1: Tank\n2: Damage\n3: Support\n4: No Limits\nQ: Q to exit.\n")
    if selection == "Q" or selection == "q":
            print('\n') 
            print('Quitting')
            sys.exit()
    if selection == "1":
            print('\n')
            print(random.choice(Tanks))
    if selection == "2":
            print('\n')
            print(random.choice(DPS))
    if selection == "3":
            print(random.choice(Support))
    if selection == "4":
            print('\n')
            print(random.choice(No_Limits))        

    else:  
            time.sleep(5)


