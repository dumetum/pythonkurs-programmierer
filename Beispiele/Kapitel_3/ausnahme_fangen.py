# Nach "Einführung in Python 3" von Bernd Klein, Hanser-Verlag.

while True:
    try:
        zahl = input("Zahl eingeben: ")
        zahl = int(zahl)
        print("Korrekte Zahl eingegeben!")
        break
    except Exception as e:
        print("Ausnahme: ", e, "vom Typ ", type(e))
        print("Keine Zahl!")
