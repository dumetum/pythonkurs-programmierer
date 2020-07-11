
fobj = open("verbrauchsdaten.txt", "r")

for line in fobj:
    print("Verbrauch: ", line.strip())
    
fobj.close
