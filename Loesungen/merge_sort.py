l = [123, 45, 67, 34, 23, 198, 263]

def merge_sort(liste):
    print("Sort: ", liste)
    if len(liste) <= 1:
        return liste
    mitte = len(liste) // 2
    l1 = merge_sort(liste[:mitte])
    l2 = merge_sort(liste[mitte:])
    return merge(l1, l2)

def merge(liste1, liste2):
    print("Merge ", liste1, liste2)
    ret_list = []
    i1 = 0
    i2 = 0
    while i1 < len(liste1) or i2 < len(liste2):
        # So lange die Elemente der Liste 1 noch kleiner sind als die dier Liste 2 (oder Liste2 schon abgearbeitet ist)
        while i1 < len(liste1) and (i2 >= len(liste2) or liste1[i1] <= liste2[i2]):
            ret_list.append(liste1[i1])
            i1 += 1
        while i2 < len(liste2) and (i1 >= len(liste1) or liste2[i2] <= liste1[i1]):
            ret_list.append(liste2[i2])
            i2 += 1
    return ret_list

# Beachte: Das Ganze hat nur dann die gewuenschte Effizienz, wenn
# das Bauen der neuen Liste effizient ist, d.h. insbesondere, wenn
# die Append-Methode effizient ist. Wie das hier in Python implementiert ist,
# wissen wir nicht (und kann uns auch egal sein). Daher handelt es sich nur um eine Uebung. 
# Python bietet die entsprechenden Funktionalitaeten, die man auch nutzen sollte.  

print(merge_sort([]))
print(merge_sort([1]))
print(merge_sort([1,2]))
print(merge_sort([2,1]))

print(l)
print(merge_sort(l))
