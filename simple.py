import random #importiert das random Package.

user = 0
pc = 0

print(chr(27) + "[2J")
pc = random.randint(1,3)
user = (int(input("Schere [1], Stein [2] oder Papier [3]")))
#Überprüfung

#Unentschieden
if user == pc:
    print("Das Spiel ist Unentschieden")
#Bei Schere
elif user == 1:
    if pc == 2:
        print("Verloren, Computer gewinnt mit Stein gegen Schere!")
        print("Gewonnen, Computer verliert mit Papier gegen Schere!")
#Bei Stein
elif user == 2:
    if pc == 1:
        print("Gewonnen, Computer verliert mit Schere gegen Stein!")
    elif pc == 3:
        print("Verloren, Computer gewinnt mit Papier gegen Stein!")
#Bei Papier
elif user == 3:
    if pc == 1:
        print("Verloren, Computer gewinnt mit Schere gegen Papier!")
    elif pc == 2:
        print("Gewonnen, Computer verliert mit Stein gegen Papier!")