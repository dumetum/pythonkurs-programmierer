
satz = input("Geben Sie einen Satz ein: ")

aktuelle_laenge = 0
maximale_laenge = 0
 
for zeichen in satz:
    if zeichen == " ":
        if aktuelle_laenge > maximale_laenge:
            maximale_laenge = aktuelle_laenge
        aktuelle_laenge = 0
    else:
        aktuelle_laenge += 1

if aktuelle_laenge > maximale_laenge:
    maximale_laenge = aktuelle_laenge
    
print("Das längste Wort in dem Satz hat", maximale_laenge, "Zeichen")