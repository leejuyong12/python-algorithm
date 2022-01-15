import sys
sys.stdin = open('효율적인해킹.txt')
from collections import deque
def bfs(V):
    cnt = 1
    visited = [False] * (N + 1)
    visited[V] = True
    queue = deque([V])
    while queue:
        v = queue.popleft()
        for i in arr[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    arr[B].append(A)
result = []
max_cnt = 0
for i in range(1, N+1):
    cnt = bfs(i)
    max_cnt = max(cnt, max_cnt)
    result.append([i, cnt])
for i, cnt in result:
    if cnt == max_cnt:
        print(i, end=' ')
# 1을 해킹하면 3도 해킹 가능 1 -> 3
# 2를 해킹하면 3도 해킹 가능 2 -> 3
# 3을 해킹하면 4도 해킹 가능 3 -> 4
# 3을 해킹하면 5도 해킹 가능 3 -> 5