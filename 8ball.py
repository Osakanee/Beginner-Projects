import random
from rich import print
from progress.bar import Bar
import time

bar = Bar('processing', max=100)
for i in range(100):
    time.sleep(0.01)
    bar.next()
bar.finish()

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



