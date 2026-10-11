from array import array
import random

n = int(input("Введіть N: "))

A = array('i', [random.randint(0, n) for i in range(4)])
B = array('i', [random.randint(0, n) for i in range(18)])
C = array('i', [])

for x in B:
    if x not in A:
        C.append(x)

print("Масив A:", A)
print("Масив B:", B)
print("Масив C:", C)