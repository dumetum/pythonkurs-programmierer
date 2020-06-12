# Ein einführendes Beispiel: Zahlenraten
# Nach Klein: Einführung in Python 3

import random

n = 20
zu_raten = random.randint(1,n)
rateversuch = 0
anzahl_versuche = 0

while zu_raten != rateversuch:
    rateversuch = int(input("Neuer Versuch: "))
    anzahl_versuche += 1
    if rateversuch > 0:
        if rateversuch == zu_raten:
            print("Treffer nach Versuchen: ", anzahl_versuche)
            break
        elif rateversuch > zu_raten:
            print("zu groß")
        else:
            print("zu klein")
    else:
        print("Auf Wiedersehen")
        break

 
