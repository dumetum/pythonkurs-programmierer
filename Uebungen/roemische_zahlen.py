# Umwandlung roemische Zahlen in Dezimalzahlen
#
# Algorithmus:
#  Die zugehörigen Dezimalwerte werden addiert.
#  Ausnahme: Steht ein Symbol mit einem kleineren Wert vor einem Symbol mit einem größeren Wert, wird der kleinere Wert subtrahiert.
#            Beispiel: IV = -1 + 5

roem_to_dez_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
roem_zahl_str = 'MCMLXVI'

# Umrechung in dezimal_zahl


print("Dezimalwert:", dezimal_zahl)
