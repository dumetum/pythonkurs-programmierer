# Schreibe ein Programm, das erkennt, ob eine Zahl „fröhlich“ ist oder nicht.
# Eine Fröhliche Zahl ist eine Zahl, bei der die Summe der Quadrate ihrer Ziffern „auf die Dauer“ 1 ergibt. Beispiel:
# 19 -> 1^2 + 9^2 = 82 -> 8^2 + 2^2 = 68 -> 6^2 + 8^2 = 100 -> 1^2 + 0^2 + 0^2 = 1 
#
# Die Idee der "fröhlichen Zahlen" stammt aus: https://ccd-school.de/coding-dojo/

zahl = 12345
gepruefte_zahlen = []

while zahl not in gepruefte_zahlen and zahl != 1:
    gepruefte_zahlen.append(zahl)
    zahl_str = str(zahl)
    zahl = 0
    for ziffer_str in zahl_str:
        zahl += int(ziffer_str) ** 2
    print("Neue Zahl: " + str(zahl))
    
        
if zahl == 1:
    print("Fröhlich!")
else:
    print("Nicht fröhlich")
