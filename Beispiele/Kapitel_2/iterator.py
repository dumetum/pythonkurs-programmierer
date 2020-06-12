class MeinIterator:

    def __init__(self):
        self.__max = 10
        self.__count = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.__count > self.__max:
            raise StopIteration
        self.__count += 1
        return self.__count
        

i = MeinIterator()
for x in i:
    print(x)
    
    
