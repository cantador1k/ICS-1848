
import numpy as np

n = int(input("Введіть N: "))

A = np.random.randint(1, n + 1, size=(5, 7))

C = np.intersect1d(A[0], A[-1])

print("Двовимірний масив A:")
print(A)

print("Перший рядок:", A[0])
print("Останній рядок:", A[-1])
print("Спільні елементи:", C)