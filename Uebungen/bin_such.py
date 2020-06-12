#
# Binäre Suche in einer geordneten Liste
#
# Idee: 
#   - Betrachte das Element in der Mitte:
#     - Das Element ist das gesuchte Element: Gebe den Index aus und fertig
#     - Das Element ist größer als das gesuchte Element: Suche (rekursiv) in der linken Hälfte der Liste
#     - Das Element ist kleiner als das gesuchte Element: Suche (rekursiv) in der rechten Hälfte der Liste
#
# Hinweis: Der Algorithmus kann iterativ und rekursiv implementiert werden.
#
# s. auch https://idea-instructions.com/binary-search/

l = ["Andreas", "Anton", "Bernd", "Berta", "Christian", "Dagobert", "Doris", "Emil", "Thomas", "Xaver", "Yps"]

#
# Bitte hier implementieren :-)
#



# Es ist immer sinnvoll die Randfaelle abzupruefen:
print(str(bin_search(l, "AA")))
print(str(bin_search(l, "Andreas")))
print(str(bin_search(l, "Yps")))
print(str(bin_search(l, "YY")))

# Und noch zwei Faelle in der Mitte. Einer mit Treffer und einer ohne
print(str(bin_search(l, "Christian")))
print(str(bin_search(l, "Chris")))
