
class Zeitspanne:

    def __init__(self, stunden, minuten):
        self.__minuten = minuten + 60 * stunden
        
    def __str__(self):
        return str(self.__minuten // 60) + ":" + str(self.__minuten % 60)
        
    def __add__(self, other):
        if type(other) == int:
            return Zeitspanne(0, self.__minuten + other)
        if type(other) == Zeitspanne:
            return Zeitspanne(0,self.__minuten + other.__minuten)
        
z1 = Zeitspanne(1,20)
z2 = Zeitspanne(0,40)
z3 = z1 + z2
z4 = z1 + 50
# z5 = 50 + z1

print(str(z1) + "+" + str(z2) + " = " + str(z3))
print(str(z1) + "+" + str(50) + " = " + str(z4))
#print(str(50) + "+" + str(z1) + " = " + str(z5))
