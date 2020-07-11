
fobj = open("verbrauchsdaten.txt", "r")

for line in fobj:
    print("Verbrauch: ", line)
    
fobj.close
