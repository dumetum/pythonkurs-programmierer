# Die Idee der Kontoklasse stammt aus: Johannes Ernesti,Peter Kaiser: Python 3, Das umfassende Handbuch, Rheinwerk Computing 

class Konto:

    def __init__(self, inhaber, kontonummer, kontostand = 0):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand
    
    def einzahlen(self, betrag):
        if betrag <= 0.0:
            raise Exception("Einzahlen eines negativen Betrages nicht möglich!")
        self.kontostand += betrag
        return True

    def auszahlen(self, betrag):
        if betrag <= 0.0:
            raise Exception("Auszahlung eines negativen Betrages nicht möglich!")
        self.kontostand -= betrag
        return True

    def zeige(self):
        return "Inhaber: " + self.inhaber + ", Kontonummer: " + str(self.kontonummer) + ", Kontostand: " + str(self.kontostand)


if __name__ == "__main__":

    # Erzeugung eines Objektes vom Typ Konto und Zuweisung zu einer Variablen. Der Interpreter rufe automatisch die __init__()-Methode auf
    k = Konto("Fritz", 4611, 100.00)
    
    # Aufruf einer Methode für ein Objekt. Python wandelt den Aufruf intern um in Konto.einzahlen(k, 100)
    k.einzahlen(100)
    print(k.zeige())
  
    k.auszahlen(50)
    print(k.zeige())
