
i = 1
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

print("Give me your name")
name = input("my name is: ")
clear()
print("choose your weapon")
print("1. sword")
print("2. staff")
ase = int(input())
clear()
if ase == 1:
    ase2 = "sword"
elif ase == 2:
    ase2 = "bow"
else:
    print("you chose wrong you die")
    quit()
print("Welcome to the cave")
while i < 4:
    print("choose your direction")
    print("1. left")
    print("2. right")
    suunta = int(input())
    clear()
    if suunta == 2:
        print("you went right there is a monster there do you want to fight?")
        print("1. no")
        print("2. yes")
        valinta = int(input())
        clear()
        if valinta == 2:
            print("you attack the monster with " + ase2 + " dealing damage")
            if ase == 1:
                print("the monster bashes your skull and you die")
                quit()
            else:
                print("you succesfully kill the monster from long range")
                print("you realize that the path behind it goes nowhere. you go back")
            
    elif suunta == 1:
        print("you went left")
        i += 5 
    else:
        print("you chose wrong you die")
        quit()
o = 1
while o < 4:
    print("You come across a big pond of water what do you wish to do?")
    print("1. swim across")
    print("2. walk around")
    v2 = int(input())
    clear()         
    if v2 == 1:
        print("something grabs you and brings you deeper underground")
        print("you awaken wet in a dark cave")
        print("where do you wish to go?")
        print("1. left")
        print("2. right")
        suunta = int(input())
        clear()
        if suunta == 2:
            print("the cave deepens")
            print("where do you wish to go?")
            print("1. left")
            print("2. right")
            suunta = int(input())
            clear()
            if suunta == 2:
                print("the cave deepens...")
                print("where do you wish to go?")
                print("1. left")
                print("2. right")
                suunta = int(input())
                clear()
                if suunta == 2: 
                    print("you made it out of the hole you were dragged into")
                    o += 5
                elif suunta == 1:
                    print("you went onwards and never found exit you died.")
                    quit()
                else:
                    print("you chose wrong you die")
                    quit()
            elif suunta == 1:
                print("you went onwards and never found exit you died")
                quit()
            else:
                print("you chose wrong you died")
                quit()
        elif suunta == 1:
            print("you continued on your tracks forever and ended up dead")
            quit()
        else:
            print("you chose wrong you died")
    elif v2 == 2:
        print("you walked around it and nothing happened")
        print("you find a tunnel that goes deeper")
        print("you enter it")
        o += 5
    else:
        print("you chose wrong you died")
        quit()
            
print("you enter a grand space that beholds piles upon piles of gold")
print("theres a dragon guarding the gold")
print("do you wish to defeat it?")
print("1. no")
print("2. yes")
decision = int(input())
clear()
if decision == 1:
    print("you go back home and make bread water soup")
    print("your spouse is disappointed in you, " + name + " are you proud of yourself?")
    print("youre poor")
    print("thank you for playing")
    quit()
elif decision == 2:
    print("you try taking the dragon head on")
    print("the dragon breathes fire upon you")
    if v2 == 1:
        print("the wet clothes from before save you from certain death")
        print("you manage to slay the dragon with your" + ase2 + "congratulations")
        print("you return home and your spouse waits there for you happily")
        print("you eat like a king for the rest of your life")
        print("thank you for playing ", name)
    else:
        print("the dragons fires kill you instantly")
        print("you will never see your family again")
        print("goodbye")
        quit()
else:
    print("you chose wrong you lost the game")
    quit()


