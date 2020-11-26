#!/usr/bin/env python3.9
print(chr(27) + "[2J") #löscht die bisherige Ausgabe.
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
gewinner = "Noch hat niemand gewonnen ;)" #useless

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
        log.info("deine eingabe war:" + str(eingabe))
        abfrage()

    elif eingabe == "Stein" or eingabe == "Schere" or eingabe == "Papier" :
        if eingabe == "Stein":
            user = int(0)
        elif eingabe == "Papier":
            user = int(1)
        elif eingabe == "Schere":
            user = int(2)
        
        else:
            print ("Es ist ein Fehler bei der zuordnug unterlaufen.\nDieser Fehler sollte nie Aufteten da die Eingabe voher geprüft wird.")
    else:
        print(chr(27) + "[2J")
        print("Deine Eingabe ist ungültig\nPrüfe ob du dich vertippt hast.")
        log.warning("Falche Eingabe: " + eingabe)
        abfrage()
    log.info("Der User hat " + str(liste[user]) + " gewählt")

abfrage()


log.info("Der Pc hat " + str(liste[pc]) + " gewählt")

def ermitteln():
    global gewinner
    if user == pc:
        log.info("Auswahl ist Gleich daher ist es Unentschieden.")
        log.debug("Nutzer Eingabe:" + str(user) +"\n" +"Computer Auswahl:" + str(pc))
        log.info = (gewinner)
        gewinner = Fore.CYAN + "Da der Pc " + str(liste[int(user)]) + " gewählt hat und du auch " + str(liste[int(pc)]) + " gewählt hast steht es unentschieden."
        

    elif pc == 0: #Stein
        log.info("Der Pc hat Stein gewählt ermittele gewinner durch benutzer eingabe...")
        if user == 1: #Papier
            gewinner = Fore.GREEN + "Da du " + str(liste[int(user)]) + " gewählt hast und der PC " + str(liste[int(pc)]) + " gewählt hat hast du Gewonnen"
        elif user == 2: #Schere
            gewinner = Fore.RED + "Da du " + str(liste[int(user)]) + " gewählt hast und der PC " + str(liste[int(pc)]) + " gewählt hat hast du Verloren."


    elif pc == 1: #Papier
        log.info("Der Pc hat Papier gewählt ermittele gewinner durch benutzer eingabe...")
        if user == 0: #Stein
            gewinner = Fore.RED + "Da du " + str(liste[int(user)]) + " gewählt hast und der PC " + str(liste[int(pc)]) + " gewählt hat hast du Verloren."
        elif user == 2: #Schere
            gewinner = Fore.GREEN + "Da du " + str(liste[int(user)]) + " gewählt hast und der PC " + str(liste[int(pc)]) + " gewählt hat hast du Gewonnen"


    elif pc == 2: #Schere
        log.info("Der Pc hat Schere gewählt ermittele gewinner durch benutzer eingabe...")
        if user == 0: #Stein
            gewinner = Fore.GREEN + "Da du " + str(liste[int(user)]) + " gewählt hast und der PC " + str(liste[int(pc)]) + " gewählt hat hast du Gewonnen"
        
        elif user == 1: #Papier
            gewinner = Fore.RED + "Da du " + str(liste[int(user)]) + " gewählt hast und der PC " + str(liste[int(pc)]) + " gewählt hat hast du Verloren."


    else:
        log.warn("Es ist ein unerwateter Fehler beim ermitteln der Ergebnisse aufgetreten")
        print(Fore.RED + "Es ist ein unerwateter Fehler aufgetreten.")
        gewinner = Fore.CYAN + "Da du " + str(liste[int(user)]) + " gewählt hast und der PC " + str(liste[int(pc)]) + " aber ein Unerwateter Fehler aufgetreten ist hat niemand gewonnen."


ermitteln()
print(gewinner)
#TODO: Doppelte enfernen.