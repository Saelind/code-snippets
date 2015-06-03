__author__ = 'Saelind'
import Termine
import Profile

class Output():
    def __init__(self):
        self.draw_main_board_text = ["1. Neuer Termin", "2. Termine bearbeiten", "3. Termine abfragen",
                                     "4. Profil optionen",
                                     "5. X Termine anzeigen", "6. Beenden"]
        self.draw_edit_dates_text = ["Was möchten sie machen?", "1. Datum ändern", "2. Betreff ändern",
                                     "3. Textinhalt ändern", "4. Termin löschen", "5. Zurück"]
        self.draw_profile_options_text = ["Was möchten sie machen?", "1. Neues Profil erstellen", "2. Profile wechseln",
                                          "3. Zurück"]

    def draw_str(self, string):
        print(str(string))

    def draw_main_board(self):
        print()
        for s in self.draw_main_board_text:
            print(s)

    def draw_numbered_list(self, sachen):    # Listet alle Termine nach Reihenfolge Index, ändern zu gibt eine Liste
                                            # nummeriert aus
        for e, i in enumerate(sachen):
            if isinstance(i, Termine.Termine):
                d = i.getdatum()  # Holt das Datum der Termin Klasse und speichert sie in d
                b = i.getbetreff()  # Holt den Betreff der Termin Klasse und speichert sie in b
                print("Nummer {0}: {1} {2}".format(e + 1, d, b))
            else:
                print("Nummer {0}: {1}".format(e+1, i))

    def draw_simple_list(self, dates):
        for i in dates:
            datum = i.getdatum()
            betreff = i.getbetreff()
            inhalt = i.gettextinhalt()
            print(datum, betreff, inhalt)

    def draw_edit_dates(self):
        for s in self.draw_edit_dates_text:
            print(s)

    def draw_profile_options(self):
        for s in self.draw_profile_options_text:
            print(s)
