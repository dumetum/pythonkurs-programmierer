# Bei Eingabe einer 0 bricht das Programm ab.

def f1(x):
    return 1 + f2(x)

def f2(x):
    return 1 + f3(x)

def f3(x):
    return 1 / x

while True:
    eingabe = input("Geben Sie eine ganze Zahl ein (e für Ende): ")
    if eingabe == "e":
        break
    zahl = int(eingabe)
    ergebnis = f1(zahl) + f1(7)
    print("Das Ergebnis ist: " + str(ergebnis))

