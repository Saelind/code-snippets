__author__ = 'Saelind'
import datetime

TEXT = 0
ZAHl = 1
DATUM = 2


def getinput(strorint, bereich=None, nachricht='Eingabe'):
    if strorint == 0:
        while True:
            eingabe = input("{0}: ".format(nachricht))
            if not len(eingabe) == 0:   # Prüft ob str leer ist
                return eingabe
    elif strorint == 1:
        while True:
            try:
                zahl = int(input("{0}: ".format(nachricht)))
                bereich and bereich.index(zahl)  # Test ob zahl in bereich
                return zahl
            except ValueError:
                print("Falsche Eingabe")
    else:
        global testdatum
        while True:
            try:
                datum = getinput(TEXT, nachricht='Datum eingeben im Format DD.MM.YYYY')
                datumsplit = datum.split('.')
                if not len(datumsplit) == 3:  # Überprüft ob es Tag/Monat/Jahr hat
                    print('debug')
                    continue
                jahr = int(datumsplit[2])
                monat = int(datumsplit[1])
                tag = int(datumsplit[0])
                testdatum = datetime.datetime(jahr, monat, tag)  # Überprüft ob die daten ein echtes datum sin
                finaldatum = datetime.datetime(jahr, monat, tag)
                return finaldatum
            except ValueError:
                print('Fehler in der Eingabe')
