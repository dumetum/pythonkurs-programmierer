def pruefe_zwei_damen(spalte1, spalte2, zeilen_differenz):
    if spalte1 == spalte2 or spalte1 == spalte2 + zeilen_differenz or spalte1 == spalte2 - zeilen_differenz:
        return False
    else:
        return True       

def pruefe_stellung_fuer_aktuelle_zeile(stellung, aktuelle_zeile, aktuelle_spalte):
    zu_testende_zeile = aktuelle_zeile
    zu_testende_spalte =  aktuelle_spalte   
    for zeile in range(0,zu_testende_zeile):
        spalte_in_zeile = stellung[zeile]
        zeilen_diff = zu_testende_zeile - zeile
        if not pruefe_zwei_damen(zu_testende_spalte, spalte_in_zeile, zeilen_diff):
            return False
    return True

# Diese Methode hat als Seiteneffekt, die Liste stellung zu verändern.
# Das ist hier in Ordnung, da es sich um eine "interne" Funktion handelt,
# die für den "Anwender" nicht sichtbar sein sollte.
def finde_loesung(aktuelle_zeile, aktuelle_stellung, anzahl_zeilen, anzahl_spalten):
    if aktuelle_zeile >= anzahl_zeilen:
        return True   

    for zu_testende_spalte in range(0, anzahl_spalten):
        aktuelle_stellung[aktuelle_zeile] = zu_testende_spalte
        if pruefe_stellung_fuer_aktuelle_zeile(aktuelle_stellung, aktuelle_zeile, zu_testende_spalte): 
            gibt_es_loesung = finde_loesung(aktuelle_zeile + 1, aktuelle_stellung, anzahl_zeilen, anzahl_spalten)           
            if gibt_es_loesung:
                return True
    return False

# Das ist die aufzurufende "Schnittstellenfunktion" ohne Seiteneffekte
# nach dem EVA-Prinzip
def loese_damen_problem(anzahl_zeilen, anzahl_spalten):
    stellung = [0] * anzahl_zeilen
    gibt_es_loesung = finde_loesung(0, stellung, anzahl_zeilen, anzahl_spalten)
    if gibt_es_loesung:
        return stellung
    else:
        return None

anzahl_zeilen = int(input("Anzahl der Zeilen: "))
anzahl_spalten = int(input("Anzahl der Spalten: "))
loesung = loese_damen_problem(anzahl_zeilen, anzahl_spalten)
if loesung:
    print("Eine Loesung ist:", loesung)
else:
    print("Es gibt keine Lösung!")