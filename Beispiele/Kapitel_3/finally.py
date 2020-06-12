# Nach "Einführung in Python 3" von Bernd Klein, Hanser-Verlag.

while True:
    try:
        zahl = input("Zahl eingeben: ")
        zahl = int(zahl)
        x = 10 / zahl
        print("Korrekte Zahl ungleich 0 eingegeben!")
        break
    except ValueError as ve:
        print("ValueError: ", ve)
        print("Keine Zahl!")
    finally:
        print("Wird trotz break im fehlerfreien Fall ausgeführt.")
        print("Wird auch ausgeführt bei Division durch Null - Ausnahme")
