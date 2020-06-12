# Nach: Bernd Klein: Einführung in Python 3 

class PList(list):
    def __init__(self, list):
        super().__init__(list)
        
    def push(self, element):
        self.append(element)
        
        
class MeineListe(PList):

    def __init__(self, l):
        super().__init__(l)

    def splice(self, offset, length, replacement):
        self[offset:offset+length] = replacement


if __name__ == "__main__":
    x = MeineListe([33,456,8,34,99])
    x.push(47)
    print(x)
    x.splice(2,3,["Hey", "you"])
    print(x)
