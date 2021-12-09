N = int(input())
a, b = 0, 1

for n in range(N):
    a, b = b, a+b
print(a)