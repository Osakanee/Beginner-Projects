from rich import print

def counting():
    currentnumber = 0
    wrongtries = 1
    while True:
        try:
            count = int(input("> "))
        except ValueError:
            print("That's not a number, goodbye.")
            break
        if count == currentnumber + 1:
            print(currentnumber + 2)
            print("Next number is:", currentnumber + 3)
            currentnumber += 2
        elif wrongtries == 3:
            print("You think you're soooo funny huh.")
            break
        else:
            print("[red]Wrong number![/red]")
            print("Warning", wrongtries)
            wrongtries += 1

print("[yellow]Welcome to counting.py![/yellow]")
print("Start [blue]counting[/blue], and i'll go with you!")
print("Current number is: 0 Next is 1!")

counting()

