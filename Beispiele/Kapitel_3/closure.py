# Beispiel für eine Closure
# Nach: https://stackoverflow.com/questions/4020419/why-arent-python-nested-functions-called-closures

def make_printer(msg):
    def printer():
        print (msg)
    return printer

printer = make_printer('Hallo!')
printer()

printer = make_printer('Welt!')
printer()
 
