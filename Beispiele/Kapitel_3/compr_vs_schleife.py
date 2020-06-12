import time as t

t1 = t.process_time()

for i in range(1000000):
    i**2
    
t2 = t.process_time()

[x**2 for x in range(1000000)]

t3 = t.process_time()

print("Zeit Schleife: " + str(t2 - t1))

print("Zeit Comprehension: " + str(t3 - t2))
