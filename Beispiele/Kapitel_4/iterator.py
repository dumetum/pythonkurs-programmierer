
class RueckwaertsZaehler:
    
    def __init__(self, startwert):
        self.wert = startwert
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.wert >= 0:
            self.wert -= 1
            return self.wert + 1
        else:
            raise StopIteration()
            
            
for i in RueckwaertsZaehler(10):
    print(i)
        
    
