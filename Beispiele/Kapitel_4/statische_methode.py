# Die Idee der Kontoklasse stammt aus: Nach Johannes Ernesti,Peter Kaiser: Python 3, Das umfassende Handbuch, Rheinwerk Computing 

class Konto:

    anzahl = 0
    
    def print_anzahl1():
        print(Konto.anzahl)
        
    @staticmethod
    def print_anzahl2():
        print(Konto.anzahl)

    def __init__(self):
        Konto.anzahl += 1


if __name__ == "__main__":
    k1 = Konto()
    print(str(Konto.anzahl))

    k2 = Konto()
    print(str(Konto.anzahl))
    
    Konto.print_anzahl1()
    
    # Das geht nicht:
    # k2.print_anzahl1()

    Konto.print_anzahl2()
    k1.print_anzahl2()
