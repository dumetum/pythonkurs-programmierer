l = ["Andreas", "Anton", "Bernd", "Berta", "Christian", "Dagobert", "Doris", "Emil", "Thomas", "Xaver", "Yps"]

def bin_search(liste, element):
    # Gibt den Index des Elementes in der Liste zurueck.
    # Ist das Element nicht vorhanden, wird -1 zurueckgegeben
    return bin_search_range(liste, element, 0, len(liste)-1)

# Start-Index und Ende-Index jeweils inklusive
def bin_search_range(liste, element, start_index, ende_index):
    if ende_index < start_index:
        return -1
    mitte = (start_index + ende_index ) // 2
    if liste[mitte] == element:
        return mitte
    if element < liste[mitte]:
        return bin_search_range(liste, element, start_index, mitte - 1)
    else:
        return bin_search_range(liste, element, mitte + 1, ende_index)

print(str(l) + "\n")

# Es ist immer sinnvoll die Randfaelle abzupruefen:
print("AA: " + str(bin_search(l, "AA")))
print("Andreas: " + str(bin_search(l, "Andreas")))
print("Yps: " + str(bin_search(l, "Yps")))
print("YY: " + str(bin_search(l, "YY")))

# Und noch zwei Faelle in der Mitte. Einer mit Treffer und einer ohne
print("Christian: " + str(bin_search(l, "Christian")))
print("Chris: " + str(bin_search(l, "Chris")))
