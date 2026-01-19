import os 
from pathlib import Path

bannedlist = ["C:/System32", "C:/System", "C:/Program Files", "C:/Program Files (x86)", "C:/Windows"]

def starterkit(path):
    path.mkdir(parents=True, exist_ok=True)
    src = path / "src"
    assets = path / "assets"
    readme = path / "README.md"
    requirements = path / "requirements.txt"
    src.mkdir()
    assets.mkdir()
    readme.touch()
    requirements.touch()

while True:
    print("〃 Gimme an absolute path to make the folder and the subfolders 〃")
    thestuff = input("> ")
    p = Path(thestuff)
    for word in thestuff:
        if thestuff in bannedlist:
            print("Unable to continue")
            thestuff = input("> ")
            p = Path(thestuff)
    if thestuff == "exit":
        break
    elif p.is_dir() == False:
        starterkit(p)
    else:
        print("Error, a folder already exists with that name or this isn't an absolute path")
        print("example of absolute path: C:/Users/YourUser/Downloads/YourProject")



