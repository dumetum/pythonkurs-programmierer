# Ein Text bleibt erstaunlich gut lesbar, wenn in jedem Wort die Buchstaben permutiert sind,
# so lange der erste und der letzte Buchstabe des Wortes erhalten bleiben.
#
# Probieren Sie dies aus, in dem Sie ein Programm schreiben, das fuer einen Text in einer
# Datei (z.B. text.txt) die Buchstaben in jedem Wort entsprechend permutiert und das
# Ergebnis in eine neue Datei schreibt (z.B. text_permutiert.txt)
#
# Bemerkung:
# Das folgende Programm funktioniert seltsamerweise bei der Verwendung von Umlauten
# nicht unter Windows, sondern nur unter Linux.
# Wenn die Methode permutiere_alle_buchstaben das übergebene Wort zurück gibt, klappt es auch unter
# Windows. Umlaute sind also unter Windows prinzipiell kein Problem.

import random

trenner_liste = [" ", "\n", ";", ".", ",", "!"]

eingabedatei = open("text.txt","r")
ausgabedatei = open("text_permutiert.txt","w")

def permutiere_alle_buchstaben(wort):
    ret_wort = ""
    index_liste = [i for i in range(0,len(wort))]

    while index_liste:
        index_aus_liste = random.randint(0,len(index_liste)-1)
        index_wort = index_liste[index_aus_liste]
        index_liste.remove(index_wort)
        ret_wort = ret_wort + wort[index_wort]

    return ret_wort

def permutiere(wort):
    if len(wort) <= 2:
        return wort
    
    rueckgabe_wort = wort[0] + permutiere_alle_buchstaben(wort[1:len(wort)-1]) + wort[-1]
       
    return rueckgabe_wort

def permutiere_woerter(zeile):
    return_zeile = ""
    aktuelles_wort = ""
    for zeichen in zeile:
        if zeichen in trenner_liste:
            if aktuelles_wort != "":
                return_zeile = return_zeile + permutiere(aktuelles_wort) + zeichen
                aktuelles_wort = ""
            else:
                return_zeile = return_zeile + zeichen
        else:
            # Da immer ein neuer String gebildet wird, ist es nicht effizient, das akutelle Wort so zeichenweise zu bestimmen.
            # Besser wäre es, den Wortanfang und das Wortende zu bestimmen.
            # Fuer eine Uebung ist es aber erst mal ok
            aktuelles_wort = aktuelles_wort + zeichen
            
    if aktuelles_wort != "":
        return_zeile = return_zeile + permutiere(aktuelles_wort)
        
    return return_zeile

for zeile in eingabedatei:
    zeile = permutiere_woerter(zeile)
    ausgabedatei.write(zeile)
    
ausgabedatei.close()
eingabedatei.close()
    
