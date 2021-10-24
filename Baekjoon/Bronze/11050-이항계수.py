# nCk = n! // ((n-k)! * k!)

def factorial(N):
    num = 1
    for x in range(1, N+1):
        num *= x
    return num

N, K = map(int, input().split())

result = factorial(N) // (factorial(N-K) * factorial(K))
print(result)
