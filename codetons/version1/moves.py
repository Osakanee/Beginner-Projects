java = {
    "name": "Java",
    "hp": 100,
    "type": "Fire"
}


python = {
    "name": "Python",
    "hp": 100,
    "type": "Electric"
}

cplus = {
    "name": "Cplus",
    "hp": 110,
    "type": "Poison"
}

vsmart = {
    "name": "Vsmart",
    "hp": 100,
    "type": "Normal"
}

codetons = {
    "java": java,
    "python": python,
    "cplus": cplus,
    "vsmart": vsmart
}

classfair = {
    "name": "classfair",
    "dmg": 5,
    "type": "Fire"
}

coffeeblast = {
    "name": "coffeeblast",
    "dmg": 25,
    "type": "Fire"
}

walkbite = {
    "name": "walkbite",
    "dmg": 30,
    "type": "Dark"
}

matchcase = {
    "name": "matchcase",
    "dmg": 5,
    "type": "Normal"
}

pyburst = {
    "name": "pyburst",
    "dmg": 15,
    "type": "Electric"
}

pywalk = {
    "name": "pywalk",
    "dmg": 30,
    "type": "Electric"
}

leakmemo = {
    "name": "leakmemo",
    "dmg": 10,
    "type": "Electric"
}

ihateyourust = {
    "name": "ihateyourust",
    "dmg": 42,
    "type": "Dark"
}

cython = {
    "name": "cython",
    "dmg": 27,
    "type": "Ice"
}

growl = {
    "name": "growl",
    "activated": False,
    "reducdmg": 2
}

movesjavdex = {
    "classfair": classfair,
    "coffeeblast": coffeeblast,
    "walkbite": walkbite,
    "growl": growl
}

movespydex = {
    "matchcase": matchcase,
    "pyburst": pyburst,
    "pywalk": pywalk,
    "growl": growl
}

movescdex = {
    "leakmemo": leakmemo,
    "ihateyourust": ihateyourust,
    "cython": cython
}


movesjava = [classfair["name"], coffeeblast["name"], walkbite["name"]]
movespython = [matchcase["name"], pyburst["name"], pywalk["name"]]
movescplus = [leakmemo["name"], ihateyourust["name"], cython["name"]]


# add moves and types and damage