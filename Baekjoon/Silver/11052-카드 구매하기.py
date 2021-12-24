import sys
sys.stdin = open('카드구매하기.txt')
# 꼭 풀이 다시 보자
N = int(input())
lst = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
for i in range(1,N+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], dp[i-k] + lst[k])
print(dp[N])