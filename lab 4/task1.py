import math
x=float(input("Введіть x: "))
a=(x+x**2+x**3+math.sin(x))**(1 / 3)
b=2.27*math.log(abs(x+100))
f=a/b
print("f(x) =", f)