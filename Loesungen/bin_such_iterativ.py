l = ["Andreas", "Anton", "Bernd", "Berta", "Christian", "Dagobert", "Doris", "Emil", "Thomas", "Xaver", "Yps"]

def bin_search(liste, element):
    # Gibt den Index des Elementes in der Liste zurueck.
    # Ist das Element nicht vorhanden, wird -1 zurueckgegeben
    unten = 0
    oben = len(liste)-1
    gefunden = False
    
    while not gefunden and oben >= unten:
        mitte = (oben + unten) // 2
        print(str(unten) + ":" + str(oben))
        if liste[mitte] == element:
            gefunden = True
        if element < liste[mitte]:
            oben = mitte - 1
        else:
            unten = mitte + 1
    
    if gefunden:
        return mitte
    else:
        return -1

print(str(l) + "\n")

# Es ist immer sinnvoll die Randfaelle abzupruefen:
print("AA: " + str(bin_search(l, "AA")))
print("Andreas: " + str(bin_search(l, "Andreas")))
print("Yps: " + str(bin_search(l, "Yps")))
print("YY: " + str(bin_search(l, "YY")))

# Und noch zwei Faelle in der Mitte. Einer mit Treffer und einer ohne
print("Christian: " + str(bin_search(l, "Christian")))
print("Chris: " + str(bin_search(l, "Chris")))
