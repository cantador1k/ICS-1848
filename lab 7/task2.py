s = input("Введіть повідомлення: ")
n = int(input("Введіть N: "))
s2 = ""

for i in range(len(s)):
    s2 = s2 + chr(ord(s[i]) + n)

print(s2)