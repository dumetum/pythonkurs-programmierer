# Merge-Sort: Sortierung einer Liste
#
# Idee: Hat die zu sortierende Liste nur 0 oder 1 Element ist nichts zu tun. Die Liste kann unverändert zurückgeben werden.
#  Andernfalls: 
#  - Teile die Listen in zwei gleichgroße Listen
#  - Sortiere die Listen rekursiv
#  - "Mische" die beiden sortierten Listen zu einer sortierten Liste und gebe diese zurück
#
# siehe auch: https://idea-instructions.com/merge-sort/
#
# Dies ist natuerlich nur eine Uebung. In Python gibt es entsprechende Funktionen.


l = [123, 45, 67, 34, 23, 198, 263]

# Bitte hier implementieren :-)

print(merge_sort([]))
print(merge_sort([1]))
print(merge_sort([1,2]))
print(merge_sort([2,1]))

print(l)
print(merge_sort(l))
