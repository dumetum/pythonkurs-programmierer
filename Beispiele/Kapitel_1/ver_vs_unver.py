# Veränderliche vs. unveränderliche Datentypen
# nach Ernesti, Kaiser: Python 3 - das umfassende Handbuch

s1 = "Wasser"
s2 = s1
s1 += "flasche" # Es wird ein neuer String erzeugt und s1 zugewiesen

print(s1) # Wasserflasche
print(s2) # Wasser

l1 = [1,2]
l2 = l1
l2 += [3,4] # Die bestehende Liste wird verändert
print(l1) # [1,2,3,4]
print(l2) # [1,2,3,4]



