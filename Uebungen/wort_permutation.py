# Ein Text bleibt erstaunlich gut lesbar, wenn in jedem Wort die Buchstaben permutiert sind,
# so lange der erste und der letzte Buchstabe des Wortes erhalten bleiben.
#
# Probieren Sie dies aus, in dem Sie ein Programm schreiben, das fuer einen Text in einer
# Datei (z.B. text.txt) die Buchstaben in jedem Wort entsprechend permutiert und das
# Ergebnis in eine neue Datei schreibt (z.B. text_permutiert.txt)
#

import random

eingabedatei = open("text.txt","r")
ausgabedatei = open("text_permutiert.txt","w")

