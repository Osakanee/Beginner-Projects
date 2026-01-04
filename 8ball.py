import random
from rich import print

options = ["[green]Yes.[/green]", "[yellow]Maybe.[/yellow]", "[red]No.[/red]", "[grey2]Don't rush.[/grey2]"]
print("Ask me a question, and I shall answer you.")

def say(thats):
    answer = random.choice(options)
    print("You've asked:", thats)
    print("The [blue]8-ball[/blue] says", answer)

while True:
    thething = input("> ").lower().strip()
    if thething == "exit":
        print("The [blue]8-ball[/blue] enjoyed your stay.")
        break
    say(thething)



