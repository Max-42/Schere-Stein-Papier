#!/usr/bin/env python3.9

import random #importiert das random package
import argparse #importiert das argparse Package um argumente zu verarbeiten
import logging as log #importiert das logging package als log um die Ausgabe des Scriptes anzupassen.
from colorama import Fore, Style, init #importiert aus colorama Fore und Style um Farbige ausgabe zu ermöglichen. init um das automatische zurücksetzen zu ermöglichen.
init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='count', default=0)
args = parser.parse_args()

#Legt die debug Ausgabeatufen fest.
stufen = [log.WARNING, log.INFO, log.DEBUG]
stufe = stufen[min(len(stufen)-1,args.verbose)]

log.basicConfig(level=stufe, format= Fore.YELLOW +"%(message)s" + Style.RESET_ALL) #legt das Nachichten format fest


#Willkommens Nachicht
spacer = Fore.BLUE + "#####################################\n"
print(spacer + "Willkommen bei Schnick Schnack Schnuck\n" + spacer)

liste = ["Stein" , "Papier", "Schere"]
pc = random.randint(0,2)


log.debug("Auswahl des PC " + str(pc) + " welches " +  str(liste[int(pc)]) + " entspricht.")  #Gibt die Auswahl des PC's an. (Zum testen)

def abfrage():
    """ 
    Führt die Abfrage des User-Inputs aus. 
    """
    global user
    eingabe = input('Gebe "Schere", "Stein" oder "Papier" ein.\n')
    if eingabe == "":
        print(chr(27) + "[2J")
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
        log.warning("Falche Eingabe: " + eingabe)
        abfrage()

abfrage()

log.debug(user)
log.info("Der User hat " + str(liste[user]) + " gewählt")
log.info("Der Pc hat " + str(liste[pc]) + " gewählt")