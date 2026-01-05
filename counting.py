from rich import print

def counting():
    global currentnumber
    currentnumber = 0
    while True:
        count = int(input("> "))
        if count == currentnumber + 1:
            print(currentnumber + 2)
            currentnumber += 2
        else:
            print("[red]Wrong number![/red]")

print("[yellow]Welcome to counting.py![/yellow]")
print("Start [blue]counting[/blue], and i'll go with you!")
print("Current number is: 0 Next is 1!")

counting()

