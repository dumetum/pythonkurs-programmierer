# Die Idee der Kontoklasse stammt aus: Johannes Ernesti,Peter Kaiser: Python 3, Das umfassende Handbuch, Rheinwerk Computing 

class Konto():

    def __init__(self, kontoinhaber):
        self.__kontostand = 0.0
        self.__kontoinhaber = kontoinhaber

    # Jetzt hat der Setter einen Mehrwert. Durch die Verwendung
    # des Setters muss man den Rest des Programms nicht aendern
    def set_kontoinhaber(self, kontoinhaber):
        self.__kontoinhaber = kontoinhaber.upper()

    def get_kontoinhaber(self):
        return self.__kontoinhaber

k = Konto("Maier")
print(k.get_kontoinhaber())
k.set_kontoinhaber("schulz")
print(k.get_kontoinhaber())

