import sys
sys.stdin = open('1260-DFS와 BFS.txt')
from collections import deque

def dfs(V):
    visited1[V] = True
    print(V, end = ' ')
    for i in arr[V]:
        if not visited1[i]:
            dfs(i)

def bfs(V):
    visited2[V] = True
    queue = deque([V])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in arr[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True

N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

for m in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
for x in range(1, N+1):
    arr[x].sort()
dfs(V)
print()
bfs(V)
print()





