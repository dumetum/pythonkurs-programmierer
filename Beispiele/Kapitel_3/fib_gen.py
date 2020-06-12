# Generator für die ersen n Fibonacci-Zahlen.
# Nach: Michael Kofler: Python der Grundkurs
# Fibonacci-Zahlen: https://de.wikipedia.org/wiki/Fibonacci-Folge

def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a,b = b, a+b

fib_10 = fib_gen(10)
print("Ergebnistyp: ", type(fib_10))
print("Ergebnis: ", fib_10)

# Zugriffsmöglichkeiten:

# Ergebnis in Liste umwandeln
print("Liste: ", list(fib_10))

# For Schleife
fib_10 = fib_gen(10)
print("For Schleife: ")
for zahl in fib_10:
    print(str(zahl))

# Mit next den nächsten Wert abfragen. Wenn der Generator keinen Wert mehr
# liefert, wird eine StopIteration- Ausnahme geworfen
#  (Ausnahmen werden später noch genauer vorgestellt).
fib_10 = fib_gen(10)
print("Next: ")
while True:
    print(next(fib_10))