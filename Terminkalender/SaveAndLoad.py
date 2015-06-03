__author__ = 'Saelind'
import pickle
import os


class SaveAndLoad:
    def __init__(self, dateiname='save.dat'):
        self.daten = {}
        self.dateiname = dateiname
        self.loaddata()

    def aktprofile(self, akt):
        self.daten['akt'] = akt

    def savedata(self):
        speichere_daten = open('save.dat', 'wb')
        pickle.dump(self.daten, speichere_daten)
        speichere_daten.close()

    def loaddata(self):
        if os.path.isfile("save.dat"):
            lade_daten = open('save.dat', 'rb')
            self.daten = pickle.load(lade_daten)
            lade_daten.close()
        else:
            self.aktprofile('Default')
            self.daten['Default'] = [[], []]

    def getdata(self):
        a = self.daten['akt']
        return self.daten[a]

    def getprofil(self):
        return self.daten['akt']

    def gettermine(self):
        a = self.daten['akt']
        b = self.daten[a]
        c = b[0]
        return c

    def getkontakte(self):
        a = self.daten['akt']
        b = self.daten[a]
        c = b[1]
        return c

    def getalleprofile(self):
        a = []
        for x in sorted(self.daten.keys()):
            if x != 'akt':
                a.append(x)
        return a

    def neudatenincome(self, profile, newdata):    # geänderte Daten mit den alten Daten zusammenführen
        if not self.daten['akt'] == profile:
            self.daten['akt'] = profile
        self.daten[profile] = newdata
        self.savedata()

    def datendisplay(self):
        print(self.daten)
