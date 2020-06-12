infinity = float("inf")
minus_infinity = float("-inf")

x = 1 + infinity
print(x) # inf

x = 1 + minus_infinity
print(x) #-inf

x = infinity / minus_infinity
print(x) # nan
 
