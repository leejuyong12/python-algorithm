import sys
sys.stdin = open('도영이가만든맛있는음식.txt')
from itertools import combinations
N = int(input())
food = [list(map(int, input().split())) for _ in range(N)]

combs = [combinations(food, i) for i in range(1, N+1)] # 조합 개수 인덱스 맞추기 위해 1, N+1
# 2개부터 N 개 까지의 조합이 combs 에 들어간다.
ans = 10000000000
for com in combs:
    for t in com:
        S, B = 1, 0
        for s, b in t:
            S *= s
            B += b
        ans = min(ans, abs(S-B))
print(ans)