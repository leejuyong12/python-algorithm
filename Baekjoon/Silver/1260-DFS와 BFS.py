import sys
sys.stdin = open('1260-DFS와 BFS.txt')
from collections import deque

def dfs(V):
    visited_1[V] = True
    print(V, end = ' ')
    for i in arr[V]:
        if not visited_1[i]:
            dfs(i)

def bfs(V):
    visited_2[V] = True
    queue = deque([V])          # deque를 사용하는 이유 - list보다 연산속도가 빠르다
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in arr[v]:
            if not visited_2[i]:
                queue.append(i)
                visited_2[i] = True

N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]

for m in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
for x in range(1, N+1):     # 정점이 여러개일 경우 작은것부터니까 sort활용
    arr[x].sort()
visited_1 = [False] * (N+1)

dfs(V)
print()
visited_2 = [False] * (N+1)
bfs(V)
print()





