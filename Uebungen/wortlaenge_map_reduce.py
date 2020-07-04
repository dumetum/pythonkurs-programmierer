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

