import math

def func(a, b, t):
    R=8.81*math.tan(a)+math.asin(math.cos(a+b))+math.sqrt(t+b)
    return R

a=float(input("Введіть a: "))
b=float(input("Введіть b: "))
t=float(input("Введіть t: "))

R=func(a,b,t)
print("R =", R)