def factorial(N):
    num = 1
    for i in range(1, N+1):
        num *= i
    return num

N, K = map(int, input().split())

result = factorial(N) // (factorial(N-K) * factorial(K))
print(result % 10007)
