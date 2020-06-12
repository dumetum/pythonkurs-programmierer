
class NotHashable:
    __hash__ = None
    
o = NotHashable()
    
dict = {}
dict[o] = 1

    
