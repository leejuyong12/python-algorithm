import sys
sys.stdin = open('1904-01타일.txt')

N = int(input())
# 1 혹은 00 ( 0이 1개만 있는건 없다)

dp = [0] *  1000001
dp[1] = 1
dp[2] = 2

# N이 1일때 - 1               1
# N이 2일때 - 00 11           2
# N이 3일때 001 100 111           3
# N이 4일때 0000 0011 1100 1001 1111    5
# N이 5일때 00001 00100 10000 11100 00111 11111 10011 11001 8

for x in range(3, N+1):
    dp[x] = (dp[x-1] + dp[x-2])%15746
print(dp[N])