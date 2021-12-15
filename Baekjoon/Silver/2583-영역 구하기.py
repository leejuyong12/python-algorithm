import sys
sys.stdin = open('영역구하기.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    arr[x][y] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    cnt += 1
                    queue.append((nx,ny))
    res.append(cnt)

M, N, K = map(int, input().split())
arr = [[0]* N for _ in range(M)]
res = []
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[j][i] = 1
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            bfs(i,j)
print(len(res))
res.sort()
for x in range(len(res)):
    print(res[x], end = ' ')

