# Schreiben Sie ein Programm:
# Eingabe: Eine Zeichenkette, die einen Satz darstellt, z.B.
#          "Dies ist ein langer Satz mit Nebensatz"
# Ausgabe: Die Länge des längsten Wortes des Satzes. Im Beispiel also 9
#
# Benutzen Sie keine Schleifen, sondern map und reduce
#
# Hinweis: Sei s eine Zeichenkette, dann liefert s.split() eine Liste der Wörter

from functools import reduce

satz = "Dies ist ein langer Satz mit Nebensatz"

# Aufspaltung nach Wörtern. Das Ergebnis ist eine Liste von Wörtern
wort_list = satz.split()
print(wort_list)

# Anwendung der Längenfunktion auf jedes Element der Liste. 
# Das Ergebnis ist ein Map-Objekt
# - aus dem man eine Liste konstruieren kann
# - über das man iterieren kann
# - auf das man "reduce" anwenden kann
laengen_list = map(len, wort_list)
print(laengen_list)

# Die Liste (das Map-Objekt) wird auf ein Ergebnis reduziert, indem die
# Max-Funktion auf jeweils zwei Elemente angewendet wird.
max_laenge = reduce(max, laengen_list)
print(max_laenge)