# Verhinderung des Programmabruchs durch Abfangen der Exception

def f1(x):
    return f2(x)

def f2(x):
    return f3(x)

def f3(x):
    return 1 / x


while True:
    eingabe = input("Geben Sie eine ganze Zahl ein (e für Ende): ")
    if eingabe == "e":
        break
    zahl = int(eingabe)

    try:
        ergebnis = f1(zahl) + f1(7)
        print("Das Ergebnis ist: " + str(ergebnis))
    except Exception as e:
        print("Da ist wohl etwas schief gegangen: " + str(e))
