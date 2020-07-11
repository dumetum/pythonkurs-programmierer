def konvertiere(s):
    if not s.isdigit():
        raise Exception("Der umzuwandelnde String besteht nicht nur aus Ziffern")
    return int(s)


while True:
    try:
        zahl = input("Zahl eingeben: ")
        zahl = konvertiere(zahl)
        print("Korrekte Zahl eingegeben!")
        break
    except Exception as e:
        print("Ausnahme: ", e)
        print("Keine Zahl!")
