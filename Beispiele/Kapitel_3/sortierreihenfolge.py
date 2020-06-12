namen = [("Anton", "Wunderlich"), ("Berta", "Mueller"), ("Thomas", "Schmitz")]

def vorname(t):
    return t[0]

def nachname(t):
    return t[1]

namen.sort(key=vorname)
print(namen)

namen.sort(key=nachname)
print(namen)
