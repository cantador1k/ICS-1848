import math
a=float(input("Введіть a: "))
b=float(input("Введіть b: "))
h=float(input("Введіть h: "))
A=[]
x=a
while x <=b:
    y=math.sqrt(abs(x))+math.copysign(abs(x)**(1/3), x)+math.sqrt(math.sqrt(abs(x)))
    A.append(y)
    x=x+h
print("Список A:")
print(A)
B=sorted(A, reverse=True)[:4]
print("Список B:")
print(B)