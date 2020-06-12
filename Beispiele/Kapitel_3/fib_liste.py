# Erzeugung der ersen n Fibonacci-Zahlen als Liste.
# Nach: Michael Kofler: Python der Grundkurs
# Fibonacci-Zahlen: https://de.wikipedia.org/wiki/Fibonacci-Folge

def fib_liste(n):
    a, b = 0, 1
    erg_liste = []
    for _ in range(n):
        erg_liste += [a]
        a,b = b, a+b
    return erg_liste

fib_10 = fib_liste(10)
print("Ergebnistyp: ", type(fib_10))
print("Ergebnis: ", fib_10)