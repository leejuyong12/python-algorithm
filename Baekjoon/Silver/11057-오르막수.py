import sys
sys.stdin = open('11057-오르막수.txt')

N = int(input())
dp = [1] * 10

for x in range(N-1):
    for y in range(1, 10):
        dp[y] += dp[y-1]

print(sum(dp) % 10007)