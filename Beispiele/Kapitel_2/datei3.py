
fobj = open("verbrauchsdaten.txt", "r")

verbrauch = 0
for line in fobj:
    print("Verbrauch: ", line)
    verbrauch += float(line.strip())
fobj.close

print("Gesamtverbrauch: ", verbrauch)
