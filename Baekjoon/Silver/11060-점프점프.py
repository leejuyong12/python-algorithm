import sys
sys.stdin = open('점프점프.txt')

N = int(input())
lst = list(map(int, input().split()))
dp = [N] * (N)
dp[0] = 0
# 0 / 1-(1) / 0-(1) / 1-(2) / 3-(3, 4, 5) / 2-((4,5,6),(5,6,7)) /
for x in range(len(lst)):
    for y in range(1, lst[x]+1):
        if x + y < N:
            dp[x+y] = min(dp[x+y], dp[x]+1) # Aj에서 하나 골라 가는거랑  비교해서 작은거
        else:
            break
if dp[N-1] != N:
    print(dp[N-1])
else:
    print(-1)
