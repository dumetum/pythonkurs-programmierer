
summe = 0
anzahl = 0

while True:
    v = input("Verbrauch: ")
    if v == "ende":
        break
    verbrauch = float(v)
    if verbrauch < 0.0:
        print("Ein negativer Verbrauch ist nicht sinnvoll!")
        continue
    summe += float(verbrauch)
    anzahl +=1

print("Durchschnittsverbrauch: ", summe / anzahl)
