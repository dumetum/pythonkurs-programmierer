# Die Idee der Kontoklasse stammt aus: Johannes Ernesti,Peter Kaiser: Python 3, Das umfassende Handbuch, Rheinwerk Computing 

class Konto:
    def __init__(self, kontoinhaber, kontonummer):
        self.kontoinhaber = kontoinhaber
        self.kontonummer = kontonummer
        self.kontostand = 0
        
    def __hash__(self):
        return hash(self.kontoinhaber) + hash(self.kontonummer)
        
    def __str__(self):
        return self.kontoinhaber + " " + str(self.kontonummer)
        
    def __eq__(self, other):
        if not type(other) == type(self):
            return false
        return (self.kontoinhaber == other.kontoinhaber and self.kontonummer == other.kontonummer)
        
konto1 = Konto("Schmitz", 4711)
    
dict = {}
dict[konto1] = "Konto1"
print(dict[konto1])

# Änderung eines Attributes, das den Hashwert bestimmt:
konto1.kontonummer = 4712
print(dict[konto1])
