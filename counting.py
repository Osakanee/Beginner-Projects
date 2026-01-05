from rich import print

def counting():
    global currentnumber
    currentnumber = 0
    wrongtries = 0
    while True:
        count = int(input("> "))
        if count == currentnumber + 1:
            print(currentnumber + 2)
            currentnumber += 2
        elif wrongtries == 2:
            print("You think you're soooo funny huh.")
            break
        else:
            print("[red]Wrong number![/red]")
            wrongtries += 1

print("[yellow]Welcome to counting.py![/yellow]")
print("Start [blue]counting[/blue], and i'll go with you!")
print("Current number is: 0 Next is 1!")

counting()

