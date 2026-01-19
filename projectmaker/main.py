import os 
from pathlib import Path
from rich import print

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
    print("〃 [grey2]Gimme an absolute path to make the folder and the subfolders[/grey2] 〃")
    thestuff = input("> ")
    p = Path(thestuff)
    for word in thestuff:
        if thestuff in bannedlist:
            print("[red]Unable to continue[/red]")
            thestuff = input("> ")
            p = Path(thestuff)
    if thestuff == "exit":
        break
    elif p.is_dir() == False:
        starterkit(p)
    else:
        print("[red]Error, a folder already exists with that name or something went wrong.[/red]")
        print("[yellow]Example of how you use this script: C:/Users/YourUser/Downloads/YourProject[/yellow]")



