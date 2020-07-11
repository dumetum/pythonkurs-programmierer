monate = ['Jan','Feb','Mar','Apr','Mai','Jun']

verbrauch1 = ['Jan:20.1','Feb:23.2','Mar:31.5']
verbrauch2 = ['Jan:20.1','Feb:23.2','xxx:31.5']
verbrauch3 = ['Jan:20.1','Feb:23.2','Mar:xxxx']

def berechne_durchschnitt(verbrauch):
    summe = 0
    anzahl = 0

    for monat in verbrauch:
        try:
            summe += bestimme_verbrauch(monat)
            anzahl += 1
        except ValueError as ve:
            print("Ungueltiger Wert in ", monat)
            print("Monat wird uebersprungen.")

    durchschnitt = summe / anzahl
    print("Durchschnittlicher Verbrauch: ", durchschnitt)


def bestimme_verbrauch(monat):
    verbrauch = float(monat.split(":")[1].strip())
    return verbrauch


print("Verbrauch 1: ")
berechne_durchschnitt(verbrauch1)

print("Verbrauch 2: ")
berechne_durchschnitt(verbrauch2)

print("Verbrauch 3: ")
berechne_durchschnitt(verbrauch3)
