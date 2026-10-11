s = input("Введіть рядок: ")

a = -1
b = -1
c = -1

for i in range(len(s)):
    if s[i] >= '0' and s[i] <= '9':
        if a == -1:
            a = i
        elif b == -1:
            b = i
        elif c == -1:
            c = i

if c != -1:
    s = s[:a + 1] + s[c:]

print(s)