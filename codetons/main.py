from rich import print
import time
import random

validcodeton = False
ongoingbattle = False

# Classes

class Codeton:
    def __init__(self, name, hp, typ):
        self.name = name
        self.hp = hp
        self.typ = typ

class Moves:
    def __init__(self, name, dmg, type, owner):
        self.name = name
        self.dmg = dmg
        self.type = type
        self.owner = owner


# all moves my back hurts
pyburst = Moves("Pyburst", 30, "Electric", "Python")
matchcase = Moves("MatchCase", 15, "Electric", "Python")
walkbite = Moves("Bite", 40, "Electric", "Python")
classfair = Moves("ClassFair", 10, "Normal", "Java")
coffeeblast = Moves("CoffeeBlast", 25, "Fire", "Java")
lungebite = Moves("LungeBite", 20, "Dark", "Java")
leakmemo = Moves("Leakmemo", 30, "Poison", "Cminus")
cython = Moves("Cython", 25, "Ice", "Cminus")
ihateyourust = Moves("Ihateyourust", 40, "Dark", "Cminus")


#enemy moves
attacklight = Moves("Light Attack", 10, "Normal", "Vsmart")
attackmed = Moves("Medium Attack", 30, "Normal", "Vsmart")
attackheavy = Moves("Heavy Attack", 40, "Normal", "Vsmart")


# User codetons
python = Codeton("Python", 100, "Electric")
java = Codeton("Java", 135, "Fire")
cminus = Codeton("Cminus", 95, "Poison")

# Enemy codeton
vsmart = Codeton("Vsmart", 100, "Normal")

# dicts 
codetons = {
    "python": python,
    "java": java,
    "cminus": cminus,
}

moves = {
    "pyburst": pyburst,
    "matchcase": matchcase,
    "walkbite": walkbite,
    "classfair": classfair,
    "coffeeblast": coffeeblast,
    "lungebite": lungebite,
    "leakmemo": leakmemo,
    "cython": cython,
    "ihateyourust": ihateyourust
}

enemycodeton = { # this shit was never USED cuz i never managed to figure out how to make it work but imma leave it either way
    "vsmart": vsmart
}

enemymoves = {
    "attacklight": attacklight,
    "attackmed": attackmed,
    "attackheavy": attackheavy
}

enemyattacks = [attacklight, attackmed, attackheavy] #randomizer heck yea
# Beginning

print("Hello, welcome to the world of codeton!")
time.sleep(0.3)
print("In this tiny program, you can battle a codeton!")
time.sleep(0.3)
print("Choose one between these three:")
print("You have [yellow]Pyt[/yellow][blue]hon.[/blue]")
time.sleep(0.3)
print("Or maybe, [red]Java.[/red]")
time.sleep(0.4)
print("Maybe you are up for a harder time and use [medium_turquoise]Cminus.[/medium_turquoise]")
time.sleep(0.2)

starter = input("> ").lower()

# valid codeton check
if starter not in codetons:
    print("Not an option, quitting the script..") 
elif starter in codetons:
    validcodeton = True
    print("Are you sure you want to choose this codeton?")
    warning = input("> ").lower()
    if warning not in ("yes", "no"):
        print("Not an option.")
        warning = input("> ").lower()
    elif warning == "yes":
        print("Good! The battle shall start.")
        ongoingbattle = True
        chosen = codetons[starter]
    elif warning == "no":
        print("I see, you may choose again then.")
        starter = input("> ")
# battle system
if validcodeton == True and ongoingbattle == True:
    while True:
        randommove = random.choice(enemyattacks)
        print("Your move!")
        attack = input("> ").lower()
        if vsmart.hp <= 0:
            print("You have defeated Tiny Vin, the keyboard warrior and got 500 Charms!")
            break # I HATE THIS BREAK TAKING TOO LONG
        elif codetons[starter].hp <= 0:
            print("You fainted")
            break
        if attack in moves and codetons[starter].name == moves[attack].owner:
            theattack = moves[attack].dmg
            themove = moves[attack].name
            time.sleep(0.5)
            print(codetons[starter].name, "used", themove, "on", vsmart.name, "and dealt", theattack, "damage!")
            vsmart.hp -= theattack
            time.sleep(0.5)
            print("Enemy has:", vsmart.hp, "hp left")
            time.sleep(0.5)
            print(f"Enemy used {randommove.name} on your codeton and dealt {randommove.dmg}!")
            codetons[starter].hp -= randommove.dmg
            print("Your codeton's current health is:", codetons[starter].hp)
            time.sleep(0.5)
        else:
            print("Invalid move!")