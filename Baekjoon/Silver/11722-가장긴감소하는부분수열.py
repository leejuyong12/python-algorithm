import sys
sys.stdin = open('11722-가장긴감소하는부분수열.txt')

N = int(input())
lst = list(map(int, input().split()))
# 10 30 10 20 20 10
dp = [1] * N
# 이전꺼랑 비교해서 이전꺼가 더 크면 길이 추가
for x in range(N):
    for y in range(x):
        if lst[x] < lst[y]:
            dp[x] = max(dp[x], dp[y]+1)
print(max(dp))