# Die Idee, die Objektorientierung an Hand einer Kontoklasse einzuführen, stammt aus dem Buch
# Johannes Ernesti,Peter Kaiser: Python 3, Das umfassende Handbuch, Rheinwerk Computing 

class Konto:

    def __init__(self):
        self.__kontostand = 0

k = Konto()
print(k.__kontostand)
