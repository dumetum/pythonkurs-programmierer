# Die Idee der Kontoklasse stammt aus: Nach Johannes Ernesti,Peter Kaiser: Python 3, Das umfassende Handbuch, Rheinwerk Computing 

class Konto:

    def __init__(self, kontoinhaber, kontostand):
        self.kontoinhaber = kontoinhaber
        self.kontostand = kontostand

    def __str__(self):
        return "Kontoinhaber: " + self.kontoinhaber + ", Kontostand: " + str(self.kontostand)

    def __repr__(self):
        return "Konto('" + self.kontoinhaber + "'," + str(self.kontostand) + ")"

k = Konto("Maier", 100.0)
print(str(k))
print(repr(k))

k_kopie = eval(repr(k))
print(str(k_kopie))
