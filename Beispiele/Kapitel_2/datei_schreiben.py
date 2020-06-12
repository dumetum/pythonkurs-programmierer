verbrauchsdaten = [23.1, 32.7,32.2]
fobj = open("verbrauchsdaten_out.txt", "w")

for verbrauch in verbrauchsdaten:
    fobj.write(str(verbrauch)+"\n")
fobj.close()

