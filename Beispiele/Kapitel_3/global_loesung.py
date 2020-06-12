
s = "Hallo"

def sage_hallo():
    global s
    print(s)
    s = "Auf Wiedersehen"
    print(s)

sage_hallo()
print(s)
