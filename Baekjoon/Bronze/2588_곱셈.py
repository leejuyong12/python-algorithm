a = int(input())
b = int(input())

A = a // 100
B = (a // 10) % 10
C = a % 10

D = b // 100
E = (b // 10) % 10
F = b % 10

print(a * F)
print(a * E)
print(a * D)
print(a*b)