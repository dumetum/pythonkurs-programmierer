# Die Idee der Kontoklasse stammt aus: Johannes Ernesti,Peter Kaiser: Python 3, Das umfassende Handbuch, Rheinwerk Computing 

class Konto():

    def __init__(self, kontoinhaber):
        self.__kontoinhaber = kontoinhaber
        self.__kontostand = 0.0

    # Nun privat, damit die Methode nicht direkt aufgerufen wird
    def __set_kontoinhaber(self, kontoinhaber):
        self.__kontoinhaber = kontoinhaber.upper()

    def __get_kontoinhaber(self):
        print("Getter von kontoinhaber")
        return self.__kontoinhaber

    kontoinhaber = property(__get_kontoinhaber, __set_kontoinhaber)

k = Konto("Maier")
print(k.kontoinhaber)
k.kontoinhaber = "schulz"
print(k.kontoinhaber)

