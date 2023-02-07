import sys
sys.stdin = open('2193-이친수.txt')

N = int(input())

# 1 -> 1    1개
# 2 -> 10   1개
# 3 -> 100 101  2개
# 4 -> 1001 1010    2개
# 5 -> 10101 10010 10001    3개
dp = [0, 1, 1]
for x in range(3, 91):
    dp.append(dp[x-1] + dp[x-2])
print(dp[N])