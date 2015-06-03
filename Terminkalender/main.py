__author__ = 'Saelind'
import datetime
import sys
from operator import attrgetter

import Termine
import Profile
import Textumsetzung
import Output
import SaveAndLoad
import Tools


TEXT = 0
ZAHl = 1
DATUM = 2


class Main():
    def __init__(self):
        # Daten laden
        self.backgrounddata = SaveAndLoad.SaveAndLoad()  # SaveAndLoad-Klassen objekt wird erstellt
        self.dates = self.backgrounddata.gettermine()  # Läd Termine
        self.contacts = self.backgrounddata.getkontakte()  # Läd Kontakte
        self.allprofiles = self.backgrounddata.getalleprofile()  # Läd alle vorhanden Profile
        self.actprofile = str(self.backgrounddata.getprofil())  # Läd aktuelles Profil
        # Output Klasse laden
        self.output = Output.Output()

    def createnewdate(self, data=None):
        if data is None:
            data = self.new_date_input()
        termin = Termine.Termine(data[0], data[1], data[2])
        termin.profile = self.actprofile
        self.dates.append(termin)

    def edit_date(self):
        pass

    def new_date_input(self):
        datum_datum = Tools.getinput(DATUM)  # Daten für Datum erstellung holen
        betreff = Tools.getinput(TEXT, nachricht='Betreff des Termines')
        textinhalt = Tools.getinput(TEXT, nachricht='Textinhalt des Termines')
        return [datum_datum, betreff, textinhalt]

    def get_next_n_dates(self, n):
        future_dates = []
        counter = 0
        for t in self.dates:
            if counter == n:
                return future_dates
            d = t.getdatum()    # Holt das Datum der Termine Objekte
            if d >= datetime.datetime.today():  # Überprüft ob Datum der Termine in der Zukunft liegt
                future_dates.append(t)
                counter += 1

    def get_last_n_dates(self, n):
        past_dates = []
        counter = 0
        for t in self.dates:
            if counter == n:
                return past_dates
            d = t.getdatum()    # Holt das Datum der Termine Objekte
            if d <= datetime.datetime.today():
                past_dates.append(t)
                counter += 1

    def sort_dates(self):
        self.dates.sort(key=attrgetter('datum'))

    def main_loop(self):
        while 1:
            self.output.draw_main_board()
            haupteingabe = Tools.getinput(ZAHl, bereich=range(1, 7))
            if haupteingabe == 1:
                self.createnewdate()
            elif haupteingabe == 2:
                if self.dates:
                    print("Welchen Termin möchten sie bearbeiten")
                    self.output.draw_numbered_list(self.dates)
                    auswahl = Tools.getinput(ZAHl, bereich=range(1, len(self.dates) + 1))
                    zubearbeitendertermin = self.dates[auswahl - 1]
                    self.output.draw_edit_dates()
                    eingabe = Tools.getinput(ZAHl, bereich=range(1, 6))
                    if eingabe == 1:
                        zubearbeitendertermin.editdatum()
                    elif eingabe == 2:
                        zubearbeitendertermin.editbetreff()
                    elif eingabe == 3:
                        zubearbeitendertermin.edittextinhalt()
                    elif eingabe == 4:
                        zubearbeitendertermin.del_self()
                        self.dates.remove(zubearbeitendertermin)
                    else:
                        pass
                else:
                    print("Es stehen keine Termine zur Verfügung")
            elif haupteingabe == 3:
                print("Eingabe 3")
                if self.dates:
                    self.output.draw_simple_list(self.dates)
            elif haupteingabe == 4:
                self.output.draw_profile_options()
                eingabe = Tools.getinput(ZAHl, bereich=range(1, 4))
                if eingabe == 1:    # Neues Profile erstellen
                    name = Tools.getinput(TEXT)
                    self.backgrounddata.neudatenincome(name, [[], []])
                    self.backgrounddata.aktprofile(name)
                    self.dates = self.backgrounddata.gettermine()
                    self.contacts = self.backgrounddata.getkontakte()
                    self.allprofiles = self.backgrounddata.getalleprofile()
                    self.actprofile = str(self.backgrounddata.getprofil())
                elif eingabe == 2:  # Profil wechseln
                    self.output.draw_numbered_list(self.allprofiles)
                    # for e, p in enumerate(self.allprofiles):
                    #    print("Nummer {0}: {1}".format(e+1, p))
                    anzahl = len(self.allprofiles)
                    auswahl = Tools.getinput(ZAHl, bereich=range(1, anzahl + 1))
                    zuwechselndesprofil = self.allprofiles[auswahl - 1]
                    a = [self.dates, self.contacts]
                    self.backgrounddata.neudatenincome(self.actprofile, a)
                    self.backgrounddata.aktprofile(zuwechselndesprofil)
                    self.dates = self.backgrounddata.gettermine()
                    self.contacts = self.backgrounddata.getkontakte()
                    self.allprofiles = self.backgrounddata.getalleprofile()
                    self.actprofile = str(self.backgrounddata.getprofil())
                elif eingabe == 3:
                    pass
            elif haupteingabe == 5:
                if self.dates:
                    print("1. Nächsten x Termine anzeigen")
                    print("2. Letzten x Termine anzeigen")
                    choose = Tools.getinput(ZAHl, bereich=range(1, 3))
                    if choose == 1:
                        x = Tools.getinput(ZAHl)
                        t = self.get_next_n_dates(x)
                        self.output.draw_simple_list(t)
                    elif choose == 2:
                        x = Tools.getinput(ZAHl)
                        t = self.get_last_n_dates(x)
                        self.output.draw_simple_list(t)
                    else:
                        pass
                else:
                    print("Keine Termine zur Verfügung")
            elif haupteingabe == 6:
                a = [self.dates, self.contacts]
                self.backgrounddata.neudatenincome(self.actprofile, a)
                sys.exit()
            else:
                pass


if __name__ == '__main__':
    main = Main()
    main.main_loop()
