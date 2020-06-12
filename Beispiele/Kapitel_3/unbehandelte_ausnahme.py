def f1():
    f2()

def f2():
    return 1 / 0

f1()
