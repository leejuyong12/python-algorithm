def factorial(N):
    num = 1
    for x in range(1, N+1):
        num *= x
    return num

n, m = map(int, input().split())
result = factorial(n) // (factorial(n-m) * factorial(m))
print(result)