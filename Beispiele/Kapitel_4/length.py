# Nach "Einführung in Python 3" von Bernd Klein, Hanser-Verlag.

class Length:
    __metric = { "mm" : 0.001,
                 "cm" : 0.01,
                 "m" : 1,
                 "km" : 1000,
                 "in" : 0.0254,
                 "ft" : 0.3048,
                 "yd" : 0.9144,
                 "mi" : 1609.344 }
    
    def __init__(self, value, unit = "m" ):
        self.value = value
        self.unit = unit

    def Converse2Metres(self):
        return self.value * Length.__metric[self.unit]

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            l = self.Converse2Metres() + other
        else:
            l = self.Converse2Metres() + other.Converse2Metres()
        return Length(l / Length.__metric[self.unit], self.unit )
        
    def __str__(self):
        return str(self.value) + " " + self.unit
    
    def __repr__(self):
        return "Length" + str((self.value, self.unit))

if __name__ == "__main__":
    x = Length(4,"km")
    print("Länge x = " + str(x) + " (" + repr(x) + ")")
    
    y = Length(3,"mm")
    print("Länge y = " + str(y) + " (" + repr(y) + ")")
    
    z = x + y
    print("\nErgebnis der Addition z = " + str(z) + " (" + repr(z) + ")")    
    x = Length(4,"mm")
    
