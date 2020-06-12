# Aus einer Liste von ganzen Zahlen sollen alle negativen Zahlen gelöscht werden.
# Während der Schleife wird also die Liste veraendert.


# Fall 1: Schleife über die Liste selbst. Das Ergebnis ist fehlerhaft:
liste = [6,3,-2,5,-8, -8, -3, 9]

for zahl in liste:
    if zahl < 0:
        liste.remove(zahl)
        
print("Liste nach remove: ", liste)

# Fall 2: Schleife über eine Kopie der Liste. Das Ergebnis ist korrekt!
liste = [6,3,-2,5,-8, -8, -3, 9]

for zahl in liste[:]:
    if zahl < 0:
        liste.remove(zahl)
        
print("Liste nach remove: ", liste)
