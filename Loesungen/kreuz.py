# Schreiben Sie ein Programm, das ein Kreuz auf den Bildschirm zeichnet.
# Die Anzahl der Zeile sind eine Programmeingabe. Bei der Eingabe 5 soll
# dass Kreuz also folgendermassen aussehen:
#
# x   x
#  x x
#   x
#  x x
# x   x
#
# Testen Sie insbesondere einen Fall mit gerader Zeilenanzahl und einen Fall
# mit ungerader Zeilenanzahl

anzahl_zeilen = int(input("Geben Sie die Anzahl der Zeilen ein: "))

for nummer_aktuelle_zeile in range(0,anzahl_zeilen):
    position_x1 = nummer_aktuelle_zeile
    position_x2 = anzahl_zeilen - 1 - nummer_aktuelle_zeile
    if position_x1 > position_x2:
        max_x = position_x1
        min_x = position_x2
    else:
        max_x = position_x2
        min_x = position_x1
    zwischenraum = max_x - min_x - 1
    if zwischenraum < 0:
        # In der Mitte steht nur ein x
        zeile = min_x * " " + "x"
    else:
        # Sonst werden zwei x gezeichnet mit dem entsprechenden Zwischenraum
        zeile = min_x * " " + "x" + zwischenraum * " " + "x"   
    print(zeile)   
