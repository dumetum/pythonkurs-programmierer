# Verhinderung des Programmabruchs ohne Exception

def f1(x):
    erg = f2(x)
    if erg == None:
        return None
    return 1 + f2(x)

def f2(x):
    erg = f3(x)
    if erg == None:
        return None
    return 1 + f3(x)

def f3(x):
    if x == 0:
        return None
    return 1 / x

while True:
    eingabe = input("Geben Sie eine ganze Zahl ein (e für Ende): ")
    if eingabe == "e":
        break
    zahl = int(eingabe)

    erg1 = f1(zahl)
    erg2 = f1(7)

    if erg1 == None or erg2 == None:
        print("Da ist wohl etwas schief gegangen")
    else:
        ergebnis = erg1 + erg2
        print("Das Ergebnis ist: " + str(ergebnis))
