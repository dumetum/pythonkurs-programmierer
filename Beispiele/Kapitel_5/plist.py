# Aus: Bernd Klein: Einführung in Python 3 

class PList(list):
    def __init__(self, list):
        super().__init__(list)
        
    def push(self, element):
        self.append(element)
        
if __name__ == "__main__":
    x = PList([33,456,8,34,99])
    x.push(47)
    print(x)
