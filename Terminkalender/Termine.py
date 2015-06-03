__author__ = 'Saelind'
import datetime
import sys
import Tools

TEXT = 0
ZAHl = 1
DATUM = 2


class Termine:
    def __init__(self, datum, betreff, textinhalt, profile='Default'):
        self.datum = datum
        self.betreff = betreff
        self.textinhalt = textinhalt
        self.neueeingabe = 'Neue Eingabe: '

    def display(self):
        print(self.datum, self.betreff, self.textinhalt)

    def editdatum(self):
        print("Aktuelles Datum: %s" % self.getdatum())
        neuesdatum = Tools.getinput(DATUM, nachricht=self.neueeingabe)
        self.datum = self.datum.replace(neuesdatum[0], neuesdatum[1], neuesdatum[2])
        print(self.datum)

    def editbetreff(self):
        print('Aktuelle Termin Betreff: %s' % self.betreff)
        neuerbetreff = Tools.getinput(TEXT, nachricht=self.neueeingabe)
        self.betreff = neuerbetreff

    def edittextinhalt(self):
        print('Aktueller Textinhalt: %s' % self.textinhalt)
        neuertextinhalt = Tools.getinput(TEXT, nachricht=self.neueeingabe)
        self.textinhalt = neuertextinhalt

    def getdatum(self):
        return self.datum

    def getbetreff(self):
        return self.betreff

    def gettextinhalt(self):
        return self.textinhalt

    def del_self(self):
        del self
