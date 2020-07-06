
def f():
    x = 12345
    print("id(x)", id(x))
    return x
    
y = f()
print("id(y)", id(y))