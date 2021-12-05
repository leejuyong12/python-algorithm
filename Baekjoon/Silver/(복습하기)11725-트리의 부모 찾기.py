import sys
sys.stdin = open('트리의 부모 찾기.txt')

# 내가 푼 방법
# sys.setrecursionlimit(10**6)
# N = int(input())
# tree = [[] for _ in range(N+1)]
# visited = [False for _ in range(N+1)]
# parents = [0 for _ in range(N+1)]
#
# for n in range(N-1):
#     a, b = map(int, input().split())
#     tree[a].append(b)
#     tree[b].append(a)
#
# def dfs(V):
#     visited[V] = True
#     for i in tree[V]:
#         if visited[i] == False:
#             parents[i] = V
#             dfs(i)
# dfs(1)
# for i in range(2, N+1):
#   print(parents[i])

# 상빈님 방법
from collections import deque

N = int(input())
table = [[] for _ in range(N+1)]
p = [0] * (N+1)

for i in range(N-1):
    n1, n2 = map(int, input().split())
    table[n1].append(n2)        # 무방향
    table[n2].append(n1)

Q = deque()
Q.append(1)
p[0] = p[1] = 1

while Q:
    now = Q.popleft()
    for i in table[now]:
        if not p[i]:
            p[i] = now
            Q.append(i)

for num in p[2:]:
    print(num)