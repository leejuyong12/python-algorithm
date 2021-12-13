import sys
sys.stdin = open('복권.txt')

def factorial(N):
    num = 1
    for i in range(1, N+1):
        num *= i
    return num

N, M, K = map(int, input().split())
ans = factorial(M) // (factorial(M-K) * factorial(K))   # M개중 K개 고르기
ans_1 = factorial(N-M) // (factorial(N-M-K) * factorial(M-K))   # N-M개 중 M-K개 고르기
res = factorial(N) // (factorial(N-M) * factorial(M)) # 분모 - N개중 M개를 뽑는 수
fin_ans = 0
for k in range(K, M+1):
    fin_ans += ans_1
print( ans * fin_ans / res - K/res)