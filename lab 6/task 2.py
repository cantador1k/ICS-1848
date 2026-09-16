import math
a=float(input("Введіть a: "))
b=float(input("Введіть b: "))
h=float(input("Введіть h: "))
x=a
for i in range(int((b-a)/h)+1):
    y=math.sqrt(abs(x))+math.copysign(abs(x)**(1/3), x)+math.sqrt(math.sqrt(abs(x)))
    print("x = %.2f   f(x) = %.3f" % (x, y))
    x=x+h