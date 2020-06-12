# Beispiel in abgewandelter Form entnommen aus Ernesti, Kaiser: Python 3 - Das umfassende Handbuch, Rheinwerk

class Kundendaten:

    def __init__(self, inhaber, kontonummer):
        self.inhaber = inhaber
        self.kontonummer = kontonummer

    def __str__(self):
        return "Inhaber: " + self.inhaber + ", Kontonummer: " + str(self.kontonummer)


class VerwalteterGeldbetrag:

    def __init__(self, anfangsbetrag):
        self.betrag = anfangsbetrag

    def einzahlen_moeglich(self, betrag):
        return True

    def auszahlen_moeglich(self, betrag):
        return True

    def einzahlen(self, betrag):
        if betrag < 0 or not self.einzahlen_moeglich(betrag):
            return False
        else:
            self.betrag += betrag
        return True

    def auszahlen(self, betrag):
        if betrag < 0 or not self.auszahlen_moeglich(betrag):
            return False
        else:
            self.betrag -= betrag
        return True

    def __str__(self):
        return "Betrag: {:.2f}".format(self.betrag)


class Konto(VerwalteterGeldbetrag):

    def __init__(self, kundendaten, kontostand):
        super().__init__(kontostand)
        self.kundendaten = kundendaten

    def geldtransfer(self, ziel, betrag):
        if self.auszahlen_moeglich(betrag) and ziel.einzahlen_moeglich(betrag):
            self.auszahlen(betrag)
            ziel.einzahlen(betrag)
            return True
        else:
            return False

    def __str__(self):
        return str(self.kundendaten) + ", " + super().__str__()


if __name__ == "__main__":
    kundendaten1 = Kundendaten("Klaus Maier", 4711)
    kundendaten2 = Kundendaten("Frank Schmitz", 4712)

    konto1 = Konto(kundendaten1, 1000)
    konto2 = Konto(kundendaten2, 2000)

    konto1.geldtransfer(konto2, 100)

    print(str(konto1))
    print(str(konto2))
