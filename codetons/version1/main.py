import time
import moves
from rich import print
battlestarted = False

print("Before you start, you must choose your codeton.")
print("[red]● Java[/red]")
print("[blue]● Py[/blue][yellow]thon[/yellow]")
print("[purple]● Cplus[/purple]")

starter = input("> ").lower()

chosen = moves.codetons.get(starter)

match starter:
    case("java"):
        validcodeton = True
        time.sleep(1)
    case("python"):
        validcodeton = True
        time.sleep(1)
    case("cplus"):
        validcodeton = True
        time.sleep(1)




if validcodeton == True:
    print("[green]Tiny Vin has challenged you to a codeton battle![/green]")
    time.sleep(2)
    print("Your moves are...")
    match starter:
        case("java"):
            battlestarted = True
            time.sleep(0.5)
            moveslist = ["ClassFair", "CoffeeBlast", "WalkBite", "Growl"]
            for i in moveslist:
                print(i)
        case("python"):
            battlestarted = True
            time.sleep(0.5)
            moveslist = ["Match Case", "PyBurst", "Pywalk", "Growl"]
            for i in moveslist:
                print(i)
        case("cplus"): 
            battlestarted = True
            time.sleep(0.5)
            moveslist = ["Leakmemo", "IhateyouRust", "Cython"]
            for i in moveslist:
                print(i)

while battlestarted == True:
    time.sleep(1)
    print("Your turn!")
    attack = input("> ").lower().strip()
    if attack in moves.movescdex and starter == "cplus":
        moves.vsmart["hp"] -= moves.movescdex[attack]["dmg"]
        print("[purple]Cplus used[/purple]", moves.movescdex[attack]["name"])
        print("[blue]Enemy's health[/blue]:", moves.vsmart["hp"])
    elif attack in moves.movespydex and starter == "python":
        if "dmg" in moves.movespydex[attack]:
            moves.vsmart["hp"] -= moves.movespydex[attack]["dmg"]
        else:
            moves.growl["activated"] = True
            print("You used growl! Enemy's moves now deal less damage")
        print("[blue]Py[/blue][yellow]thon[/yellow] used", moves.movespydex[attack]["name"])
        print("[blue]Enemy's health[/blue]:", moves.vsmart["hp"])
    elif attack in moves.movesjavdex and starter == "java":
        if "dmg" in moves.movesjavdex[attack]:
            moves.vsmart["hp"] -= moves.movesjavdex[attack]["dmg"]
        else:
            moves.growl["activated"] = True
            time.sleep(0.2)
            print("You used growl! [darkgreen]Enemy's moves now deal less damage[/darkgreen]")
        print("[red]Java used[/red]", moves.movesjavdex[attack]["name"])
        print("[blue]Enemy's health[/blue]:", moves.vsmart["hp"])
    else:
        print("Move not valid, it's now the enemy's turn.")
    if starter == "cplus" and moves.vsmart["hp"] > 0:
        moves.cplus["hp"] -= 10
        time.sleep(0.2)
        print("[blue]Vsmart used ignoremistake![/blue], Your codeton lost 10 hp. Current Codeton health:", moves.cplus["hp"])
    elif starter == "java" and moves.vsmart["hp"] > 0:
        if moves.growl["activated"] == True:
            moves.java["hp"] -= (10 - moves.growl["reducdmg"])
            time.sleep(0.2)
            print("[blue]Vsmart used ignoremistake![/blue], [darkred]Your codeton lost 8 hp[/darkred]. Current Codeton health:", moves.python["hp"])
        elif moves.growl["activated"] == False:
            moves.java["hp"] -= 10
            time.sleep(0.2)
            print("[blue]Vsmart used ignoremistake![/blue], [darkred]Your codeton lost 10 hp[/darkred]. Current Codeton health:", moves.python["hp"])
    elif starter == "python" and moves.vsmart["hp"] > 0:
        if moves.growl["activated"] == True:
            moves.python["hp"] -= (10 - moves.growl["reducdmg"])
            time.sleep(0.2)
            print("[blue]Vsmart used ignoremistake![/blue], Your codeton lost 8 hp. Current Codeton health:", moves.python["hp"])
        elif moves.growl["activated"] == False:
            moves.python["hp"] -= 10
            time.sleep(0.2)
            print("[blue]Vsmart used ignoremistake![/blue], Your codeton lost 10 hp. Current Codeton health:", moves.python["hp"])
    if moves.vsmart["hp"] == 0 or moves.vsmart["hp"] < 0:
        print("You've won! Congrats!")
        time.sleep(0.4)
        break
    elif starter == "cplus" and moves.cplus["hp"] == 0:
        print("You lost... you rushed back to overflow center.")
        time.sleep(0.4)
        break
    elif starter == "java" and moves.java["hp"] == 0:
        print("You lost... you rushed back to overflow center.")
        time.sleep(0.4)
        break
    elif starter == "python" and moves.java["hp"] == 0:
        print("You lost... you rushed back to overflow center.")
        time.sleep(0.4)
        break
# fix java not getting damage, fix the losing system and fix every bug 