import math
x=float(input("Задайте x: "))
if x>=2:
    y = math.exp(x)-2**x+math.log(x+6, 3)
    print("y =", y)
elif -1<x<2:
    y = 0.5*x+math.sin(x)/(3*x+5)+math.log10(abs(x))
    print("y =", y)
else:
    y=1/math.exp(x+6)
    print("y =", y)
    