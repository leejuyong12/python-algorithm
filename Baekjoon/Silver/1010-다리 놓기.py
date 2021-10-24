import sys
sys.stdin = open('다리 놓기.txt')


# mCn = m! // ((m-n)! * n!)
def factorial(N):
    num = 1
    for x in range(1, N+1):
        num *= x
    return num

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    result = factorial(M) // (factorial(M-N) * factorial(N))
    print(result)