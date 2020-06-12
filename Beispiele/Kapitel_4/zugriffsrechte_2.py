# Die Idee der Kontoklasse stammt aus: Johannes Ernesti,Peter Kaiser: Python 3, Das umfassende Handbuch, Rheinwerk Computing 

class Konto:

    def __init__(self):
        self.__kontostand = 0

    def print_kontostand(self):
        print(str(self.__kontostand))

k = Konto()

# Das geht nicht:
# print(k.__kontostand)

# Das folgende geht wohl, erzeugt aber ein Klassenattribut
k.__kontostand = 100.0
k.print_kontostand()
print(k.__dict__)
