def factorial(N):
    num = 1
    for i in range(1, N+1):
        num *= i
    return num

N, M, K = map(int, input().split())
res = 0
res2 = factorial(N) // factorial(N-M)
while M >= K:
    res += factorial(M) // factorial(M-K)
    K += 1

print(res/res2)