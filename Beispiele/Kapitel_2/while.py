
summe = 0
anzahl = 0

while True:
    v = input("Verbrauch: ")
    if v == "ende":
        break
    summe += float(v)
    anzahl +=1

print("Durchschnittsverbrauch: ", summe / anzahl)
