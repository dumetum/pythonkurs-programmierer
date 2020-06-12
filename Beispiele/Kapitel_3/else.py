# Nach "Einführung in Python 3" von Bernd Klein, Hanser-Verlag.

while True:
    try:
        zahl = input("Zahl eingeben: ")
        zahl = int(zahl)
    except Exception as e:
        print("Exception beim Lesen der Zahl")
    else:
        x = 10 / zahl
        print("Korrekte Zahl ungleich 0 eingegeben!")
        break
        
