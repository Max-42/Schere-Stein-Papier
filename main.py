#!/usr/bin/env python3.9
#importiert das random package
import random
#willkommens Nachicht
spacer = "#####################################\n"
print(spacer + "Willkommen bei Schnick Schnack Schnuck\n" + spacer)

liste = ["Stein" , "Papier", "Schere"]
pc = random.choice(liste)

print(pc)#Gibt die Auswahl des PC's an. (Zum testen)

def abfrage():
    """ Führt die Abfrage des User-Inputs aus. """
    global user
    eingabe = input('Gebe "Schere", "Stein" oder "Papier" ein.\n')
    if eingabe == "":

        print("Du darfst nicht nichts angeben.")
        abfrage()

    elif eingabe == "Stein" or eingabe == "Schere" or eingabe == "Papier" :
        if eingabe == "Stein":
            user = int(0)
        elif eingabe == "Schere":
            user = int(1)
        elif eingabe == "Papier":
            user = int(2)
        else:
            print ("Es ist ein Fehler bei der zuordnug unterlaufen.\nDieser Fehler sollte nie Aufteten da die Eingabe voher geprüft wird.")
    else:
        print("Deine Eingabe ist ungültig\nPrüfe ob du dich vertippt hast.")
        print(abfrage)
        abfrage()

abfrage()

print(user)
print("Der User hat " + str(liste[user]) + "gewählt")
print ("Der PC hat ")