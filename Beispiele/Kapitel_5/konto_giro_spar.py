# Nach einer Idee von Johannes Ernesti,Peter Kaiser: Python 3, Das umfassende Handbuch, Rheinwerk Computing 

class Konto:

    def __init__(self, inhaber, kontonummer, kontostand = 0):
        self._inhaber = inhaber
        self._kontonummer = kontonummer
        self._kontostand = kontostand
    
    # Methode hat Zugriffsrecht protected, d.h. ist in Klasse und Unterklasse aufrufbar, aber nicht von außen
    def _pruefe_betrag(self,betrag):
        if betrag <= 0.0:
            raise Exception("Negativen Betrag nicht möglich!")
    
    def einzahlen(self, betrag):
        self._pruefe_betrag(betrag)
        self._kontostand += betrag
        return True

    def auszahlen(self, betrag):
        self._pruefe_betrag(betrag)
        self._kontostand -= betrag
        return True

    def zeige(self):
        return "Inhaber: " + self._inhaber + ", Kontonummer: " + str(self._kontonummer) + ", Kontostand: " + str(self._kontostand)


class Sparkonto(Konto):
    
    def __init__(self, inhaber, kontonummer, zinssatz, kontostand = 0):
        super().__init__(inhaber, kontonummer, kontostand)   
        self.__zinssatz = zinssatz
    
    def berechne_zinsen_pro_jahr(self):
        # Das gilt natürlich nur,wenn sich der kontostand ein Jahr nicht ändert. Ist halt ein Festgeld-Sparkonto :-)
        return self.__zinssatz / 100 * self._kontostand


class GiroKonto(Konto):
    
    def __init__(self, inhaber, kontonummer, kontostand = 0):
        super().__init__(inhaber, kontonummer, kontostand)
        
    def ueberweise(self, anderes_konto, betrag):
        self._pruefe_betrag(betrag)
        self.auszahlen(betrag)
        anderes_konto.einzahlen(betrag)


if __name__ == "__main__":
    k = Sparkonto("Sabine", 4610, 0.5, 100.00)
    print(k.zeige() + ": Zinsen: " + str(k.berechne_zinsen_pro_jahr()))
    
    k1 = GiroKonto("Fritz", 4611, 100.00)
    k2 = GiroKonto("Hans", 4612, 200.00)
    k1.ueberweise(k2,50)
    print(k1.zeige())
    print(k2.zeige())

