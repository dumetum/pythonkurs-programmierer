# Die Idee der Kontoklasse stammt aus: Johannes Ernesti,Peter Kaiser: Python 3, Das umfassende Handbuch, Rheinwerk Computing 

class Konto:

    def __init__(self, inhaber, kontonummer, kontostand = 0, max_tagesumsatz = 1500):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand
        self.max_tagesumsatz = max_tagesumsatz
        self.umsatz_heute = 0
    
    def einzahlen(self, betrag):
        if betrag <= 0.0 or self.umsatz_heute + betrag > self.max_tagesumsatz:
            return False
        self.kontostand += betrag
        self.umsatz_heute += betrag
        return True

    def auszahlen(self, betrag):
        if betrag <= 0.0 or betrag > self.kontostand or self.umsatz_heute + betrag > self.max_tagesumsatz:
            return False
        self.kontostand -= betrag
        self.umsatz_heute += betrag
        return True

    def geldtransfer(self, ziel, betrag):
        if (betrag < 0 or self.umsatz_heute + betrag > self.max_tagesumsatz or ziel.umsatz_heute + betrag > ziel.max_tagesumsatz):
                return False
        else:
            self.kontostand -= betrag
            self.umsatz_heute += betrag
            ziel.kontostand += betrag
            ziel.umsatz_heute += betrag
        return True

    def zeige(self):
        return "Inhaber: {}, Kontonummer: {}, Kontostand: {:.2f}, heute umgesetzt {:.2f} von {:.2f}".format(self.inhaber, self.kontonummer, self.kontostand, self.umsatz_heute, self.max_tagesumsatz)


k1 = Konto("Heinz Meier", 567123, 12350.0)
k2 = Konto("Erwin Schmidt", 396754, 15000.0)

k1.geldtransfer(k2, 160)
k2.geldtransfer(k1, 1000)
k2.geldtransfer(k1, 500)

if k2.einzahlen(500):
    print("Einzahlen moeglich!")
else:
    print("Einzahlen nicht moeglich!")

print(k1.zeige())
print(k2.zeige())
