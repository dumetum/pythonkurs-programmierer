# Umwandlung roemische Zahlen in Dezimalzahlen

roem_to_dez_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
roem_zahl_str = 'MCMLXVI'

dezimal_zahl = 0
prev = 0
for zeichen in roem_zahl_str:
    current = roem_to_dez_dict[zeichen]
    if prev < current:
        dezimal_zahl -= prev
    else:
        dezimal_zahl += prev
    prev = current
dezimal_zahl += current

print("Dezimalwert:", dezimal_zahl)
