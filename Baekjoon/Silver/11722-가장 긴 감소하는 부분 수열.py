import sys
sys.stdin = open('가장긴감소하는부분수열.txt')

N = int(input())
lst = list(map(int, input().split()))

dp = [1] * N # 기본 길이는 1개

for i in range(1, N):
    for j in range(i):
        if lst[j] > lst[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
